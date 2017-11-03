"""
Django settings for ttsx project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gasa@u=0$za#4mg1$gn@+zzsz$=*p#%jub#@knlu=-qglz0$%2'

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
    'users',
    'goods',
    'cart',
    'orders',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ttsx.urls'

WSGI_APPLICATION = 'ttsx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ttsx_three',
        'HOST':'localhost',
        'PORT':3306,
        'USER':'root',
        'PASSWORD':'123456',
        # "init_command":"SET foreign_key_checks = 0;",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#new add templates config

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

STATIC_URL = '/static/'
STATICFILES_DIRS = [
	os.path.join(BASE_DIR,'static')
]

# 配置上传路径
MEDIA_ROOT = os.path.join(BASE_DIR,'static/goods')

#富文本编辑器
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    # 'theme': 'simple',
    'width': 600,
    'height': 400,
    'language': 'zh-CN',
    'theme_advanced_buttons1': 'bold, italic, underline, strikethrough, justifyleft, justifycenter, justifyright, justifyfull, styleselect, bullist, numlist, outdent, indent, undo,redo, link, unlink, image, cleanup, help, code, table, row_before, row_after, delete_row, separator, rowseparator',
    'theme_advanced_buttons2': 'col_before, col_after, delete_col, hr, removeformat, sub, sup, formatselect, fontselect, fontsizeselect, forecolor,charmap,visualaid,spacer,cut,copy,paste'
}


# 配置发送邮件
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
# 发送邮件的邮箱
EMAIL_HOST_USER = 'sh_python03@163.com'
# 在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'chr904812'
# 收件人看到的发件人
EMAIL_FROM = 'xxl<sh_python03@163.com>'
