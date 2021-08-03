from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Light
from .serializers import LightSerializer
import serial
from rest_framework.response import Response
import time
from rest_framework import viewsets
from .forms import LightsForm
ser = serial.Serial('/dev/ttyUSB0', 9600)


# Create your views here

# ser = serial.Serial('/dev/ttyUSB0', 9600)

def index(request):
    lights = Light.objects.all()
    context = {'lights':lights}

    return render(request, 'index.html', context)

class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

def updateLight(request, pk):
    light = get_object_or_404(Light, pk=pk)
    form = LightsForm(instance=light)
    if request.method == 'POST':
        form = LightsForm(request.POST, instance=light)
        if form.is_valid():
            state = request.POST['state']
            print(f"{light},{state},")
            form.save()
            ser.write(str(f'{str(light)},{state},').encode())
            return redirect('index')
        
    context = {'light':light, 'form':form}
    return render(request, 'update-light.html', context)
