from django.db import models
from django.contrib.auth.models import User


class Raspberry(models.Model):
    user = models.ForeignKey(User, default=1)
    temperature = models.DecimalField(decimal_places=2, max_digits=4)
    memory_used = models.IntegerField()

    def __str__(self):
        return 'RaspberryPi'
