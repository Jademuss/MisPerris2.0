from django import forms
from .models import Goku, FormJB
from django.contrib.auth.models import User



class CreateUserForm(forms.ModelForm):
    
    class Meta:
        model = Goku
        fields = ['imagen_lomito','nombre_lomito','raza_lomito','estado_lomito','descripcion_lomito']
        
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = FormJB
        fields  = ['correo','password']