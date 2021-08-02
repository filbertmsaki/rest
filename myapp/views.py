from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Road
from .serializers import RoadSerializer
import serial
from rest_framework.response import Response
import time

# Create your views here

ser = serial.Serial('/dev/ttyUSB0', 9600)

class RoadViewSet(APIView):
   # queryset = Road.objects.all()
   # serializer_class = RoadSerializer
   def get(self, request, format=None):
       roads = Road.objects.all()
       serializer = RoadSerializer(roads, many=True)
       return Response(serializer.data)

   def post(self, request, format=None):
       data = request.data
       print(f'{data}')
       ser.write(data['state'])
       serializer = RoadSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

