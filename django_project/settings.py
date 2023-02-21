"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-t2yib&rf5^v^jdnb=w65*qd0qx+p1j0ml-@m8jc99@i$fu(#+q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # 배포시에는 False로 변경 (에러메시지 노출 방지)

ALLOWED_HOSTS = ['pt0108.pythonanywhere.com', 'localhost']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # 맨 마지막 데이터에도 쉼표를 달아두면 좋은 점 
             # -> 다음에 추가 할 때 까먹어도 봐줌 
             # -> 추가되거나 제거된 코드 비교 할 때 보기 좋아서
    "django_extensions",

    # 게시판을 예쁘게 꾸며주기 위한 패키지
    "crispy_forms",
    "crispy_bootstrap5",
    "markdownx",

    # all-auth 패키지
     # The following apps are required:
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',
]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]



CRISPY_TEMPLATE_PACK = 'bootstrap5'

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

# LANGUAGE_CODE = "en-us"
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')  
# 변수명 중에 _붙어있는 경우 개발자만 쓸 거다 라는 뜻이라고 생각하시면 됩니다
# url 경로와 실제 파일이 저장되는 경로를 일부러 불일치시킨것 
# 해당 글에서만 저 경로의 파일을 호출할 수 있도록

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1 # 배포할 때 site 중 n번째 사이트와 연결하겠다는 의미

# ACCOUNT_EMAIL_REQUIRED = True  # 어느 필드까지 우선으로 받을 것인지
# ACCOUNT_EMAIL_VERIFICATION = 'none' # 메일 인증 필요한 경우 받을 수 있음
LOGIN_REDIRECT_URL = "/blog/"  # 로그인 후 'blog'로 이동 
# -> 이유 blog의 views.py에 login, logout, update 등의 기능 모두 구현해놓았기 때문 