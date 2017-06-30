from .base import *

DEV_DATABASES = {
    'default': {
        'NAME': "default_db",
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'pinachet',
        'PASSWORD': 'balonka2015',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
    },
    'second': {
        'NAME': "second_db",
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'pinachet',
        'PASSWORD': 'balonka2015',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'CONN_MAX_AGE': 0,
    },
}

DATABASES.update(DEV_DATABASES)

ADMINS.append(("Константин", EMAIL_HOST_USER))

DEBUG = False

ADMINS.append(("Константин", EMAIL_HOST_USER))
ALLOWED_HOSTS.append("xn----8sbbgarrfm3apqjhfek7m.xn--p1ai")
