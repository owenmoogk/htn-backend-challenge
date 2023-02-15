from django.urls import path
from .views import *

# register all of the urls
urlpatterns = [
    path('create-user/', CreateUser.as_view()),
    path('check-in/<int:user_id>/', CheckInUser.as_view()),
]
