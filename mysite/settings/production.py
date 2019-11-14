# 실서버 설정
from mysite.util import get_server_info_value # SECRET_KEY, DATABASES 설정(server_info.json) 불러오기
from .base import *

# WSGI application
WSGI_APPLICATION = 'mysite.wsgi.production.application'

DEBUG = False

ALLOWED_HOSTS = ['piaoxm.pythonanywhere.com']

# SECRET_KEY, DATABASES 설정(server_info.json) 불러오기-------------
SETTING_PRD_DIC = get_server_info_value("production")

SECRET_KEY = SETTING_PRD_DIC["SECRET_KEY"]

DATABASES = {
    'default': SETTING_PRD_DIC['DATABASES']["default"]
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'name',
#         'USER': 'user',
#         'PASSWORD': 'password'
#     }
# }