from django.shortcuts import render
from .models import Goku, FormJB
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import CreateUserForm, LoginForm
from django.template import loader
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  
from .serializers import perroSerializer





def index(request):
    form2 = LoginForm(request.POST or None)
    if form2.is_valid():    
        data = form.cleaned_data
        correo = data.get("correo")
        password = data.get("password")
        acceso = authenticate(correo=correo, password=password)
        if acceso is not None:
            login(request,acceso)
            return render ('goku_list'.format (nombres_usuarios))
    
        else:
            return render ("Usuario y/o Contraseña invalidos")
    
    else:
            form = LoginForm()
            
    var = {
            "form_login":form,
    }
    return render(request,'misperris/index.html',var)


def goku_list(request): 
    lomitos_disponibles = Goku.objects.filter(estado_lomito="Disponible")[:3]
    lomitos_adoptados   = Goku.objects.filter(estado_lomito="Adoptado")[:3]
    lomitos_rescatados  = Goku.objects.filter(estado_lomito="Rescatado")[:3]    
    context = {'lomitos_disponibles': lomitos_disponibles,
               'lomitos_adoptados':   lomitos_adoptados,
               'lomitos_rescatados':  lomitos_rescatados}   
    return render(request, 'misperris/goku_list.html', context)


def goku_lista(request):
    lista_de_lomitos = Goku.objects.all()
    lista_lomitos_disponibles = Goku.objects.filter(estado_lomito="disponible")
    context = {'lista_de_lomitos': lista_de_lomitos,			
              'lista_lomitos_disponibles':lista_lomitos_disponibles}
    return render(request,'misperris/goku_lista.html',context)



def goku_details(request,pk):
    goku = get_object_or_404(Goku, pk=pk)
    context = {'goku':goku}
    return render (request, 'misperris/goku_details.html',context)      



def goku_new(request):
    if request.method == 'POST':
        form = CreateUserForm( request.POST,request.FILES)
        if form.is_valid():
            gohan = form.save(commit=False)
            gohan.save()
            return redirect('goku_details',pk=gohan.pk)
    else:
        form = CreateUserForm()
    context = {'form':form}
    return render(request, 'misperris/goku_edit.html',context)



def goku_edit(request,pk):
    goku = get_object_or_404(Goku,pk=pk)
    if request.method == 'POST':
        form = CreateUserForm(request.POST,request.FILES, instance=goku)
        if form.is_valid():
            goku = form.save(commit=False)
            goku.save()
            return redirect('goku_details',pk=goku.pk)
    else:
        form = CreateUserForm(instance = goku)
    context = {'form':form}
    return render(request,'misperris/goku_edit.html',context)  

 

def goku_formulario(request):
    
        correo1 = request.POST.get('txtEmail',False)        
        rut1 = request.POST.get('txtrut',False)
        nombre1 = request.POST.get('txtName',False)
        ingresarFecha = request.POST.get('txtdate',False)
        telefono1 = request.POST.get('txtPhone',False)
        region1 = request.POST.get('txtRegion',False)
        ciudad1 = request.POST.get('txtCity',False)
        tipo1 = request.POST.get('sel-vivienda',False)
        password1 = request.POST.get('txtPassword',False)        
        modelos = FormJB(correo = correo1,
        rut_usuario = rut1,
        nombre = nombre1,
        ingresar_fecha = ingresarFecha,
        telefono = telefono1,
        region = region1,
        ciudad = ciudad1,
        tipo = tipo1,
        password = password1)        
        modelos.save() 
        return render(request, 'misperris/goku_formulario.html',{})

class ListarPerro(APIView):

    def get(self,request):
        perros = Goku.objects.all()
        serializers = perroSerializer(perros,context={"request":request},many=True)
        return Response(serializers.data)

    def post(self,request):
        pass   

