from .base import *

# celery redis settings
import djcelery


import djcelery
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_SEND_TASK_ERROR_EMAILS = True
djcelery.setup_loader()


# end celery settings

DEV_INSTALLED_APP = [
    'djcelery',
    'home',
    'services',
    'scan_products',
    'contacts',
    'about',
]
INSTALLED_APPS.extend(DEV_INSTALLED_APP)

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

DATABASE_ROUTERS = [
    "project.project_db_routers.DefaultRouter",
    "project.project_db_routers.DataRouter",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media/")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static/")
STATICFILES_DIRS = (
                    #os.path.join(PROJECT_ROOT, "static/"),
                    os.path.join(PROJECT_ROOT, 'home/static/'),
                    os.path.join(PROJECT_ROOT, 'services/static/'),
                    os.path.join(PROJECT_ROOT, 'scan_products/static/'),
                    os.path.join(PROJECT_ROOT, 'contacts/static/'),
                    os.path.join(PROJECT_ROOT, 'about/static/'),
                    )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "templates/base/"),
            os.path.join(PROJECT_ROOT, "templates/inherit/"),
            os.path.join(PROJECT_ROOT, "templates/"),
            os.path.join(PROJECT_ROOT, "home/templates/base/"),
            os.path.join(PROJECT_ROOT, "home/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "home/templates/"),
            os.path.join(PROJECT_ROOT, "services/templates/base/"),
            os.path.join(PROJECT_ROOT, "services/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "services/templates/"),
            os.path.join(PROJECT_ROOT, "scan_products/templates/base/"),
            os.path.join(PROJECT_ROOT, "scan_products/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "scan_products/templates/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/base/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/"),
            os.path.join(PROJECT_ROOT, "about/templates/base/"),
            os.path.join(PROJECT_ROOT, "about/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "about/templates/"),
        ],
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

EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "webmaster@rybinsk-tech.ru"
EMAIL_HOST_PASSWORD = "=IJD6v0Xvegz"
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
ADMINS.append(("Константин", EMAIL_HOST_USER))
