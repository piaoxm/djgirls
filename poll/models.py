import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField('Question!!', max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    #  admin.py의 list_display에 사용되는 칼럼(was_published_recently)의 속성
    was_published_recently.admin_order_field = 'pub_date'   # 정렬시 정렬기준으로 할 필드 지정
    was_published_recently.boolean = True   # true/False 를 O/X 아이콘으로 나타내는 기능.
    was_published_recently.short_description = '24시간이내 published'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return "{} (투표수:{})".format(self.choice_text,self.votes)