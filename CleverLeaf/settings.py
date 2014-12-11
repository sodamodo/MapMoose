"""
Django settings for CleverLeaf project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^tg3v-#689z!kxkes3k9k@vj-^l&&jrcuf9qd!mk=m5vkzu1h%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.gis',
    'Mapski',
    'bootstrap3',
    'registration',
    'annoying',
    # 'djcelery',
    # 'celery',
    # 'mapnik',
    # 'editor',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CleverLeaf.urls'

WSGI_APPLICATION = 'CleverLeaf.wsgi.application'


# The registration Stuff is bellow.

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

ACCOUNT_ACTIVATION_DAYS = 2

REGISTRATION_AUTO_LOGIN = True

ACTIVATION_REQUIRED = False

LOGIN_REDIRECT_URL = '/main/'

LOGIN_URL = '/accounts/login/'

LOGOUT_URL = '/accounts/logout/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

REGISTRATION_OPEN = True #True means you can register, false is the opposite.



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# n

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '12345',
        # 'HOST': '10.132.176.116',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_bin')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_bin')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,  'static'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_ROOT = os.path.join(BASE_DIR,  'media')
MEDIA_URL = '/media/'




