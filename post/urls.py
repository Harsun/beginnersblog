from django.urls import path
from .views import *


app_name = 'post'

urlpatterns = [
    path('', homeview, name='index'),
    path('create/', createview, name='create'),
    path('<slug:slug>/', detailview, name='detail'),
    path('<slug:slug>/edit/', editview, name='edit'),
    path('<slug:slug>/delete/', deleteview, name='delete'),
]
