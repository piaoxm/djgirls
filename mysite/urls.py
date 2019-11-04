"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin# 프로젝트 urls에만 있음
from django.urls import path, include # 방법1:include로 타 앱의 urls 연결

#from home import views  #방법2: 앱urls를 여기에 링크하려면 : 기본 세팅(home을 기본으로)
#from bookmark import views

# 개발환경에서의 media 파일 서빙이 지원안되어 직접 서빙 Rule 추가
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views #django.contrib.auth.views.logout 을 사용하기 위해

urlpatterns = [
    path('admin/', admin.site.urls),#보안을 위해 admin은 다른것으로 수정하여 배포
    path('accounts/', include('allauth.urls')), # 소셜 로그인 allauth앱
    #path('accounts/login/', views.login, name='login')
    #path('accounts/logout/', views.logout, name='logout', kwargs={'next_page': '/'}),
    path('blog/', include('blog.urls')),# 방법1 # include 로 각 앱(home)의 urls를 읽어옴
    path('todo/', include('todo.urls')),
    path('testapp/', include('testapp.urls')),
    #path('', views.index),   #방법2 # home앱은 위에 등록하였으므로 생략. home앱의 view로 연결해줌
]

# media #개발환경이 아닌경우 빈리스트가 반환됨. 즉 개발환경시에만 media 파일 서빙되도록 함
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# debug_toolbar 추가
from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

