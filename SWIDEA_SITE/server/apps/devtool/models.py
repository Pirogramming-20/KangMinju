from django.db import models

class DevTool(models.Model):
    name = models.CharField('이름', max_length=24)
    kind = models.CharField('종류', max_length=24)
    dev_content = models.TextField('개발툴 설명')
    
    def __str__(self):
        return self.name
