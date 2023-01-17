from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin,AbstractUser
from django.db import models
from django.utils import timezone



class marks(models.Model):
  sub1 = models.IntegerField()
  sub2 = models.IntegerField()
  class Meta:
    permissions = [
    ("can_add_marks", "Can add data"),
    ("can_view_marks", "Can view data"),
    ]