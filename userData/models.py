# Create your models here.
from django.db import models
import json

# skill model, stores the skill name and the skill rating
class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

# user model, storing the user data as well as a link to the user's skills
class User(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill)

# serializing the skill into a dictionary
def skillSerializer(skill):
    return {"name": skill.name, "rating": skill.rating}

# serializing the user into a dictionary
def userSerializer(user):
    return {
        'name': user.name, 
        'company': user.company,
        'email': user.email,
        'phone': user.phone,
        'skills': [skillSerializer(skill) for skill in user.skills.all()] 
    }
