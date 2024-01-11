from django.contrib import admin
#추가한 단어 include
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
		#post 코드 추
    path('review/', include("review.urls")),
]
# Register your models here.
