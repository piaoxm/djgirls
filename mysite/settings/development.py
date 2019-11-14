import os

from .base import *

# WSGI application
WSGI_APPLICATION = 'mysite.wsgi.development.application'

# 개발환경용.
SECRET_KEY = '3ic4lgil4)(e1#xlo0$f2wie0!wdb5u0vfsto#wq3r2u=@(awi'

# 개발환경용
DEBUG = True  # 배포시 수정할 것. 보안상 중요   

# 개발환경용
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar',  # Debug_Toolbar
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # Debug_Toolbar
]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Debug_Toolbar 실행은 localhost 에서만
INTERNAL_IPS = ['127.0.0.1', ]
