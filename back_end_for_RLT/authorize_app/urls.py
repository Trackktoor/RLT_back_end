from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('user_registration', views.user_registration.as_view(), name='user_registration'),
    path('', views.home.as_view(), name='home')
]