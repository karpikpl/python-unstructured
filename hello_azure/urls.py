from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('word', views.word, name='word'),
    path('excel', views.excel, name='excel'),
    path('powerpoint', views.powerpoint, name='powerpoint'),
]