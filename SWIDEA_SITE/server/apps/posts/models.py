from django.db import models
from apps.devtool.models import DevTool
#from apps.local_users.models import LocalUser

# Create your models here.
class Post(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default = 0)
    #예상 개발툴
    #user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, verbose_name='작성자')
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name='개발툴')
    created_date = models.DateTimeField('작성일', auto_now_add=True)
    
    def __str__(self):
        return self.title