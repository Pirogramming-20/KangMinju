from django.db import models
#from apps.local_users.models import LocalUser

# Create your models here.
class Post(models.Model):
    title = models.CharField('아이디어명', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.CharField('아이디어 설명', max_length=24)
    interest = models.IntegerField('아이디어 관심도', default = 0)
    #예상 개발툴
    #user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, verbose_name='작성자')
    
    
    
    # admin에서 보여지는 str 
    def __str__(self):
        return self.title