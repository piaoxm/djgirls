# 요건 삭제 가능 :  from django.contrib import admin
from django.urls import path
from . import views  #앱urls를 각각 작성하면 이렇게 연결.

# 앱폴더에 urls.py파일을 두면, 요거는 필요 없어짐 : from home import views
#기본 세팅(home을 기본으로)
app_name = 'poll'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    #path('', views.index, name='index'), # name은 템플릿에서 {% url 'index' %}  으로 경로 연결하기위해
    
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:question_id>/', views.detail, name='detail'),
    
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/results/', views.results, name='results'),
    
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]