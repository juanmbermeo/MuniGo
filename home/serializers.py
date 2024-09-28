from rest_framework import serializers
from .models import Usuario, ServicioMunicipal, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Basura

# Serializer para el modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'telefono', 'avatar']
        # Incluye solo los campos necesarios para la API.

# Serializer para el modelo ServicioMunicipal
class ServicioMunicipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioMunicipal
        fields = '__all__'  # Incluye todos los campos del modelo.

# Serializer para el modelo Evento
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

# Serializer para el modelo Alerta
class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

# Serializer para el modelo PagoServicio
class PagoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoServicio
        fields = '__all__'

# Serializer para el modelo Comunicado
class ComunicadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunicado
        fields = '__all__'

# Serializer para el modelo ContactoEmergencia
class ContactoEmergenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactoEmergencia
        fields = '__all__'

# Serializer para el modelo Basura
class BasuraSerializer(serializers.ModelSerializer):
    # Incluir el nombre del barrio y tipo_basura como campos adicionales
    barrio_nombre = serializers.CharField(source='barrio.nombre', read_only=True)
    tipo_basura_nombre = serializers.CharField(source='tipo_basura.tipo_basura', read_only=True)
    
    class Meta:
        model = Basura
        fields = ['id_basura', 'barrio', 'barrio_nombre', 'fecha', 'hora', 'tipo_basura', 'tipo_basura_nombre']
        # Incluye campos adicionales que referencian las relaciones.

