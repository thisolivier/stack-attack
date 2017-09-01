# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from model_fields import PasswordField
from django.core.validators import EmailValidator

from model_managers import UserManager

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254, blank=False, unique=True)
    password = PasswordField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = UserManager()