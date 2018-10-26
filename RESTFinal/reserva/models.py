from django.db import models

# Create your models here.
class Reserva(models.Model):
    precio = models.CharField(max_length=50)
    fecha_inicio = models.CharField(max_length=40)
    fecha_caduca  = models.CharField(max_length=30)
    carro = models.CharField(max_length=30)
    parqueadero = models.CharField(max_length=30)
    oferente = models.CharField(max_length=30)
