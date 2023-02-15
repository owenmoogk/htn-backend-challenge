from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from userData.models import *

# Create your views here.
class CreateUser(APIView):

  def post(self, request):
    data = request.data
    try:
      # create skill objects
      skills = []
      for skill in data["skills"]:
        newSkill = Skill(name = skill["skill"], rating = skill['rating'])
        newSkill.save()
        skills.append(newSkill)

      # create user
      user = User(name = data['name'], company = data['company'], email = data['email'], phone = data['phone'])
      user.save()
      
      # add skills to user
      for skill in skills:
        user.skills.add(skill)
      
      # add social media relationship
      socialMediaObj = SocialMedia.objects.create()
      socialMediaObj.save()
      user.socialMedia = socialMediaObj

      # save and return
      user.save()
      return Response({"userId": user.id}, status=status.HTTP_201_CREATED)
    
    # if the data was not entered correctly
    except:
      return Response({"error": "Ensure all data is entered correctly"}, status=status.HTTP_400_BAD_REQUEST)

class CheckInUser(APIView):

  # get the status of the user (regarding if they've been checked in)
  def get(self, request, user_id):
    user = User.objects.get(id = user_id)
    if user.checkedIn:
      return Response({"status": True}, status=status.HTTP_200_OK)
    return Response({"status": False}, status=status.HTTP_200_OK)

  # check the users in
  def put(self, request, user_id):
    user = User.objects.get(id = user_id)
    if user.checkedIn:
      return Response({"status": True}, status=status.HTTP_208_ALREADY_REPORTED)

    user.checkedIn = True
    user.save()
    return Response({"status": True}, status=status.HTTP_200_OK)