# Create your models here.
from django.db import models

# skill model, stores the skill name and the skill rating
class Skill(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

# model to store social media information
class SocialMedia(models.Model):
    linkedin = models.CharField(max_length=100, null=True)
    discord = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    thingiverse = models.CharField(max_length=100, null=True)
    

# user model, storing the user data as well as a link to the user's skills
class User(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill, null=True)

    # 'private' variables, to track user information that should not be shared
    checkedIn = models.BooleanField(default=False)
    socialMedia = models.OneToOneField(SocialMedia, on_delete=models.CASCADE, null=True)

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

def socialMediaSerializer(socialMedia):
    return {
        'linkedin': socialMedia.linkedin, 
        'thingiverse': socialMedia.thingiverse,
        'discord': socialMedia.discord,
        'instagram': socialMedia.instagram,
        'github': socialMedia.github, 
        'twitter': socialMedia.twitter,
        'facebook': socialMedia.facebook
    }
