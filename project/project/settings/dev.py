from .base import *

DEV_DATABASES = {
    'default': {
        'NAME': "default_db_for_carservice",
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
    },
    'second': {
        'NAME': "second_db_for_carservice",
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
    },
}
DATABASES.update(DEV_DATABASES)

ADMINS.append(("Константин", EMAIL_HOST_USER))

DEBUG = False

ALLOWED_HOSTS.append("192.168.1.65")
