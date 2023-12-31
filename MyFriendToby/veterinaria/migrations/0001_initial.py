# Generated by Django 2.2.24 on 2023-12-09 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoptado', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=255)),
                ('edad', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('tamaño', models.CharField(choices=[('Grande', 'Grande'), ('Mediano', 'Mediano'), ('Pequeño', 'Pequeño')], max_length=10)),
                ('enfermedades', models.CharField(default='ninguna', max_length=255)),
                ('foto', models.TextField()),
                ('dineromantenimiento', models.IntegerField(null=True)),
                ('espaciomantenimiento', models.CharField(max_length=255, null=True)),
                ('chequeo', models.DateField(null=True)),
                ('prox_chequeo', models.DateField(null=True)),
                ('id_adoptante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adoptante', to=settings.AUTH_USER_MODEL)),
                ('id_donante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donante', to=settings.AUTH_USER_MODEL)),
                ('id_veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='veterinario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
