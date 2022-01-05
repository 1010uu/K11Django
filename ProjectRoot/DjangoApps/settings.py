"""
Django settings for DjangoApps project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!t6)=i06vjkoys71n0ns(h8&x0a18=!5+3@-(kj9492=f=3j+n'

# SECURITY WARNING: don't run with debug turned on in production!
'''
디버그 모드에 대한 설정으로 True이면 테스트모드(개발용)
false이면 배포용(운영모드)
'''
DEBUG = True
#아이피를 설정. 개발용인 경우 아래와 같이 로컬호스트로 설정하면 됨
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition
'''
프로젝트 생성한 후 App을 추가하면 반드시 해당 항목에 등록해야 한다.
형식: 앱의 이름.apps.설정클래스명
(해당 앱 파일의 apps.py가면 설정 클래스명 화인 가능)

앱1 : 설문 관리 앱
앱2 : 템플릿 문법 앱
앱3 : 도서관리 앱
'''
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'livepolls.apps.LivepollsConfig',
    'tempapps.apps.TempappsConfig',
    'books.apps.BooksConfig'
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

ROOT_URLCONF = 'DjangoApps.urls'

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

WSGI_APPLICATION = 'DjangoApps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#DB는 기본적으로 설정된 sqllite3를 사용하므로 변경하지 않는다.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
#타임존 설정. 한국으로 변경
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
'''
장고 프레임워크에서는 CSS, JS, 이미지와 같은 정적 파일들은 static 폴더에
저장하도록 규정되어있다. 개발자가 임의로 images와 같은 폴더를 생성하더라도
접근할 수 없다.
'''
STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
