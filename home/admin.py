from django.contrib import admin
from .models import Evento, Usuario, ServicioMunicipal, Alerta, Basura, Comunicado, ContactoEmergencia, PagoServicio, Barrio, TipoBasura
from unfold.admin import ModelAdmin
from django.utils.html import format_html

@admin.register(Evento)
class EventoAdmin(ModelAdmin):
    list_display = ('titulo', 'fecha_evento', 'hora_evento', 'ubicacion')
    search_fields = ('titulo',)
    list_filter = ('fecha_evento',)
    ordering = ('titulo',)  # Ordenar por fecha de evento de forma descendente
    readonly_fields = ('likes',)
    fieldsets = (
        ('Información básica', {'fields': ('titulo', 'descripcion')}),
        ('Detalles del evento', {'fields': ('fecha_evento', 'hora_evento', 'ubicacion')}),
        ('Multimedia', {'fields': ('imagen', 'likes')}),
    )


@admin.register(Usuario)
class UsuarioAdmin(ModelAdmin):
    list_display = ('username', 'email', 'telefono', 'avatar_image')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    fieldsets = (
        ('Información básica', {'fields': ('username', 'email', 'password')}),
        ('Información adicional', {'fields': ('telefono', 'avatar')}),
    )
    
        # Método para mostrar la imagen en el panel de administración
    def avatar_image(self, obj):
        if obj.avatar:  # Verificar si existe una imagen en el campo 'avatar'
            return format_html('<img src="{}" style="width: 50px; height:50px; border-radius: 50%;" />', obj.avatar.url)
        return "No image"

    avatar_image.short_description = 'Avatar'  # Nombre de la columna en el admin


@admin.register(ServicioMunicipal)
class ServicioMunicipalAdmin(ModelAdmin):
    list_display = ('nombre', 'ubicacion', 'contacto', 'hora_apertura', 'hora_cierre')
    search_fields = ('nombre',)
    list_filter = ('hora_apertura',)
    ordering = ('nombre',)
    readonly_fields = ('id_servicio',)
    fieldsets = (
        ('Información básica', {'fields': ('nombre', 'descripcion')}),
        ('Contacto', {'fields': ('ubicacion', 'contacto', 'email')}),
        ('Horario', {'fields': ('hora_apertura', 'hora_cierre')}),
    )


@admin.register(Alerta)
class AlertaAdmin(ModelAdmin):
    list_display = ('titulo', 'fecha', 'tipo_alerta', 'estado')
    search_fields = ('titulo',)
    list_filter = ('tipo_alerta', 'estado')
    ordering = ('titulo',) 
    readonly_fields = ('fecha',)
    fieldsets = (
        ('Información básica', {'fields': ('titulo', 'descripcion')}),
        ('Detalles de la alerta', {'fields': ('fecha', 'ubicacion', 'tipo_alerta', 'estado')}),
        ('Multimedia', {'fields': ('imagenes',)})
    )


@admin.register(PagoServicio)
class PagoServicioAdmin(ModelAdmin):
    list_display = ('nombre_servicio', 'icono', 'link',)
    search_fields = ('nombre_servicio',)
    list_filter = ('nombre_servicio',)
 
    
@admin.register(Comunicado)
class ComunicadoAdmin(ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion', 'estado', 'likes', 'compartidos')
    search_fields = ('titulo',)
    list_filter = ('estado', 'titulo')
    readonly_fields = ('fecha_publicacion', 'likes', 'compartidos')
    fieldsets = (
        ('Información básica', {'fields': ('titulo', 'texto')}),
        ('Detalles', {'fields': ('imagen', 'fecha_publicacion', 'estado')}),
        ('Estadísticas', {'fields': ('likes', 'compartidos')}),
    )
    

@admin.register(ContactoEmergencia)
class ContactoEmergenciaAdmin(ModelAdmin):
    list_display = ('nombre', 'telefono', 'icono')
    search_fields = ('nombre',)
    fieldsets = (
        ('Información básica', {'fields': ('nombre', 'telefono')}),
        ('Imagen', {'fields': ('icono',)})
    )
      

@admin.register(Barrio)
class BarrioAdmin(ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(TipoBasura)
class TipoBasuraAdmin(ModelAdmin):
    list_display = ('tipo_basura',)
    search_fields = ('tipo_basura',)


@admin.register(Basura)
class RecoleccionBasuraAdmin(ModelAdmin):
    list_display = ('barrio', 'fecha', 'hora', 'tipo_basura')
    list_filter = ('barrio', 'fecha', 'tipo_basura')
    search_fields = ('barrio__nombre',)