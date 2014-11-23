"""
Django settings for wsc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2!16c2ar37@tk9m3bg@d3u__(i)i$nntyfbx*slllf+p2m@=$x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.eyuanonline.com',
]

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',#'django.db.backends.postgresql_psycopg2','django.db.backends.sqlite3','django.db.backends.oracle'
        'NAME': 'note',#'wsc',
        'USER': 'root',
        'PASSWORD': '1234567890',
        'HOST': '127.0.0.1',
        # 'PASSWORD': 'honest1101',
        # 'HOST': '192.168.8.65',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-CN' #'en-us'

TIME_ZONE = 'Asia/Shanghai'#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False#True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/site_media/'
STATIC_UPLOAD = os.path.join(BASE_DIR, 'upload')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS=(
    #os.path.join(BASE_DIR,'static'),
#    os.path.join(BASE_DIR,'upload'),
#    )

TEMPLATE_DIRS = (  
    os.path.join(os.path.dirname(__file__), '../templates'),
)

# LOGGING = {
#     'version':1,
#     'disable_existing_loggers':False,
#     'formatters':{
#         'verbose':{
#             'format':'%(asctime)s %(levelname)-8s module:%(name)s %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters':{
#     },
#     'handlers':{
#         'handler_console':{
#             'level':'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#         },
#         'handler_file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR,'debug.log'),
#             'formatter': 'verbose',
#         },
#     },
#     'loggers':{
#         'wsc':{
#             'handlers':['handler_console'],
#             'level':'INFO',
#         },
#         'django_gearman_commands':{
#             'handlers': ['handler_console'],
#             'level': 'INFO',
#         },
#     },
# }
