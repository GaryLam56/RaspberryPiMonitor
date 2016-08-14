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
    return line.split()[1:7]


def getTemperature():
    # returns temperature in celcius
    return float(os.popen("sudo vcgencmd measure_temp").readline()[5:-3])


def getUptime():
    return os.popen("uptime").readline().split()


def getCpuUsage():
    # returns an array of cpu usage percentages
    theLines = os.popen("mpstat -P ALL")
    theLines.readline()
    theLines.readline()
    theLines.readline()
    theLines.readline()
    cpu1 = 100 - float(theLines.readline().split()[12])
    cpu2 = 100 - float(theLines.readline().split()[12])
    cpu3 = 100 - float(theLines.readline().split()[12])
    cpu4 = 100 - float(theLines.readline().split()[12])
    return [cpu1, cpu2, cpu3, cpu4]


def test(request):
    if request.method == 'GET':
        response_data = {}
        response_data['temp'] = getTemperature()
        response_data['mem_used'] = int(getRamStats()[1][:-1])
        response_data['mem_avail'] = int(getRamStats()[2][:-1])
        response_data['mem_total'] = int(getRamStats()[0][:-1])
        response_data['mem_buffer'] = int(getRamStats()[4][:-1])
        response_data['mem_cache'] = int(getRamStats()[5][:-1])
        response_data['up_day'] = int(getUptime()[2])
        response_data['up_hour'] = int(getUptime()[4])
        response_data['up_minute'] = int(getUptime()[6])
        cpuList = getCpuUsage()
        response_data['cpu0'] = cpuList[0]
        response_data['cpu1'] = cpuList[1]
        response_data['cpu2'] = cpuList[2]
        response_data['cpu3'] = cpuList[3]
        return HttpResponse(json.dumps(response_data), content_type="application/json")


class MonitorList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = PiSerializer
