from django.db import models
from django_userpack.models import AdvancedBaseUser


class CustomUser(AdvancedBaseUser):
    national_code = None