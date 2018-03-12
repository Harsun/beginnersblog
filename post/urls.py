from django.urls import path
from .views import *


app_name = 'post'

urlpatterns = [
    path('', homeview, name='index'),
    path('<int:id>', detailview, name='detail'),
    path('create', createview, name='create'),
    path('<int:id>/edit', editview, name='edit'),
    path('<int:id>/delete', deleteview, name='delete'),
]
