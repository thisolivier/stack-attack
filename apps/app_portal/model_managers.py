from django.db import models

# Redundant, should be removed
class UserManager(models.Manager):
    def check_login(self, data):
        pass