from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator

import re

def validar_telefono(value):
    # Expresión regular para validar el formato de teléfono (ajusta según tu formato)
    regex = r'^\+\d{1,3}\s\d{8,14}$'  # Ejemplo: +57 3112345678
    if not re.match(regex, value):
        raise ValidationError(('El número de teléfono debe tener el formato +XXX XXXXXXXXX.'), params={'value': value})

class Usuario(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios',  # Nombre único para esta relación
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios',  # Nombre único para esta relación
        blank=True
    )
    telefono = models.CharField(max_length=15, unique=True, validators=[validar_telefono])
    email = models.EmailField(unique=True, validators=[EmailValidator()],
                             error_messages={'unique': "Ya existe un usuario con ese correo electrónico."})
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

class ServicioMunicipal(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False,)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=255)
    contacto = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+\d{1,3}\s?\d{8,14}$',
                message="El número de teléfono debe tener el formato +XXX XXXXXXXXX"
            )
        ]
    )
    email = models.EmailField(blank=True)   
    hora_apertura = models.TimeField()
    hora_cierre = models.TimeField()
    icono = models.ImageField(upload_to='iconos/')  # Para almacenar iconos
    
    class Meta:
        verbose_name_plural = 'Servicios Municipales'
        verbose_name = 'Servicio Municipal'
        ordering = ['nombre']

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField()
    fecha_evento = models.DateField()
    hora_evento = models.TimeField()
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    
    def incrementar_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])
        
    def __str__(self):
        return self.titulo

class Alerta(models.Model):
    id_alerta = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, null=False, blank=False)
    descripcion = models.TextField()
    fecha= models.DateTimeField(auto_now_add=True)
    ubicacion = models.CharField(max_length=255, blank=True, null=True)
    tipo_alerta = models.CharField(max_length=50, choices={'emergencia': 'Emergencia','informacion': 'Información',}, default='informacion')    
    imagenes = models.FileField(upload_to='imagenes_alertas/', blank=True, null=True)  # Permite múltiples imágenes
    estado = models.CharField(max_length=20, choices=[
        ('activa', 'Activa'),
        ('resuelta', 'Resuelta'),
        ('cancelada', 'Cancelada'),
    ], default="activa")
    
    def __str__(self):
        return self.titulo
        
class PagoServicio(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100, null=False)
    icono = models.ImageField(upload_to='iconos_recoleccion/')
    link = models.URLField(validators=[URLValidator()])

class Comunicado(models.Model):
    id_comunicado = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_comunicados/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    compartidos = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('borrado', 'Borrado'),
    ], default='activo')

    def incrementar_likes(self):
        self.likes += 1
        self.save(update_fields=['likes'])

    def incrementar_compartidos(self):
        self.compartidos += 1
        self.save(update_fields=['compartidos'])

    def save(self, *args, **kwargs):
        # Si el objeto ya existe, no permitimos modificar likes y compartidos
        if self.pk:
            del self.__dict__['likes']
            del self.__dict__['compartidos']
        super().save(*args, **kwargs)

    def clean(self):
        if self.pk and (self.likes != self._original_likes or self.compartidos != self._original_compartidos):
            raise ValidationError('No puedes modificar los campos likes y compartidos.')
        
    def __str__(self):
        return self.titulo

class ContactoEmergencia(models.Model):
    id_contacto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=15, null=False)
    icono = models.ImageField(upload_to='iconos_emergencia/')
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class TipoBasura(models.Model):
    tipo_basura = models.CharField(max_length=50)

class Basura(models.Model):
    id_basura = models.AutoField(primary_key=True)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    tipo_basura = models.ForeignKey(TipoBasura, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Recogida de basura en el barrio {self.barrio} el {self.fecha} a las {self.hora}"
    

