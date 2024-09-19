from django.urls import path
from .views import custom_login_view, custom_logout

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout, name='logout'),
]
