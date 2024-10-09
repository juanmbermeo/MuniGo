from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Usuario, ServicioMunicipal, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Barrio, TipoBasura, Basura
from .serializer import UsuarioSerializer, ServicioMunicipalSerializer, EventoSerializer, AlertaSerializer, PagoServicioSerializer, ComunicadoSerializer, ContactoEmergenciaSerializer, BarrioSerializer, TipoBasuraSerializer, BasuraSerializer


@never_cache
def custom_login_view(request):
    if request.user.is_authenticated:
        return redirect('admin:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('admin:index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')



class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'  # Plantilla personalizada

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'  # Plantilla personalizada

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'  # Plantilla personalizada

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'  # Plantilla personalizada


class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  # Permitir acceso a todos
    permission_classes = [AllowAny]

class ServicioMunicipalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ServicioMunicipal.objects.all()
    serializer_class = ServicioMunicipalSerializer
    permission_classes = [AllowAny]

class EventoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [AllowAny]

class AlertaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer
    permission_classes = [AllowAny]

class PagoServicioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PagoServicio.objects.all()
    serializer_class = PagoServicioSerializer
    permission_classes = [AllowAny]

class ComunicadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comunicado.objects.all()
    serializer_class = ComunicadoSerializer
    permission_classes = [AllowAny]

class ContactoEmergenciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactoEmergencia.objects.all()
    serializer_class = ContactoEmergenciaSerializer
    permission_classes = [AllowAny]

class BarrioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [AllowAny]

class TipoBasuraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TipoBasura.objects.all()
    serializer_class = TipoBasuraSerializer
    permission_classes = [AllowAny]

class BasuraViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Basura.objects.all()
    serializer_class = BasuraSerializer
    permission_classes = [AllowAny]