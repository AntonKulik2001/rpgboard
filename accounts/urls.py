from django.urls import path, include

from .views import SignUp


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]