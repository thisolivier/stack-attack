# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from model_fields import PasswordField
from validators import name_validator

from model_managers import UserManager

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, blank=False, unique=True)
    password = PasswordField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[name_validator])
    last_name = models.CharField(max_length=50, validators=[name_validator])
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class Instructor(models.Model):
    name = models.CharField(max_length=80, validators=[name_validator])
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)