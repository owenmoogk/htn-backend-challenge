from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.forms.models import model_to_dict
from django.core import serializers
import json
from .models import *

# the function turns the slightly messier skill data into a rating dictionary's
def serializeSkills(skills):
  returnData = {}
  for skill in skills:
    returnData[skill['name']] = skill['rating']
  return returnData

# return all of the users in json
class UserList(APIView):

  def get(self, request):
    users = User.objects.all()
    data = [userSerializer(user) for user in users]

    return Response(data, status=status.HTTP_200_OK)

class UserInfo(APIView):

  # return a single users data in a json
  def get(self, request, user_id):
    user = User.objects.get(id = user_id)
    data = userSerializer(user)
    return Response(data, status=status.HTTP_200_OK)

  # update a user's data
  def put(self, request, user_id):

    data = request.data

    user = User.objects.get(id = user_id)

    for key in data:
      
      # if the data to be updated is in the skills section
      if key == 'skills':
        updatedSkills = serializeSkills(data[key])

        # loop through skills and check if they need to be updated
        for skillObj in user.skills.all():
          if skillObj.name in updatedSkills:
            skillObj.rating = updatedSkills[skillObj.name]
            skillObj.save()
            updatedSkills.pop(skillObj.name)
        
        # for the skills that don't need to be updated
        for skill in updatedSkills:
          newSkill = Skill(name=skill, rating=updatedSkills[skill])
          newSkill.save()
          user.skills.add(newSkill)

      # otherwise we just update the current user data
      else:
        setattr(user, key, data[key])
    
    # save the user model
    user.save()

    return Response(userSerializer(user), status=status.HTTP_200_OK)

class Skills(APIView):
  
  def get(self, request):
    try:
      minFreq = int(request.GET['min_frequency'])
    except:
      minFreq = 0
    try:
      maxFreq = int(request.GET['max_frequency'])
    except:
      maxFreq = float('inf')

    skills = Skill.objects.all()
    aggregate = {}
    for skillObj in skills:
      if skillObj.name in aggregate:
        aggregate[skillObj.name] += 1
      else:
        aggregate[skillObj.name] = 0

    returnData = {}
    for key in aggregate:
      if aggregate[key] <= maxFreq and aggregate[key] >= minFreq:
        returnData[key] = aggregate[key]

    return Response(returnData, status=status.HTTP_200_OK)