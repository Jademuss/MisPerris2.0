from django.urls import path
from . import views

urlpatterns = [
    path('', views.goku_list, name='goku_list'),
]