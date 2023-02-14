from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('users/', UserList.as_view()),
    path('user/<int:user_id>/', UserInfo.as_view()),
    path(r'skills/', Skills.as_view())
]
