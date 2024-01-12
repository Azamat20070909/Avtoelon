from django.shortcuts import render
from .models import Car
from .serializer import CarSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import generics

# Create your views here.

class CarApi(APIView):

	def get(self, request):
		a = Car.objects.all()
		dict_data = CarSerializer(a, many = True)
		return Response(dict_data.data)

	def post(self, request):
		rasm_list = request.data.getlist('photo', [])
		serializer = CarSerializer(data = request.data)

		if serializer.is_valid():
			Car = serializer.save()
			for x in rasm_list:
				t = Image.objects.create(photo = x)
				Car.image.add(t)
			return Response(serializer.data)
		return Response(serializer.errors)






