from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:user_id>/', UserInfo.as_view())
]
