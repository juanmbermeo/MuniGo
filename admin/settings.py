"""
Django settings for admin project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s6dzv9#(*u##26l3f5a*ixr3-6t!bx+5a(j1o+=s(9@c+6t9-i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "unfold",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]

UNFOLD = {
    "SITE_TITLE": "MuniGo",
    "SITE_HEADER": "Admin MuniGo",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    "SITE_ICON": {
        "light": lambda request: static("img/logo_munigo.jpeg"),  # light mode
        "dark": lambda request: static("img/logo_munigo.jpeg"),  # dark mode
    },
    
    "SITE_SYMBOL": "MuniGo",
    "SITE_FAVICONS": [ 
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("img/logo_munigo.jpeg"),
        },
    ],
    
    "LOGIN": {
        "image": lambda request: static("img/logo_munigo.jpeg"),
    },
       
    "STYLES": [
        lambda request: static("css/style.css"),
    ],
    
    "COLORS": {
    "font": {
        "subtle-light": "120 143 115",  # Verde suave para modo claro
        "subtle-dark": "168 196 155",   # Verde suave para modo oscuro
        "default-light": "50 102 50",   # Verde oscuro para texto principal en modo claro
        "default-dark": "200 230 200",  # Verde claro para texto principal en modo oscuro
        "important-light": "34 85 34",  # Verde más oscuro para destacar en modo claro
        "important-dark": "220 255 220",# Verde claro para destacar en modo oscuro
    },
    "primary": {
        "50": "236 253 245",   # Verde muy claro
        "100": "209 250 229",  # Verde más suave
        "200": "167 243 208",  # Verde pálido
        "300": "110 231 183",  # Verde moderado
        "400": "52 211 153",   # Verde vibrante
        "500": "16 185 129",   # Verde principal (botones, etc.)
        "600": "5 150 105",    # Verde más intenso
        "700": "4 120 87",     # Verde oscuro
        "800": "6 95 70",      # Verde muy oscuro
        "900": "6 78 59",      # Verde intenso y oscuro
        "950": "2 44 33",      # Verde muy oscuro casi negro
    },
}

}
    
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'munigo',
        'USER': 'root',
        'PASSWORD': 'rootjuan',
        'HOST': 'localhost',
        'PORT': '3307',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = '/login/'  

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
