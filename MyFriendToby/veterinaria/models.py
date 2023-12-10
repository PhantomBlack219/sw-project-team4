from django.db import models
from django.contrib.auth.models import User

class Mascota(models.Model):
    TAMANO_CHOICES = [
        ('Grande', 'Grande'),
        ('Mediano', 'Mediano'),
        ('Pequeño', 'Pequeño'),
    ]

    id_donante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donante',null=True)
    id_veterinario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='veterinario',null=True)
    id_adoptante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='adoptante', null=True)
    adoptado = models.BooleanField(default=False)
    nombre = models.CharField(max_length=255, null=False)
    edad = models.IntegerField(null=False)
    peso = models.IntegerField(null=False)
    tamaño = models.CharField(max_length=10, choices=TAMANO_CHOICES, null=False)
    enfermedades = models.CharField(max_length=255, default='ninguna')
    foto = models.TextField(null=False)
    dineromantenimiento = models.IntegerField(null=True)
    espaciomantenimiento = models.CharField(max_length=255, null=True)
    chequeo = models.DateField(null=False)
    prox_chequeo = models.DateField(null=True)

    def get_adoptadp(self):
        return self.adoptado

    def get_nombre(self):
        return self.nombre
        
    def get_edad(self):
        return self.edad

    def get_peso(self):
        return self.peso

    def get_tamaño(self):
        return self.tamaño
    
    def get_enfermedades(self):
        return self.enfermedades
    
    def get_foto(self):
        return self.foto
    
    def get_dineromantenimiento(self):
        return self.dineromantenimiento

    def get_espaciomantenimiento(self):
        return self.espaciomantenimiento

    def get_chequeo(self):
        return self.chequeo

    def get_prox_chequeo(self):
        return self.prox_chequeo

    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.nombre, self.id)

