#from django.http import HttpResponseRedirect
#from django.shortcuts import get_object_or_404, render
#from django.urls import reverse

# from django.views import generic
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin #  ??????????
from django.urls import reverse_lazy
#from django.http import HttpResponse
from mysite.views import OwnerOnlyMixin  #  ??????????
from bookmark.models import Bookmark

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark
    #template_name = 'polls/index.html'
    #context_object_name = 'latest_question_list'
    #언급없으면   1.템플릿: Bookmark_list.html    2.컨택스트 변수 object_list
    
    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Bookmark.objects.order_by('-title')[:5]


class BookmarkDV(DetailView):#bookmark_id 는 url에서 넘어옴(매개변수로 언급 안해도 됨, 아래에서 변수 사용 안해도 됨.)
    model = Bookmark

       #언급없으면   1.템플릿: Bookmark_detail.html    2.컨택스트 변수 object_list


class BookmarkCreateView(LoginRequiredMixin, CreateView): 
    model = Bookmark 
    fields = ['title', 'url'] 
    success_url = reverse_lazy('bookmark:list') 

    def form_valid(self, form): 
        form.instance.owner = self.request.user 
        return super().form_valid(form) 


class BookmarkChangeLV(LoginRequiredMixin, ListView): 
    template_name = 'bookmark/bookmark_change_list.html' 

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView): 
    model = Bookmark 
    fields = ['title', 'url'] 
    success_url = reverse_lazy('bookmark:list') 


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView): 
    model = Bookmark 
    success_url = reverse_lazy('bookmark:list')

