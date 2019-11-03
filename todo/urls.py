from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    #path('archives/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('', views.index, name='index'),
    path('vueonly/', views.TodoVueOnlyTV.as_view(), name='vueonly'),
]


urlpatterns += [
    path('fetch/', views.todo_fetch, name='fetch'),
    path('save/', views.todo_save, name='save'),
]
