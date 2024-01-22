from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name ='create'),
    path('delete/<int:pk>/', delete, name ='delete'),
    path('update/<int:pk>/', update, name ='update'),
    path('detail/<int:pk>/', detail, name ='detail'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path ('detail/<int:pk>/comment/', comment, name="comment"),
    path ('detail/<int:pk>/get_comments/<int:comment_pk>/', get_comments, name="get_comments"),
    path ('detail/<int:pk>/delete_comment/<int:postId>/<int:commentId>/', delete_comment, name = "delete_comment")
]