from django.db import models

class UserManager(models.Manager):
    
    def check_login(self, data):
        pass