from django.contrib import admin
#추가한 단어 include
from .models import *
# Register your models here.
admin.site.register(Movie)