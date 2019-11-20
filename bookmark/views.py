#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
#from django.urls import reverse

from django.views import generic
from bookmark.models import Bookmark
#from django.http import HttpResponse

# Create your views here.
class BookmarkLV(generic.ListView):
    model = Bookmark
    #template_name = 'polls/index.html'
    #context_object_name = 'latest_question_list'
    #언급없으면   1.템플릿: Bookmark_list.html    2.컨택스트 변수 object_list
    
    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Bookmark.objects.order_by('-title')[:5]


class BookmarkDV(generic.DetailView):#bookmark_id 는 url에서 넘어옴(매개변수로 언급 안해도 됨, 아래에서 변수 사용 안해도 됨.)
    model = Bookmark

       #언급없으면   1.템플릿: Bookmark_detail.html    2.컨택스트 변수 object_list