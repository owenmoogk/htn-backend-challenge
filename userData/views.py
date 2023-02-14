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
    print(skill)
    returnData[skill['name']] = skill['rating']
  return returnData

class UserList(APIView):

  def get(self, request):
    users = User.objects.all()
    data = [userSerializer(user) for user in users]

    return Response(data, status=status.HTTP_200_OK)

class UserInfo(APIView):

  def get(self, request, user_id):
    user = User.objects.get(id = user_id)
    data = userSerializer(user)
    return Response(data, status=status.HTTP_200_OK)

  def put(self, request, user_id):

    data = request.data

    user = User.objects.get(id = user_id)

    for key in data:
      if key == 'skills':
        updatedSkills = serializeSkills(data[key])
        for skillObj in user.skills.all():
          if skillObj.name in updatedSkills:
            skillObj.rating = updatedSkills[skillObj.name]
            skillObj.save()
      else:
        setattr(user, key, data[key])
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