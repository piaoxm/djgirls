from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'todoapi'

urlpatterns = [
    path('', views.TodoView.as_view(), name='index'),
    path('<int:pk>/',views.TodoDetailView.as_view(), name='detail'),
    # path('<title>',views.TodoDetailView.as_view()),# lookup_field = 'title'로 받기. 기본적으로는 위처럼 pk로 상세페이지를 불러온다. pk외에 다른 매개변수를 사용하고 싶을 때는 이렇게 함.
    # path('<int:pk>/',views.TodoDeleteView.as_view()),
    # path('<int:pk>/',views.TodoUpdateView.as_view()),



    # path('vueonly/', views.TodoVueOnlyTV.as_view(), name='vueonly'),
]


# urlpatterns += [
#     path('fetch/', views.todo_fetch, name='fetch'),
#     path('save/', views.todo_save, name='save'),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
