from django.urls import path
from .models import homeview


url_patterns = [
    path('', homeview),
]

