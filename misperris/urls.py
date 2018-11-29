from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    path('', views.goku_list, name='goku_list'),
    path('goku_list/goku_formulario/', views.goku_formulario, name="goku_formulario"),    
    path('goku_list/goku_lista/', views.goku_lista, name='goku_lista'),
    path('goku_list/goku_lista/<int:pk>/', views.goku_details, name='goku_details'),
    path('goku_list/goku_new/', views.goku_new, name= 'goku_new'),    
    path('goku_list/<int:pk>/edit/', views.goku_edit , name ='goku_edit'),  
    path('api/',views.ListarPerro.as_view()),

]	