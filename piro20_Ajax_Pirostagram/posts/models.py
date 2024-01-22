from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField('제목', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField('설명')
    like = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  

    # class Meta:
    #     ordering = ['-created_at']
        
    def __str__(self):
        return self.title