from django.contrib import admin
from django.urls import path, include

# register the admin url, redirect to userData urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userData.urls'))
]
