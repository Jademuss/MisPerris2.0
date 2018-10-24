from django.urls import path
from . import views

urlpatterns = [
    path('', views.goku_list, name='goku_list'),
    path('goku_list/goku_formulario/', views.goku_formulario, name="goku_formulario"),
    path('goku_list/goku_formulario/goku_perros/', views.goku_perros, name="goku_perros"),
    path('goku_list/goku_formulario/goku_perros/goku_notfound/', views.goku_notfound, name='goku_notfound'),    
]