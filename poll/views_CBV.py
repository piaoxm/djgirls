#from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.template import loader  #(템플릿)방법2
from django.shortcuts import (get_object_or_404,  # (템플릿)방법1(HttpResponse와 loader를 포함함)
                              render)
#from django.http import Http404
from django.urls import reverse
from django.views import generic
#
from django.utils import timezone
# Model
from .models import Choice, Question



class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
        pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
        #Question.objects.filter (pub_date__lte = timezone.now ()) 는 timezone.now 보다 pub_date 가 작거나 같은 Questions 를 포함하는 queryset을 리턴합니다.


#함수형
#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'poll/index.html', context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())#시간체크. 미래꺼는 제외
#함수형
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'poll/detail.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'
#함수형
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'poll/results.html', {'question': question})

### POST 로 넘어오는 함수
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):#만약 POST 자료에 choice 가 없으면, request.POST['choice'] 는 KeyError 가 일어납니다.
        # 현재 설문 다시 보여주기
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 성공적으로 처리 한 후에는 항상 HttpResponseRedirect 를 반환해야합니다.
        # 이 팁은 Django에만 국한되는것이 아닌 웹개발의 권장사항입니다.(두번 연속 클릭 방지!)
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
