from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('', views.home, name = "index"),
]


