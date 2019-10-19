from django.urls import path, register_converter # 1.django\urls\converters.py 의 register_converter 함수
from .converters import FourDigitYearConverter  # 2. 사용자 정의 converter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')# 3. register_converter 함수로 사용자 정의 converter(FourDigitYearConverter)를 'yyyy'타입형으로 쓰기로함


#한글 지원되는 Slug Converter 만들기(StringConverter를 상속받아서)
from django.urls.converters import StringConverter # django\urls\converters.py 의 StringConverter 클래스

class SlugUnicodeConverter(StringConverter):
    regex = r'[-\w]+'

#참고로 - django\urls\converters.py 의 StringConverter 클래스
# class StringConverter:
#     regex = '[^/]+'

#     def to_python(self, value):
#         return value

#     def to_url(self, value):
#         return value



app_name = 'blog'

urlpatterns = [
    #path('archives/<yyyy:year>/', views.archives_year, name='archives_year'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('new/', views.post_new, name='post_new'),
    
]


