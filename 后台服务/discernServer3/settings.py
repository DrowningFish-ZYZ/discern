import os.path
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&_0glo_i8=_!t!mp0kh%0=pta#c#s8k=n!fkb*3!rvutybgkyz'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'discernServer3.urls'
WSGI_APPLICATION = 'discernServer3.wsgi.application'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 自定义配置
MY_USER_UPLOAD_PATH = os.path.join(BASE_DIR, 'static\\user')
MY_DISCERN_UPLOAD_PATH = os.path.join(BASE_DIR, 'static\\discern')
YOLO_DIR = os.path.join(BASE_DIR, 'yolo')
LOGIN_URL = '/api/1/admin/login/'

# Application definition
INSTALLED_APPS = [
    # 'django.contrib.admin',  # 后台管理【不需要】
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # 跨域
    'rest_framework',

    'api1'
]

# 中间件【拦截器】
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 跨域配置
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'discern3',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 静态文件配置 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 跨域配置
# 中间件设置【白名单设置】
# CORS_ORIGIN_WHITELIST = (
#     'http://127.0.0.1:8080',
#     'http://localhost:8080',
#     'http://172.20.10.12:8080',
#     'http://172.20.10.2:8080',
# )
CORS_ORIGIN_ALLOW_ALL = True  # 取消白名单限制
# 允许携带 cookie
CORS_ALLOW_CREDENTIALS = True
# 前端headers携带token允许进入
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'Referer',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-token',
    'token'
)

# DRF 配置
# 注意: 如果你在 APIView 中配置局部认证，那么全局认证便会被覆盖
REST_FRAMEWORK = {
    # 用户认证方式【全局配置】
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',  # 基本认证
        'rest_framework.authentication.SessionAuthentication',  # session 认证
        'api1.utils.jwt.JWTUserAuthentication',  # JWT 用户认证
    ],
    # 权限认证方式【全局配置】
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # 任意用户
    ],
    # 限流配置【全局】
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.ScopedRateThrottle',  # 自定义限流
    ],
    'DEFAULT_THROTTLE_RATES': {
        'discern': '1/minute',  # 识别图片【每分钟一次】
        'download': '1/minute',  # 下载数据【每分钟一次】
        'upload': '1/minute'
    }
}

# JWT 用户认证配置
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),  # JWT 有效期
}
