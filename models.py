from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(User):
    year = models.IntegerField(default=0)
