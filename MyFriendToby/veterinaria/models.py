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
    chequeo = models.DateField(default='2023-12-04' ,null=False)
    prox_chequeo = models.DateField(null=True)

    def get_adoptado(self):
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

class FormularioAdopcion(models.Model):
    Pregunta1_CHOICES = [
        ('1 a 2 veces al dia', '1 a 2 veces al dia'),
        ('2 o 3 veces al dia', '2 o 3 veces al dia'),
        ('Mas de tres veces', 'Mas de tres veces'),
        ('No aplica', 'No aplica')
    ]
    Pregunta2_CHOICES = [
        ('1 vez a la semana', '1 vez a la semana'),
        ('1 a 3 veces a la semana', '1 a 3 veces a la semana'),
        ('Mas de 3 veces a la semana', 'Mas de 3 veces a la semana'),
    ]
    Pregunta3_CHOICES = [
        ('Comida seca especial para mascotas', 'Comida seca especial para mascotas'),
        ('Comida seca y comida casera', 'Comida seca y comida casera'),
        ('comida casera', 'comida casera'),
        ('No aplica', 'No aplica')
    ]
    
    Pregunta4_CHOICES = [
        ('De 1 a 3 veces al mes', 'De 1 a 3 veces al mes'),
        ('De 1 a 3 veces cada 2 meses', 'De 1 a 3 veces cada 2 meses'),
        ('Cada vez que tenga olor fuerte', 'Cada vez que tenga olor fuerte'),
    ]
    
    Pregunta5_CHOICES = [
        ('De 1 a 3 veces cada 2 meses', 'De 1 a 3 veces cada 2 meses'),
        ('1 vez por mes', '1 vez por mes'),        
        ('1 vez por semana', '1 vez por semana'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario', null=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='mascota', null=True)
    ingresos_mensuales = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_miembros_familia = models.IntegerField()
    tiene_otros_animales = models.BooleanField(default=False)
    pregunta1= models.CharField(max_length=50, choices=Pregunta1_CHOICES, null=False)
    pregunta2=models.CharField(max_length=50, choices=Pregunta2_CHOICES, null=False)
    pregunta3= models.CharField(max_length=50, choices=Pregunta3_CHOICES, null=False)
    pregunta4=models.CharField(max_length=50, choices=Pregunta4_CHOICES, null=False)
    pregunta5= models.CharField(max_length=50, choices=Pregunta5_CHOICES, null=False)
    descripcion_casa = models.TextField()

