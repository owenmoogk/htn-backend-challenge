from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.forms.models import model_to_dict
from django.core import serializers
import json
from .models import *


class UserList(APIView):

  def get(self, request):
    users = User.objects.all()
    data = [userSerializer(user) for user in users]

    return Response(data, status=status.HTTP_200_OK)

class UserInfo(APIView):

  def get(self, request, user_id):
    print(user_id)
    user = User.objects.get(pk = 1)
    data = userSerializer(user)
    return Response(data, status=status.HTTP_200_OK)