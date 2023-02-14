# Create your models here.
from django.db import models
import json

class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill)

def skillSerializer(skill):
    return {"name": skill.name, "rating": skill.rating}

def userSerializer(user):
    return {
        'name': user.name, 
        'company': user.company,
        'email': user.email,
        'phone': user.phone,
        'skills': [skillSerializer(skill) for skill in user.skills.all()] 
    }
