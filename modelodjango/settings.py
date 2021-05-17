"""
Django settings for modelodjango project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from functools import partial
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from decouple import config, Csv
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

AUTH_USER_MODEL = 'base.User'  # "qual é a app onde o modelo se encontra"<ponto>"o modelo"
# AUTH_USER_MODEL = '<app>.<Model>'
# é necessario essa variavel pois nao estamos utilizado o usuario padrão do django. Por isso precisamos informar qual
# será a classe base usada como usuario


# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'collectfast',
    'django.contrib.staticfiles',
    'modelodjango.base',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'modelodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'modelodjango.wsgi.application'
# Configuração Django Debug Toolbar
INTERNAL_IPS = config('INTERNAL_IPS', cast=Csv(), default='127.0.0.1')
if DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# ------------------------

default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

# partial server para criar uma nova chamada de função personalizada(com alguns parametros preselecionados)
# no caso estamos criando uma chamada da função parse, com o parametro 'conexão maxima 600'.  Dessa forma, será
# necessario passar apenas o primeiro parametro, que é a URL.

parse_database = partial(dj_database_url.parse, conn_max_age=600)
# abaixo, esta buscando o valor da variavel de ambiente 'DATABASE_URL', se nao encontrar pega o "default"(que aponta
# para o arquivo db.sqlite3, na raiz do projeto), mas em tod0 caso vai passar o valor obtido para a função do parametro
# "cast", que é um "partial" de dj_database_url.parse, que irá retornar uma serie de valores, que são:
# {'NAME': '/home/phsw/PycharmProjects/estudo-django/db.sqlite3', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '',
#  'CONN_MAX_AGE': 600, 'ENGINE': 'django.db.backends.sqlite3'}

DATABASES = {
    'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
}
# -----------------------/codigo antigo E codigo antigo(da aula pytho pro Endereço de Banco de Dados)

#     #django 3.2.2
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
#     #django do curso python pro
# default_db_url = os.path.join(BASE_DIR, 'db.sqlite3')
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': default_db_url,
#     }
# }
# ---------------


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# configuração de ambiete de desenvolvimento
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # na pasta 'staticfiles' no diretorio root(BASE_DIR)
# configurar pasta de upload de arquivos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

CONNECTFAST_ENABLED = False
# storage configuration in S3 AWS

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')

if AWS_ACCESS_KEY_ID:  # pragma: no cover
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }  # controle de tempo de cach do S3
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False  # nao vamos criar buckets automaticamente
    AWS_QUERYSTRING_AUTH = True  # para gerar urls assinadas.
    AWS_S3_CUSTOM_DOMAIN = None  # por q nos vamos utilizar o proprio dominio do S3
    AWS_DEFAULT_ACL = 'private'  # para que nossos arquivos do S3 nao fiquem publicos.
    CONNECTFAST_ENABLED = True
    # -----/Static assets
    # STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"  # linha original da documentação.
    COLLECTFAST_STRATEGY = "collectfast.strategies.boto3.Boto3Strategy"  # essa e a anterior sao o do collectfast
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    # classe da biblioteca que instalamos que vai fazer a gestão da pasta static pragente.
    STATIC_S3_PATH = 'static'  # path padrão dos arquivos estaticos
    STATIC_ROOT = f'/{STATIC_S3_PATH}/'  # sobrescrever o static_root da linha 158.
    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}/'
    # começa com '//' por que vai seguir o protocolo no qual ele for inserido (https, http,)
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'  # separar os arquivos staticos de admin

    # ---/Upload Media Folder
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.StaticStorage'
    # classe dessa biblioteca que vai fazer a gestão de upload de arquivos
    DEFAULT_S3_PATH = 'media'  # path padrão dos arquivos estaticos
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}/'  # sobrescrever o static_root da linha 158.
    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}/'
    # começa com '//' por que vai seguir o protocolo no qual ele for inserido (https, http,)
    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')  # adicionar essas libs apenas se estiver com AWS configurado.
