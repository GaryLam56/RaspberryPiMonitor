from django.shortcuts import render
import os
import sys
from rest_framework import generics
from monitor.serializers import PiSerializer
from monitor.models import Raspberry
from .forms import RaspberryForm
from django.http import HttpResponse
import json


def index(request):
    # if user is not logged in make them
    #if not request.user.is_authenticated():
    #   return render(request, 'monitor/login_user.html')
    #else:
    mem_stats = getRamStats()
    temp = getTemperature()
    form = RaspberryForm(request.POST or None, request.FILES or None)
    pi = form.save(commit=False)
    pi.temperature = temp
    pi.memory_used = int(mem_stats[1][:-1])
    pi.save()
    context = {"mem_stats": mem_stats, "temp": temp}
    return render(request, 'monitor/index.html', context)


def getRamStats():
    free = os.popen("free -h")
    free.readline()
    line = free.readline()
    # total, used, and free ram
    return line.split()[1:4]


def getTemperature():
    # returns temperature in celcius
    return float(os.popen("sudo vcgencmd measure_temp").readline()[5:-3])


def test(request):
    if request.method == 'GET':
        response_data = {}
        response_data['temp'] = getTemperature()
        response_data['mem_stats'] = int(getRamStats())
        return HttpResponse(json.dumps(response_data), content_type="application/json")


class MonitorList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = PiSerializer
