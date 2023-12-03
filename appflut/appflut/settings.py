"""
Django settings for appflut project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!_=hia%yw+d$ics+^*2(v)i1$!-zk&gjy&kd0taq9zvy-hl!96'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webflut',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'appflut.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'appflut.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


LOGIN_URL = 'home'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_TRUSTED_ORIGINS = [
    'https://1bf8-178-127-218-219.ngrok-free.app',
    'https://1bf8-178-127-218-219.ngrok-free.app/register/',
    'https://1bf8-178-127-218-219.ngrok-free.app/person_info/',
    'https://1bf8-178-127-218-219.ngrok-free.app/login/',
    'https://1bf8-178-127-218-219.ngrok-free.app/logout/',
    'https://1bf8-178-127-218-219.ngrok-free.app/calories_and_bjy/',
    'https://1bf8-178-127-218-219.ngrok-free.app/profile/',
    'https://1bf8-178-127-218-219.ngrok-free.app/report/',
    'https://1bf8-178-127-218-219.ngrok-free.app/breakfast/',
    'https://1bf8-178-127-218-219.ngrok-free.app/lunch/',
    'https://1bf8-178-127-218-219.ngrok-free.app/dinner/',
    'https://1bf8-178-127-218-219.ngrok-free.app/snack/',
    'https://1bf8-178-127-218-219.ngrok-free.app/activities/',
    'https://1bf8-178-127-218-219.ngrok-free.app/eatingbase/',
    'https://1bf8-178-127-218-219.ngrok-free.app/add_breakfast/',
    'https://1bf8-178-127-218-219.ngrok-free.app/add_lunch/',
    'https://1bf8-178-127-218-219.ngrok-free.app/add_dinner/',
    'https://1bf8-178-127-218-219.ngrok-free.app/add_snack/',
    'https://1bf8-178-127-218-219.ngrok-free.app/add_activity_view/',
    'https://1bf8-178-127-218-219.ngrok-free.app/remove_from_list/<int:product_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/remove_from_list2/<int:product_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/delete_activity/<int:id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/edit_person_info/',
    'https://1bf8-178-127-218-219.ngrok-free.app/creategroup/',
    'https://1bf8-178-127-218-219.ngrok-free.app/groupdetail/<int:group_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/adduser/<int:group_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/removeuser/<int:group_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/userinfo/<int:user_id>/',
    'https://1bf8-178-127-218-219.ngrok-free.app/step1/',
    'https://1bf8-178-127-218-219.ngrok-free.app/step2/',
    'https://1bf8-178-127-218-219.ngrok-free.app/step3/',
    'https://1bf8-178-127-218-219.ngrok-free.app/step4/',
    'https://1bf8-178-127-218-219.ngrok-free.app/step5/',
    'https://1bf8-178-127-218-219.ngrok-free.app/display_chart/',

    # Другие доверенные источники (если есть)
]