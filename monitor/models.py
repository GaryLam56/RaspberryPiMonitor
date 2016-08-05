from django.db import models
from django.contrib.auth.models import User


class Raspberry(models.Model):
    temperature = models.DecimalField(decimal_places=1, max_digits=3)
    memory_used = models.IntegerField()

    def __str__(self):
        return 'RaspberryPi'
