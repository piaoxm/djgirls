from django.conf import settings
from django.db import models
#from django.utils import timezone as tz

class University(models.Model):
    university_name = models.CharField(max_length=40)

    def __str__(self):
        return self.university_name

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, # <- 특정 사용자 모델에 종속적이지 않다.
        on_delete=models.CASCADE
    )

    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE
    )
    student_num = models.CharField(
        max_length=20
    )
    # created_at = models.DateTimeField(_('Created At'), null=False,
    #                                   db_column='created_at', blank=False,
    #                                   default=tz.now)
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        #db_table = 'account_profile'
        app_label = 'account' # <- account 앱(allauth의 앱) 카테고리에서 관리되도록 한다.

    def __str__(self):
        return "{} : {}".format(self.university,self.student_num)