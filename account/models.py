
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.PositiveIntegerField(null=True, blank=False)
    address = models.CharField(max_length=50, null=True, blank=False)
