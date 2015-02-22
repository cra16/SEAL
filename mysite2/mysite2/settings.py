"""
Django settings for mysite2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SESSION_EXPIRE_AT_BROWSER_CLOSE =True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(5x0pq$7_%f(m4+8hw38ad37+$-c#3^uikh$04!m-1l7t=53t$'

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
    'blog',
    'login',
    'index',
    'lecture',
    'schedule',
    'course',
    'notice',
    'qna',
    'mycourse',


)
#AUTH_USER_MODEL = 'CustomUser.User'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
   
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite2.urls'

WSGI_APPLICATION = 'mysite2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CustomDB',
        'HOST': '/opt/bitnami/mysql/tmp/mysql.sock',                                                 
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'bitnami'
      }
}

TIME_ZONE = 'Asia/Seoul'
LANGUAGE_CODE = 'ko-kr'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/




STATIC_ROOT = '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static'

STATIC_URL = '/mysite2/static/'

STATICFILES_DIRS = (
('css', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/css'),
('js', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/js'),
('img', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/img'),
)


TEMPLATE_DIRS = ('/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/html')
