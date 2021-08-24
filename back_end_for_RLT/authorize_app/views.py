from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser

# Create your views here.

class user_registration(APIView):
    parser_classes = (JSONParser, FormParser)

    def post(self, request):
        first_name, password, email, last_name = \
            request.data['first_name'],\
            request.data['password'],\
            request.data['email'],\
            request.data['last_name']
        user = User.objects.create_user(first_name, email, password)

        user.first_name = first_name
        user.last_name = last_name
        user.save()

class home(APIView):
    parser_classes = (JSONParser, FormParser)

    def get(self, request):
        return render(
            request,
            'home.html',
        )

    def post(self, request):
        return render(
            request,
            'home/home.html',
        )