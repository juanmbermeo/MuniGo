from django.urls import path
from .views import (
    custom_login_view,
    custom_logout,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    UsuarioList,
    UsuarioDetail,
    ServicioMunicipalList,
    ServicioMunicipalDetail,
    EventoList,
    EventoDetail,
    AlertaList,
    AlertaDetail,
    PagoServicioList,
    PagoServicioDetail,
    ComunicadoList,
    ComunicadoDetail,
    ContactoEmergenciaList,
    ContactoEmergenciaDetail,
    BasuraList,
    BasuraDetail,
)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
     # Rutas para el modelo Usuario
    path('api/usuarios/', UsuarioList.as_view(), name='usuario-list'),  # Listar usuarios
    path('api/usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),  # Detalle de un usuario

    # Rutas para el modelo ServicioMunicipal
    path('api/servicios/', ServicioMunicipalList.as_view(), name='servicio-list'),  # Listar servicios
    path('api/servicios/<int:pk>/', ServicioMunicipalDetail.as_view(), name='servicio-detail'),  # Detalle de un servicio

    # Rutas para el modelo Evento
    path('api/eventos/', EventoList.as_view(), name='evento-list'),  # Listar eventos
    path('api/eventos/<int:pk>/', EventoDetail.as_view(), name='evento-detail'),  # Detalle de un evento

    # Rutas para el modelo Alerta
    path('api/alertas/', AlertaList.as_view(), name='alerta-list'),  # Listar alertas
    path('api/alertas/<int:pk>/', AlertaDetail.as_view(), name='alerta-detail'),  # Detalle de una alerta

    # Rutas para el modelo PagoServicio
    path('api/pagos/', PagoServicioList.as_view(), name='pago-list'),  # Listar pagos
    path('api/pagos/<int:pk>/', PagoServicioDetail.as_view(), name='pago-detail'),  # Detalle de un pago

    # Rutas para el modelo Comunicado
    path('api/comunicados/', ComunicadoList.as_view(), name='comunicado-list'),  # Listar comunicados
    path('api/comunicados/<int:pk>/', ComunicadoDetail.as_view(), name='comunicado-detail'),  # Detalle de un comunicado

    # Rutas para el modelo ContactoEmergencia
    path('api/contactos/', ContactoEmergenciaList.as_view(), name='contacto-list'),  # Listar contactos
    path('api/contactos/<int:pk>/', ContactoEmergenciaDetail.as_view(), name='contacto-detail'),  # Detalle de un contacto

    # Rutas para el modelo Basura
    path('api/basura/', BasuraList.as_view(), name='basura-list'),  # Listar basura
    path('api/basura/<int:pk>/', BasuraDetail.as_view(), name='basura-detail'),  # Detalle de un registro de basura
]
