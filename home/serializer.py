# api/serializer.py
from rest_framework import serializers
from .models import Usuario, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Barrio, TipoBasura, Basura

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'telefono', 'email', 'avatar']
"""        
class ServicioMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMunicipal
        fields = '__all__'"""
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'        

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'        
        
class PagoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoServicio
        fields = '__all__' 
        
class ComunicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicado
        fields = '__all__' 
        
class ContactoEmergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoEmergencia
        fields = '__all__' 
        
class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__' 
        
class TipoBasuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBasura
        fields = '__all__' 
        
class BasuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basura
        fields = '__all__'  
