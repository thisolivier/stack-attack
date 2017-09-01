# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from model_fields import PasswordField

from model_managers import UserManager

# Create your models here.
class User(models.Model):
    email = models.EmailField()
    password = PasswordField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = UserManager()