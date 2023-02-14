# Create your models here.
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill)
