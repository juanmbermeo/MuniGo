from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.shortcuts import redirect
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, ServicioMunicipal, Evento, Alerta, PagoServicio, Comunicado, ContactoEmergencia, Basura
from .serializers import UsuarioSerializer, ServicioMunicipalSerializer, EventoSerializer, AlertaSerializer, PagoServicioSerializer, ComunicadoSerializer, ContactoEmergenciaSerializer, BasuraSerializer


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


class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    def get(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            serializer = UsuarioSerializer(usuario, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            usuario.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ServicioMunicipalList(APIView):
    def get(self, request):
        servicios = ServicioMunicipal.objects.all()
        serializer = ServicioMunicipalSerializer(servicios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicioMunicipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServicioMunicipalDetail(APIView):
    def get(self, request, pk):
        try:
            servicio = ServicioMunicipal.objects.get(pk=pk)
            serializer = ServicioMunicipalSerializer(servicio)
            return Response(serializer.data)
        except ServicioMunicipal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            servicio = ServicioMunicipal.objects.get(pk=pk)
            serializer = ServicioMunicipalSerializer(servicio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ServicioMunicipal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            servicio = ServicioMunicipal.objects.get(pk=pk)
            servicio.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ServicioMunicipal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EventoList(APIView):
    def get(self, request):
        eventos = Evento.objects.all()
        serializer = EventoSerializer(eventos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventoDetail(APIView):
    def get(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
            serializer = EventoSerializer(evento)
            return Response(serializer.data)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
            serializer = EventoSerializer(evento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            evento = Evento.objects.get(pk=pk)
            evento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Evento.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AlertaList(APIView):
    def get(self, request):
        alertas = Alerta.objects.all()
        serializer = AlertaSerializer(alertas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlertaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AlertaDetail(APIView):
    def get(self, request, pk):
        try:
            alerta = Alerta.objects.get(pk=pk)
            serializer = AlertaSerializer(alerta)
            return Response(serializer.data)
        except Alerta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            alerta = Alerta.objects.get(pk=pk)
            serializer = AlertaSerializer(alerta, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Alerta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            alerta = Alerta.objects.get(pk=pk)
            alerta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Alerta.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class PagoServicioList(APIView):
    def get(self, request):
        pagos = PagoServicio.objects.all()
        serializer = PagoServicioSerializer(pagos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PagoServicioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PagoServicioDetail(APIView):
    def get(self, request, pk):
        try:
            pago = PagoServicio.objects.get(pk=pk)
            serializer = PagoServicioSerializer(pago)
            return Response(serializer.data)
        except PagoServicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            pago = PagoServicio.objects.get(pk=pk)
            serializer = PagoServicioSerializer(pago, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PagoServicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            pago = PagoServicio.objects.get(pk=pk)
            pago.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PagoServicio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ComunicadoList(APIView):
    def get(self, request):
        comunicados = Comunicado.objects.all()
        serializer = ComunicadoSerializer(comunicados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ComunicadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComunicadoDetail(APIView):
    def get(self, request, pk):
        try:
            comunicado = Comunicado.objects.get(pk=pk)
            serializer = ComunicadoSerializer(comunicado)
            return Response(serializer.data)
        except Comunicado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            comunicado = Comunicado.objects.get(pk=pk)
            serializer = ComunicadoSerializer(comunicado, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comunicado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            comunicado = Comunicado.objects.get(pk=pk)
            comunicado.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comunicado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ContactoEmergenciaList(APIView):
    def get(self, request):
        contactos = ContactoEmergencia.objects.all()
        serializer = ContactoEmergenciaSerializer(contactos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactoEmergenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContactoEmergenciaDetail(APIView):
    def get(self, request, pk):
        try:
            contacto = ContactoEmergencia.objects.get(pk=pk)
            serializer = ContactoEmergenciaSerializer(contacto)
            return Response(serializer.data)
        except ContactoEmergencia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            contacto = ContactoEmergencia.objects.get(pk=pk)
            serializer = ContactoEmergenciaSerializer(contacto, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ContactoEmergencia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            contacto = ContactoEmergencia.objects.get(pk=pk)
            contacto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ContactoEmergencia.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BasuraList(APIView):
    def get(self, request):
        basuras = Basura.objects.all()
        serializer = BasuraSerializer(basuras, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BasuraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BasuraDetail(APIView):
    def get(self, request, pk):
        try:
            basura = Basura.objects.get(pk=pk)
            serializer = BasuraSerializer(basura)
            return Response(serializer.data)
        except Basura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            basura = Basura.objects.get(pk=pk)
            serializer = BasuraSerializer(basura, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Basura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            basura = Basura.objects.get(pk=pk)
            basura.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Basura.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
