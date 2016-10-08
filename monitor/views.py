from django.shortcuts import render
from django.contrib.auth import authenticate, login
import os
from rest_framework import generics
from monitor.serializers import PiSerializer
from monitor.models import Raspberry
from django.http import HttpResponse
import json
import re
import time


def index(request):
    # if user is not logged in make them
    if not request.user.is_authenticated():
        return render(request, 'monitor/login_user.html')
    else:
        return render(request, 'monitor/index.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'monitor/index.html')
        else:
            return render(request, 'monitor/login_user.html', {'error_message': 'Invalid login'})
    return render(request, 'monitor/login_user.html')


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
    return os.popen("uptime -p").readline()[3:]


def getCpuUsage():
    class PiStats(object):
        def __init__(self, w):
            self.lastCPUInfo = {'total':0, 'active':0}
            self.currentCPUInfo = {'total':0, 'active':0, 'w':w}
            self.temp_in_celsius = None

        def calculate_cpu_percentage(self):
            total_diff = self.currentCPUInfo['total'] - self.lastCPUInfo['total']
            active_diff = self.currentCPUInfo['active'] - self.lastCPUInfo['active']
            return round(float(active_diff) / float(total_diff), 3) * 100.00

        def update_stats(self):
            self.lastCPUInfo['total'] = self.currentCPUInfo['total']
            self.lastCPUInfo['active'] = self.currentCPUInfo['active']
            self.currentCPUInfo['total'] = 0
            with open('/proc/stat', 'r') as cpu_file:
                for i, line in enumerate(cpu_file):
                    if i == w:
                        cpuStats = re.findall('([0-9]+)', line.strip())
                        self.currentCPUInfo['idle'] = int(cpuStats[3]) + int(cpuStats[4])
                        for t in cpuStats:
                            self.currentCPUInfo['total'] += int(t)

                        self.currentCPUInfo['active'] = self.currentCPUInfo['total'] - self.currentCPUInfo['idle']
                        self.currentCPUInfo['percent'] = self.calculate_cpu_percentage()

        def get_cpu_info(self):
            return self.currentCPUInfo

    w = 0
    list_cpu_percentage = []
    while w < 4:
        stats = PiStats(w)
        stats.update_stats()
        time.sleep(1)
        stats.update_stats()
        cpu_info = stats.get_cpu_info()
        list_cpu_percentage.append(round(cpu_info['percent'], 3))
        w += 1
    return list_cpu_percentage


def test(request):
    if request.method == 'GET':
        response_data = {}
        response_data['temp'] = getTemperature()
        response_data['mem_used'] = float(getRamStats()[1][:-1])
        response_data['mem_avail'] = float(getRamStats()[2][:-1])
        response_data['mem_total'] = float(getRamStats()[0][:-1])
        response_data['mem_buffer'] = float(getRamStats()[4][:-1])
        response_data['mem_cache'] = float(getRamStats()[5][:-1])
        response_data['up_time'] = getUptime()
        cpu_list = getCpuUsage()
        response_data['cpu0'] = cpu_list[0]
        response_data['cpu1'] = cpu_list[1]
        response_data['cpu2'] = cpu_list[2]
        response_data['cpu3'] = cpu_list[3]
        return HttpResponse(json.dumps(response_data), content_type="application/json")


class MonitorList(generics.ListCreateAPIView):
    queryset = Raspberry.objects.all()
    serializer_class = PiSerializer
