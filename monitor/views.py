from django.shortcuts import render
import os
import sys
from rest_framework import generics
from monitor.serializers import PiSerializer
from monitor.models import Raspberry
from .forms import RaspberryForm


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
    return render(request, 'monitor/index.html')


def getRamStats():
    free = os.popen("free -h")
    free.readline()
    line = free.readline()
    # total, used, and free ram
    return line.split()[1:4]


def getTemperature():
    # returns temperature in celcius
    free = os.popen("sudo vcgencmd measure_temp")
    print(sys.stderr, free)
    print(sys.stderr, free.readline())
    print(sys.stderr, os.popen("sudo vcgencmd measure_temp"))
    print(sys.stderr, os.popen("sudo vcgencmd measure_temp").readline())
    print(sys.stderr, os.popen("sudo vcgencmd measure_temp").readline()[5:-3])
    return os.popen("sudo vcgencmd measure_temp").readline()[5:-3]


class MonitorList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = PiSerializer
