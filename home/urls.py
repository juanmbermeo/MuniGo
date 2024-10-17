from django.urls import path, include
from .views import (
    custom_login_view,
    custom_logout,
    CustomPasswordResetView,
    CustomPasswordResetDoneView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView,
    UsuarioViewSet, EventoViewSet, AlertaViewSet, PagoServicioViewSet, ComunicadoViewSet, ContactoEmergenciaViewSet, BarrioViewSet, TipoBasuraViewSet, BasuraViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
#router.register(r'servicios-municipal', ServicioMunicipalViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'alerta', AlertaViewSet)
router.register(r'pago-servicio', PagoServicioViewSet)
router.register(r'comunicado', ComunicadoViewSet)
router.register(r'contacto-emergencia', ContactoEmergenciaViewSet)
router.register(r'barrio', BarrioViewSet)
router.register(r'tipos-basura', TipoBasuraViewSet)
router.register(r'basura', BasuraViewSet)

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('v1/', include(router.urls)),

]
