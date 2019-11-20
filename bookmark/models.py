from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField('사이트 제목', max_length=100, blank=True, null=True)
    url = models.URLField(verbose_name='URL주소', unique=True)#   'url'는 별칭(verbose_name)

    #객체를 나타네는 문자열(테이블명)
    def __str__(self):
        return self.title