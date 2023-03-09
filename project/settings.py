import os
from environs import Env

env = Env()
env.read_env()


db_adress = env("DB_ADRESS")
db_password = env("DB_PASSWORD")
db_port = env("DB_PORT")
db_name = env("DB_NAME")
db_user = env("DB_USER")
secret_key = env("SECRET_KEY", "REPLACE_ME")
debug = env.bool("DEBUG", False)
allowed_hosts = env.list("ALLOWED_HOSTS", ["localhost:8000"])





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': db_adress,
        'PORT': db_port,
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = secret_key

DEBUG = debug

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = allowed_hosts


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
