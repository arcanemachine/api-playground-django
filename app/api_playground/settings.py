import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://localhost:8010']

SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')
if SECRET_KEY == 'your-secret-key':
    print("""Using the default SECRET_KEY...""")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local
    'api.apps.ApiConfig',
    'users.apps.UsersConfig',
    # third-party
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_playground.urls'

TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'api_playground.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

auth_pv_prefix = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{auth_pv_prefix}.UserAttributeSimilarityValidator'},
    {'NAME': f'{auth_pv_prefix}.MinimumLengthValidator'},
    {'NAME': f'{auth_pv_prefix}.CommonPasswordValidator'},
    {'NAME': f'{auth_pv_prefix}.NumericPasswordValidator'}]

# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Canada/Mountain'
USE_I18N = True
USE_TZ = True

# static
STATIC_URL = '/staticfiles/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# misc
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# THIRD-PARTY APPS #

# django-cors-headers / corsheaders
CORS_ALLOW_HEADERS =\
    ['hx-current-url', 'hx-request', 'hx-target', 'hx-trigger', 'x-csrftoken']
# CORS_ALLOWED_ORIGINS = ['http://localhost:8010']
CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True

# djangorestframework / rest_framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}
