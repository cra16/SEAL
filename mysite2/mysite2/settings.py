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
SESSION_COOKIE_AGE =10800
SESSION_SAVE_EVERY_REQUEST = True
CSRF_COOKIE_AGE = 10800

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
    'login',
    'index',
    'lecture',
    'schedule',
    'course',
    'notice',
    'qna',
    'mycourse',
    'functionhelper',
    'databasehelper',
    'dbbackup', # django-dbbackup
    'django_mobile'
    

)
AUTH_USER_MODEL = 'auth.User'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
   
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',

)

ROOT_URLCONF = 'mysite2.urls'

WSGI_APPLICATION = 'mysite2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CustomDB',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'bitnami'
      
      }
}
DATABASE_OPTIONS={
    'unix_socket' : '/tmp/mysql.sock',
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

STATIC_URL = '/static/'

STATICFILES_DIRS = (
('css', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/css'),
('js', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/js'),
('img', '/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/img'),
('html','/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/html'),
('m_html','/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/m_skins/m_html'),
('m_css','/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/m_skins/m_css'),
('m_js','/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static/m_skins/m_js')
)


TEMPLATE_DIRS = (
    ('/opt/bitnami/apps/django/django_projects/darkzero/mysite2/static'),
)

TEMPLATE_LOADERS = (
    "django_mobile.loader.Loader",
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader")

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django_mobile.context_processors.flavour")
 