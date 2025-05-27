from consultas.models import *
from rest_framework import serializers


class consultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = [
            'id',
            'nombre',
            'descripcion',
            'edad',
            'sintomas'
        ]

class IntervencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intervencion
        fields = [
            'id',
            'descripcion',
            'estrategia'
        ]
    
class ApoyoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoyo
        fields = [
            'id',
            'descripcion',
            'tipos'
        ]

class SintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintomas
        fields = [
            'edad',
            'caracteristicas',
            'factores'
        ]



