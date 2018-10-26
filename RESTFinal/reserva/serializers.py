
from rest_framework import serializers
from . import models


class ReservaSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('precio', 'fecha_inicio','fecha_caduca', 'carro', 'parqueadero', 'oferente',)
        model = models.Reserva
