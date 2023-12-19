from rest_framework import serializers
from .models import Inscrito, Institucion

class inscrito_serializer(serializers.ModelSerializer):
    class Meta:
        model = Inscrito
        fields = '__all__'

class institucion_serializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class autor_serializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=20)
    seccion = serializers.CharField(max_length=30)