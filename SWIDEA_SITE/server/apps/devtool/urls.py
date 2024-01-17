from django.urls import path
from .views import *

app_name = 'devtools'

urlpatterns = [
    path('list/', devtool_list, name='list'),
    path('create/', create, name ='create'),
    path('delete/<int:pk>/', delete, name="delete"),
    path('update/<int:pk>/', update, name='update'),
    path('detail/<int:pk>/', detail, name='detail'),
]