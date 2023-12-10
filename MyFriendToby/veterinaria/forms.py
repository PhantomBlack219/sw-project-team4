from django import forms
from .models import *

class AddPetForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'tamaño', 'edad', 'peso', 'dineromantenimiento', 'espaciomantenimiento', 'enfermedades', 'chequeo', 'foto']

class FormularioAdopcionForm(forms.ModelForm):
    class Meta:
        model = FormularioAdopcion
        fields = ['ingresos_mensuales', 'numero_de_miembros_familia', 'tiene_otros_animales', 'pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5', 'descripcion_casa']