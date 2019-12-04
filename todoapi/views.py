# from django.shortcuts import render
from rest_framework import generics
# from rest_framework.pagination import PageNumberPagination
#from rest_framework.decorators import api_view
# from django.views.generic import TemplateView
# from django.http import JsonResponse
from .models import Todoapi
from .serializers import TodoSerializer

# class TodoListView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer #serializer_class : 요청의 검증작업이 필요할 때, 그리고 요청받은 데이터를 serializer화 시킬 때 사용한다.
#     pagination_class = PageNumberPagination
#     # filter_backends = (SearchFilter, OrderingFilter)# 쿼리셋을 필터링하는데 사용한다. 검색이나 정렬, 필터링을 적용시킬 때 사용한다.
#     search_fields = ('title','content',)
    

# CreateAPIView (생성) : POST 메서드 핸들러를 제공한다. 요청에 대한 응답은 성공시 201 Created와 함께 serialized representation, 실패시 400 Bad Request
# class TodoCreateView(generics.CreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# get 메서드 핸들러를 제공한다. 쿼리셋을 반환할 때 사용한다. 쿼리셋의 serialized representation과 함께 200 OK의 응답을 반환한다.
# class TodoListView(generics.ListAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     pagination_class = PageNumberPagination

#ListCreateAPIView (생성 + 읽기)
#get, POST 메서드 핸들러를 제공한다. get요청과 POST 요청을 받을 수 있다. ListAPIView, CreateAPIView를 합친 것이다.
class TodoView(generics.ListCreateAPIView):
    queryset = Todoapi.objects.all()
    serializer_class = TodoSerializer #serializer_class : 요청의 검증작업이 필요할 때, 그리고 요청받은 데이터를 serializer화 시킬 때 사용한다.
    # pagination_class = PageNumberPagination
    # filter_backends = (SearchFilter, OrderingFilter)# 쿼리셋을 필터링하는데 사용한다. 검색이나 정렬, 필터링을 적용시킬 때 사용한다.
    search_fields = ('title','content',)

# class TodoDetailView(generics.RetrieveAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     # lookup_field = 'title'# 기본 값은 'pk', 검색, 수정, 삭제 등 하나의 객체에 접근할 때 사용. urls에 동일하게 반영해야함.
#                             # urls.py에서 기본적으로는 pk로 상세페이지를 불러온다. pk외에 다른 매개변수를 사용하고 싶을 때는 이렇게 함.
#     #title이 중복되는 경우 500 서버에러를 발생시키므로 반드시 매개변수는 unique한 값이어야 한다.

# # DestroyAPIView (삭제)
# # delete 메서드 핸들러를 제공한다. 객체를 삭제하면 204 No Content를, 객체가 존재하지 않을 경우 404 Not Found의 응답을 반환한다. 하나의 객체를 삭제하므로 매개변수는 unique한 값이어야 한다.
# class TodoDeleteView(generics.DestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# #UpdateAPIView
# # put, patch 메서드 핸들러를 제공한다. 하나의 객체를 수정할 때 사용한다. 업데이트 완료시 200 OK와 함께 serialized representiation의 응답을 반환하지만 데이터가 invalid 한경우 400 Bad Request를 반환한다. 역시, 매개변수는 unique한 값이어야한다.
# class TodoUpdateView(generics.UpdateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# RetrieveUpdateAPIView
# get, put, patch 메서드 핸들러를 제공한다. 하나의 객체에서 사용되는 것이므로 매개변수는 unique 값이어 한다. 상세페이지 검색과 수정을 하고자할 때 사용한다.

# RetrieveDestroyAPIView
# get, delete 메서드 핸들러를 제공한다. 하나의 객체에서 사용되는 것이므로 매개변수는 unique 값이어야 한다. 상세페이지 검색과 삭제를 하고자할 때 사용한다.

# RetrieveUpdateDestroyAPIView
# get, put, patch, delete 메서드 핸들러를 제공한다. 하나의 객체에서 사용되는 것이므로 매개변수는 unique 값이어야 한다. 상세페이지 검색, 삭제, 수정을 하고자할 때 사용한다
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todoapi.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'title'