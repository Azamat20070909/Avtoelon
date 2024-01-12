from django.shortcuts import render
from .models import *
from .serializer import *
# Create your views here.
from rest_framework import generics


class UserApi(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer