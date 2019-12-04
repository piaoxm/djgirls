"""
공통 settings
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
"""

import os
#import member.forms

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '123456789'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True  # 배포시 수정할 것

# 배포시 수정할 것
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

#로그인관련 Redirect
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = '/'  # 로그인후 자동으로 갈 경로
ACCOUNT_AUTHENTICATED_LOGOUT_REDIRECTS = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',

    'django.contrib.sites',  # 소셜 로그인

    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'debug_toolbar',  # Debug_Toolbar
    'rest_framework',

    'blog',
    'bookmark',
    'poll',
    'todoapi',
    'todo',

    'testapp',
    'member',

    # allauth 앱 : 소셜 로그인
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # 소셜 로그인 provider 구글, 페이스북, 카톡, 깃헙
    'allauth.socialaccount.providers.google',
]


MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',  # Debug_Toolbar
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS는 Django 템플릿을 로드 할 때 검사 할 파일 시스템 디렉토리 목록입니다. 바로 검색 경로입니다.
        'DIRS': [os.path.join(BASE_DIR, 'mysite', 'templates')], # 파일시스템 템플릿 로더(File system Template Loader)
        #프로젝트 디렉토리 (manage.py를 포함하고있는)에 templates 디렉토리를 만들어 쓰는 경우.
        # 'DIRS': [] 라면 APP_DIRS 설정이 True로 설정되어 있기 때문에 Django는 각 어플리케이션(admin도 어플리케이션) 패키지 내에서 templates/ 서브 디렉토리를 자동으로 찾아서 대체
        # true : 각 INSTALLED_APPS 디렉토리의 "templates" 하위 디렉토리를 탐색함.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [  # View에서 Template으로 넘어갈때 항상 실행하는 것. View에서 매번 넘겨주지 않아도 자동 실행하여 넘겨주도록 함.
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'#'ko-kr'
#관리자 화면을 한국어로 변경하길 원할 경우 # 장고의 언어를 한글'ko-kr'로 변경   / 디폴트 영어 'en-us'
TIME_ZONE = 'Asia/Seoul'  # 한국 시간 'Asia/Seoul' 으로 변경 검토 / 디폴트 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# runserver는 STATIC_URL과 STATICFILES_DIRS를 통해 정적 파일을 탐색한다.
# 각 앱단위 static 파일에 대한 URL Prefix / 템플릿 태그 {% static “경로” %} 에 의해서 참조되는 설정
STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),] # 프로젝트 단위 (File System Loader 에의해 참조되는 경로)
STATICFILES_DIRS = [os.path.join(
    BASE_DIR, 'mysite', 'static'), ]  # 프로젝트폴더 내에 위치할 경우
# collectstatic 명령을 실행시 STATIC_ROOT에 등록된 디렉토리에 복사된다
STATIC_ROOT = os.path.join(BASE_DIR, '.static_root')

# 첨부파일 등을 위한 세팅 추가!
MEDIA_URL = '/media/'  # 항상 / 로 끝나도록 설정
# 업로드된 파일을 저장할 디렉토리 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

#Debug_Toolbar 실행은 localhost 에서만
# INTERNAL_IPS = ['127.0.0.1', ]


# 소셜 로그인
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1 # 소셜 로그인 # admin앱에서 sites 모델의 사용할 도메인 id값
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'#- SMTP 메일서버 세팅이 안되어 있기 때문에 에러가 나는데 이를 임시방편으로 해결하기 위해 아래의 코드를 추가해 주는 것이다.- 실제 이를 구현하고 싶다면 구글의 Gmail 또는 AWS을 이용해서 smtp 서버를 설정해주면 된다.

# 소셜 로그인 - Google
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile', #필수
            'email',# 선택사항 optionally email scope depending on whether or not SOCIALACCOUNT_QUERY_EMAIL is enabled.
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# 소셜 로그인 allauth 추가 설정
ACCOUNT_AUTHENTICATION_METHOD = 'email' #로그인 인증 방법으로 username, email, username_email을 지정할 수 있다
ACCOUNT_EMAIL_REQUIRED = True #회원가입할 때 이메일 주소 입력 필수
ACCOUNT_USERNAME_REQUIRED = False# 회원 가입할 때 username 입력 필수 여부이다. 디폴트 값은 True이므로 반드시 ACCOUNT_AUTHENTICATION_METHOD를 통해 이메일로 로그인으로 설정하더라도 username을 입력해야 가입된다.
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None#커스텀 사용자 모델을 사용하는 경우 아이디 필드의 이름이 username이 아닌 다른 이름일 경우 지정한다. 만약 None으로 지정할 경우 allauth에서 username과 관련된 모든 기능을 사용하지 않는다. 이 경우 ACCOUNT_USERNAME_REQUIRED 값 또한 반드시 False로 지정해야 한다.
ACCOUNT_EMAIL_VERIFICATION = 'optional' #메일 유효성 인증이 필요한지 여부이다. 'mandatory', 'optional', 'none' 값을 지정할 수 있으며 'mandatory'는 회원가입 후 이메일 주소를 인증하지 않으면 회원가입하더라도 로그인할 수 없다. 'optional'은 인증 이메일은 발송되지만 인증하지 않아도 로그인할 수 있고 'none'은 인증 메일을 보내지도 않고 로그인할 수 있다.
#ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
#ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
SOCIALACCOUNT_AUTO_SIGNUP = False #디폴트 값은 True이며 SNS 공급자에서 넘겨받은 정보를 가지고 바로 회원가입시킨다. 부가정보를 입력 받기 위해 False로 설정할 수 있다.
ACCOUNT_SIGNUP_FORM_CLASS = 'member.forms.SignupForm' #회원가입 폼 클래스를 지정

############## Rest Framework #################
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASSES' : ('rest_framework.pagination.PageNumberPagination',),# Pagination을 적용
#     # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',# Request GET https://localhost:8000/api/post/?limit=2&offset=3
#     'PAGE_SIZE': 3,# Pagination을 적용
# }
