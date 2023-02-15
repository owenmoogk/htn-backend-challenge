from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *

class SocialMedia(APIView):

  # return a single users data in a json
  def get(self, request, user_id):
    user = User.objects.get(id = user_id)
    socials = user.socialMedia
    return Response(socialMediaSerializer(socials), status=status.HTTP_200_OK)

  # update a user's data
  def put(self, request, user_id):

    data = request.data

    user = User.objects.get(id = user_id)
    socials = user.socialMedia

    for key in data:
      setattr(socials, key, data[key])
    
    # save the user model
    socials.save()

    return Response(socialMediaSerializer(socials), status=status.HTTP_200_OK)