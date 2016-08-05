from rest_framework import serializers
from monitor.models import Raspberry

class PiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raspberry
        field = ('temperature', 'memory_used')