from django import forms
from .models import *

class AddPetForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'tamaño', 'edad', 'peso', 'dineromantenimiento', 'espaciomantenimiento', 'enfermedades', 'chequeo', 'foto']
