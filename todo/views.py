from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Todo

def index(request):
    return render(request, 'todo/list.html')

# 저장 된 모든 할 일 데이터를 불러온 후에 하나씩 json 데이터로 가공할 수 있게 사전형 데이터로 저장
# 마지막으로 JsonResponse 형태로 데이터를 반환하면 Vue.js앱에서 데이터를 받아서 보여주게된다.
def todo_fetch(request): # 목록 불러오기
    todos = Todo.objects.all()
    print(todos)
    todo_list = []
    for index, todo in enumerate(todos, start=1): # eumerate는 반복문 사용 시 몇 번째 반복문인지 돌려준다.
        todo_list.append({'id':index,'title':todo.title,'completed':todo.completed})

    return JsonResponse(todo_list, safe=False)

#######################################
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import TodoForm

#save/ 로 접근하면 비어있는 사전형 데이터 하나만 나온다. todo_save 뷰는 POST 메서드로 데이터를 전송해야만 제대로 기능을 하기 때문입니다.
# @csrf_exempt
# def todo_save(request): #할 일 목록 전체 데이털르 받아서 그대로 저장하는 역할을 한다.
#     if request.body:
#         data = json.loads(request.body)
#         if 'todos' in data: #3 그런데 뷰를 호출 할 때 마다 데이터 확인 없이 데이터를 지우게되면 문제가 발생함으로 확인
#             todos = data['todos']
#             Todo.objects.all().delete() #2 전체 데이터를 지우고 다시 입력하는 방식 사용
#             for todo in todos:
#                 print('todo', todo)
#                 form = TodoForm(todo) # 데이터를 저장
#                 if form.is_valid():
#                     form.save() # DB에 저장
#     return JsonResponse({})

#이런 비어있는 뷰를 보여주기 싫고 POST 멧더르르 사용했을 때만 뷰가 동작하도록 하고 싶다면 데코레이터를 이용해서 제약 조건을 만들 수 있습니다.

@csrf_exempt
@require_POST # POST 메서드로 접근했을 때만 동작
def todo_save(request):
    if request.body:
        data = json.loads(request.body)
        if 'todos' in data:
            todos = data['todos']
            Todo.objects.all().delete()
            for todo in todos:
                form = TodoForm(todo)
                if form.is_valid():
                    form.save()
                    
    return JsonResponse({})




class TodoVueOnlyTV(TemplateView):
    template_name = 'todo/todo_vue_only.html'


# class TodoMOMCV(MultipleObjectMixin, CreateView):
#     model = Todo # model은 Todo로 지정한다.
#     fields = '__all__' # Todo model의 모든 필드를 가져와라
#     template_name = 'todo/todo_form_list.html'
#     success_url = reverse_lazy('todo:mixin') 

#     def get(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset() # DB에서 레코드들을 꺼내오는 메소드get_queryset()
#         # get_queryset() 메소드는 어느쪽에 있는 것을 호출할까? (MultipleObjectMixin, CreateView)
#         # 이럴 때 순서가 중요하다, 앞에 있는 클래스를 먼저 봐서 이 클래스에 get_queryset 메소드가
#         # 있다면 그걸 호출하고, 거기에 없으면 CreateView에서 찾아서 get_queryset() 메소드를 호출
#         # 둘 다 get_queryset() 메소드가 있기 때문에 MultipleObjectMixin 에 있는 것이 호출된다.
#         return super().get(request, *args, **kwargs)
#         # 상위 클래스(TodoMOMCV)의 get 메소드를 그대로 호출하게 되면, CreateView클래스의
#         # get_context_data 메소드가 호출되고, 이 메소드에서 object_list라는 context변수가
#         # 템플릿에 넘어가게 되는 것이다.
#         # 그리고 상위 클래스의 메소드를 오버라이딩 할 때는 인자는 동일하게 써줘야 한다.

#     def post(self, request, *args, **kwargs):
#         self.object_list = self.get_queryset()
#         return super().post(request, *args, **kwargs) # 인자는 동일하게


# class TodoDelV2(DeleteView):
#     model = Todo
#     # template_name = 'todo/todo_confirm_delete.html' # form 을 보여주는 과정생략
#     success_url = reverse_lazy('todo:mixin')

#     def get(self, request, *args, **kwargs): # get 요청이 왔을 때
#         return self.delete(request, *args, **kwargs) # 바로 삭제를 진행해라