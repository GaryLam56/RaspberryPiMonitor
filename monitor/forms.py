from django import forms
from .models import Raspberry


class RaspberryForm(forms.ModelForm):

    class Meta:
        model = Raspberry
        fields = ['temperature', 'memory_used']