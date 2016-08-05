from django.db import models
from django.contrib.auth.models import User


class Raspberry(models.Model):
    temperature = models.CharField(max_length=4)
    memory_used = models.IntegerField()

    def __str__(self):
        return 'RaspberryPi'
