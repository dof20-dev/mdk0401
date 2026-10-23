import os
from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ (в реальном проекте его нужно скрывать в .env)
SECRET_KEY = 'django-insecure-ваш-секретный-ключ-для-электронного-дневника'

# Режим отладки (для учебного проекта оставляем True)
DEBUG = True

ALLOWED_HOSTS = ['*']

# Подключенные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Сторонние библиотеки
    'rest_framework',
    'drf_spectacular',
    
    # Наши приложения
    'apps.accounts',
    'apps.schedule',
    'apps.students',
    'apps.grades',
    'apps.reports',
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

# ==========================================
# НАСТРОЙКА БАЗЫ ДАННЫХ PostgreSQL
# ==========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diary_db',       # Имя базы данных, которую ты создал в pgAdmin
        'USER': 'postgres',       # Твой пользователь PostgreSQL
        'PASSWORD': '123', # <--- ОБЯЗАТЕЛЬНО ЗАМЕНИ НА СВОЙ ПАРОЛЬ ОТ pgAdmin
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Локализация и время
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Статические файлы (CSS, JS)
STATIC_URL = 'static/'

# Автоматическое поле ID
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Кастомная модель пользователя
AUTH_USER_MODEL = 'accounts.User'

# ==========================================
# НАСТРОЙКИ DJANGO REST FRAMEWORK (DRF) И SWAGGER
# ==========================================
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API Электронного дневника',
    'DESCRIPTION': 'Документация для системы учета оценок',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}