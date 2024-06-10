# api/urls.py
from django.urls import path
from .views import code_interpreter

urlpatterns = [
    path('code_interpreter/', code_interpreter, name='code_interpreter'),
]
