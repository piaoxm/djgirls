# 요건 삭제 가능 :  from django.contrib import admin
from django.urls import path
from . import views  #앱urls를 각각 작성하면 이렇게 연결.
# 앱폴더에 urls.py파일을 두면, 요거는 필요 없어짐 : from home import views
#from bookmark.views import BookmarkDV, BookmarkLV

app_name = 'bookmark'
urlpatterns = [
    # ex: /Bookmark/
    path('', views.BookmarkLV.as_view(), name='list'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'), 
    
    # Example: /bookmark/add/
    path('add/',
         views.BookmarkCreateView.as_view(), name="add",
    ),

    # Example: /bookmark/change/
    path('change/',
         views.BookmarkChangeLV.as_view(), name="change",
    ),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/',
         views.BookmarkUpdateView.as_view(), name="update",
    ),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/',
         views.BookmarkDeleteView.as_view(), name="delete",
    ),
]
