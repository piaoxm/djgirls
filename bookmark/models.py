from django.db import models
from django.conf import settings #settings.AUTH_USER_MODEL 를 사용하기위해
#from django.contrib.auth.models import User #settings.AUTH_USER_MODEL 대신 User 를 사용하기위해
# Create your models here.
DEFAULT_USER_ID=1

class Bookmark(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    title = models.CharField('사이트 제목', max_length=100, blank=True, null=True)
    url = models.URLField(verbose_name='URL주소', unique=True)#   'url'는 별칭(verbose_name)

    #객체를 나타네는 문자열(테이블명)
    def __str__(self):
        return "{} : {}".format(self.title,self.url)