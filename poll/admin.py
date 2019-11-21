from django.contrib import admin
from .models import Question, Choice# 추가

### 관리자 모드에서 보여줄 모양을 클래스로 정의.
class ChoiceInline(admin.TabularInline):#테이블 형태로 간격을 조밀하게  #class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
# 목록(list) 모드
    list_display = ('question_text', 'pub_date', 'was_published_recently')# Tuple or List 여야함
    list_filter = ['pub_date']
    search_fields = ['question_text']# 검색할 필드 지정(question_text 필드를 검색)

## 작성(write field) 모드
#    fields = ['pub_date', 'question_text']# Tuple or List 여야함
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information <-요렇게 표시됨', {'fields': ['pub_date'], 'classes': ['collapse']}),# 'classes': ['collapse'] 는 (숨기기처럼)접혀있음
    ]
    inlines = [ChoiceInline]


### Admin클래스에 model 클래스 등록
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


