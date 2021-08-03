from django.forms import ModelForm
from .models import Light

class LightsForm(ModelForm):
    class Meta:
        model = Light
        fields = ['state',]