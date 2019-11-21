from django.contrib import admin
from .models import Bookmark# 추가
# Register your models here.

#관리자 모드에서 보여줄 모양을 클래스로 정의.
@admin.register(Bookmark) #Admin클래스에 model 클래스 등록 #방법2
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'title', 'url') # Tuple or List 여야함

#admin.site.register(Bookmark,BookmarkAdmin)# Admin클래스에 model 클래스 등록 #방법1