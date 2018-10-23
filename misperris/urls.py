from django.urls import path
from . import views

urlpatterns = [
    path('', views.goku_list, name='goku_list'),
    path('goku_list/goku_formulario/', views.goku_formulario, name="goku_formulario"),
    path('goku_list/goku_formulario/goku_notfound/', views.goku_notfound, name='goku_notfound'),    
]