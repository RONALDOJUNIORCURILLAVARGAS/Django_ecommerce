import os
import environ

env = environ.Env()

# Leer el archivo .env
environ.Env.read_env()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'core',
    'cart',
]
DEFAULT_FROM_EMAIL=env('DEFAULT_FROM_EMAIL')
NOTIFY_EMAIL=env('NOTIFY_EMAIL')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

CRISPY_TEMPLATE_PACK='bootstrap4'
# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]
STATIC_ROOT= os.path.join(BASE_DIR,"static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,"media")

PAYPAL_CLIENT_ID=env('PAYPAL_SANDBOX_CLIENT_ID')
PAYPAL_SECRET_KEY=env('PAYPAL_SANDBOX_SECRET_KEY')

if DEBUG is False:
    #SEGURIDAD DE LA PAGINA
    SESSION_COOKIE_SECURE=True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF=True
    SECURE_HSTS_INCLUDE_SUBDOMAINS=True
    SECURE_HSTS_SECONDS=31536000
    SECURE_REDIRECT_EXEMPT=[]
    SECURE_SSL_REDIRECT=True
    SECURE_PROXY_SSL_HEADER=('HTTP_X_XFORWARDED_PROTO','https')
    #-----------------------------------------------------------
    ALLOWED_HOSTS=['https://datadosis.com']

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    DATABASES ={
        'default':{
            'ENGINE':'django.db.backend.postgresql_psycopg2',
            'NAME':'',
            'USER':'',
            'PASSWORD':'',
            'HOST':'',
            'PORT':'',

        }
    }
    PAYPAL_CLIENT_ID=env('PAYPAL_LIVE_CLIENT_ID')
    PAYPAL_SECRET_KEY=env('PAYPAL_LIVE_SECRET_KEY')