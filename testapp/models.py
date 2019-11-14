from django.db import models

class Company(models.Model):
    A = '간'
    B = '복'
    C = '성'
    D = '복'
    BOOK_DUTY = (
        ('간', '간편'),
        ('복', '복식'),
        ('성', '성실'),
        ('법', '법인'),
    )
    
    # 맨처음 verbose name
    corp = models.BooleanField
    com_num = models.CharField("법인등록번호", max_length=13, unique=True, help_text="법인등록번호, 개인사업자는 주민등록번호 <em>하이픈(-) 을 제외하고 숫자만 입력하세요</em>.")
    branch_num = models.CharField("사업자등록번호", max_length=10, db_index=True)#db_index=True 데이터베이스 색인이 작성됩
    com_name = models.CharField(max_length=60)
    ceo_name = models.CharField(max_length=40)
    book_duty = models.CharField(max_length=1, choices=BOOK_DUTY, default='간')
    date_open = models.DateField()
    date_close = models.DateField()
    memo = models.TextField()
    # created_date= models.DateTimeField(default=timezone.now)
    # published_date = models.DateTimeField(blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    ### 승인된 댓글만 보이기
    # approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()
        
    # # 승인된 댓글의 개수만 보이게 하기위해
    # def approved_comments(self):
    #     return self.comments.filter(approved_comment=True)



    # REQUIRED_FIELDS = ["email"] # 필수 항목

    class Meta:        # 관리자모드 등에 반영
        ordering = ['com_name', 'date_open']
        # db_table= 'tb_post' #기본 DB테이블명은 "앱이름_모델명"
        # verbose_name='company'
        # verbose_name_plural='companys'
        index_together=[['id','branch_num','com_name']]# 멀티 컬럼 색인 기능(id, slug 필드를 묶어서 색인)
        # app_label = 'account' #  admin모드에서 특정 앱 카테고리에서 관리되도록 한다.
        # abstract = True  # 추상 모델
    
    def __str__(self):      # admin 사이트 에서도 객체의 표현이 사용
        return "{} ({}) [{}]".format(self.com_name,self.ceo_name,self.book_duty)

    def get_absolute_url(self):
         #return reverse('testapp:com_detail', args=[self.pk])
         return reverse('testapp:com_detail', kwargs={'pk': self.pk})
    #복식부기의무자
    def is_doublebook(self):
        return self.book_duty in (self.B, self.C, self.D)
    
    # memo 100자만 보여주기
    def summary(self):
        return self.memo[:100]

