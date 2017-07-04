import os

# celery redis settings

import djcelery
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_SEND_TASK_ERROR_EMAILS = True
djcelery.setup_loader()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = "/".join(BASE_DIR.split("/")[:-1])
_PATH = os.path.abspath(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mbaf8)#^&8k*6&q*s$05@djrez0$f-beas6ih!iw_k5vna2tp('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'home',
    'services',
    'parse',
    'contacts',
    'about',
    'errors',
    'mytemplatetags',
    'sendsms',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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
            os.path.join(PROJECT_ROOT, "parse/templates/base/"),
            os.path.join(PROJECT_ROOT, "parse/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "parse/templates/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/base/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "contacts/templates/"),
            os.path.join(PROJECT_ROOT, "about/templates/base/"),
            os.path.join(PROJECT_ROOT, "about/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "about/templates/"),
            os.path.join(PROJECT_ROOT, "errors/templates/base/"),
            os.path.join(PROJECT_ROOT, "errors/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "errors/templates/"),
            os.path.join(PROJECT_ROOT, "mytemplatetags/templates/base/"),
            os.path.join(PROJECT_ROOT, "mytemplatetags/templates/inherit/"),
            os.path.join(PROJECT_ROOT, "mytemplatetags/templates/"),
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


WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases


DATABASES = {
}

DATABASE_ROUTERS = [
    "project.project_db_routers.DefaultRouter",
    "project.project_db_routers.DataRouter",
]

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru_RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False

#email settings
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "webmaster@rybinsk-tech.ru"
EMAIL_HOST_PASSWORD = "=IJD6v0Xvegz"
EMAIL_USE_TLS = True
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

#media and static settings
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "media/")

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(PROJECT_ROOT, "static/")
STATICFILES_DIRS = (
                    os.path.join(PROJECT_ROOT, "static/"),
                    os.path.join(PROJECT_ROOT, 'home/static/'),
                    os.path.join(PROJECT_ROOT, 'services/static/'),
                    os.path.join(PROJECT_ROOT, 'parse/static/'),
                    os.path.join(PROJECT_ROOT, 'contacts/static/'),
                    os.path.join(PROJECT_ROOT, 'about/static/'),
                    os.path.join(PROJECT_ROOT, 'errors/static/'),
                    os.path.join(PROJECT_ROOT, 'mytemplatetags/static/'),
                    )
