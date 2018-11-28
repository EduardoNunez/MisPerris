"""
Django settings for misPerris project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dfi@44a3-l#f2%3-x2p04246n)^5o#62+&j&&p$kr2i4xt#sb%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# Le decimos a django donde se redigirá el usuario cuando haya iniciado sesión
# correctamente.

LOGIN_REDIRECT_URL = "/"

# Le decimos a django donde se redigirá el usuario cuando haya cerrado su sesión.

LOGOUT_REDIRECT_URL = "/accounts/login"

# Application definition
SOCIAL_AUTH_FACEBOOK_KEY = '305278046739444' #App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '02182ae3f0cca73cd0c36fa196646860' #App SECRET

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',	
    'accounts',
    'social_django',
    'crispy_forms', # Cargaremos el plugin en nuestro proyecto
    'api',
    'pwa',
    'fcm_django',
]


# Ahora le decimos al plugin crispy con que libreria el trabajará
CRISPY_TEMPLATE_PACL = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'misPerris.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ]
        },
    },
]

FCM_DJANGO_SETTINGS = {
        "FCM_SERVER_KEY": "AAAAg7irfRw:APA91bG3KHvF-fP6NFUB5ZZS5WPqv7SzabTXpXmkPHwVt7tvWnxdJwvBZE7IUo-Ve-0C2ihWXqIkwa7mlcsAmS4HnqnqGELVoTpYVRg8eVR-I5H2LPeCRfEbsg8hQd1qXX2m0pclI1JE",
         # true if you want to have only one active device per registered user at a time
         # default: False
        "ONE_DEVICE_PER_USER": False,
         # devices to which notifications cannot be sent,
         # are deleted upon receiving error response from FCM
         # default: False
        "DELETE_INACTIVE_DEVICES": False,
}

WSGI_APPLICATION = 'misPerris.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

####Lo que digo que va 
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home2/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',

)

SOCIAL_AUTH_LOGIN_ERROR_URL = '/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# Le diremos a django donde queda nuestro serviceworker.
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'serviceworker.js')

PWA_APP_NAME = "Mis Perris"

PWA_APP_ICONS = [

    {
        'src':'/static/core/img/mascota_logo.png',
        'sizes':'160x160',
    }

]