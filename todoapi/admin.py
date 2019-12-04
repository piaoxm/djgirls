from django.contrib import admin
from .models import Todoapi

class TodoapiAdmin(admin.ModelAdmin):
    list_display = ['title','completed'] #list_display = ['user','title','completed']
    list_editable = ['title','completed']
    # raw_id_fields = ['user'] # 위젯 : ForeignKey, ManyToManyField(:여러개는 콤마로 구분) 필드 옆에 돋보기 버튼을 표시하여 사용자가 값을 검색하고 선택할 수 있도록 한다.
    
# admin.site.register(Todoapi, TodoapiAdmin)

admin.site.register(Todoapi)