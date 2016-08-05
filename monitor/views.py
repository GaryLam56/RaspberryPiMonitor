from django.shortcuts import render
import os
from rest_framework import generics
from monitor.serializers import PiSerializer
from monitor.models import Raspberry


def index(request):
    # if user is not logged in make them
    if not request.user.is_authenticated():
        return render(request, 'monitor/login_user.html')
    else:
        # Displays the main page/List all of the user's files
        mem_stats = getRamStats()
        # cpu_stats = getCPUStats()
        temp = getTemperature()
        return render(request, 'monitor/index.html', {'mem_stats': mem_stats})


def getRamStats():
    free = os.popen("free -h")
    free.readline()
    line = free.readline()
    # total, used, and free ram
    return line.split()[1:4]


def getTemperature():
    # returns temperature in celcius
    return os.popen("vcgencmd measure_temp").readline()[5:-2]


class MonitorList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = PiSerializer