import os
from pathlib import Path
import dj_database_url

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète pour le développement (ne jamais l'exposer en production)
SECRET_KEY = 'django-insecure-votre-cle-secrete-ici'

# Mode développement
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',  # Ton application
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Fichier urls principal
ROOT_URLCONF = 'portfolio_fadil.urls'

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'portfolio' / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'portfolio_fadil.wsgi.application'

# Gestion des mots de passe
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

# Langue et fuseau horaire
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'

USE_I18N = True
USE_TZ = True

# URL des fichiers statiques
STATIC_URL = '/static/'

# Dossiers où chercher les fichiers statiques
STATICFILES_DIRS = [
    BASE_DIR / 'portfolio' / 'static',
]

# Fichiers médias (si jamais tu en ajoutes plus tard)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Clé par défaut du champ d'auto ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


X_FRAME_OPTIONS = 'ALLOWALL'
