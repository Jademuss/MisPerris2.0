from django.db import models
from django.utils import timezone


class FormJB(models.Model):
    correo         = models.CharField(max_length=15)
    rut_usuario    = models.AutoField(primary_key=True)
    nombre         = models.CharField(max_length=15)        
    ingresar_fecha = models.CharField(max_length=30)
    telefono       = models.IntegerField(blank=True,null=True)
    region         = models.CharField(max_length=30)
    ciudad         = models.CharField(max_length= 30)
    tipo           = models.CharField(max_length=30)
    password       = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nombre

class Goku(models.Model): 
    opciones_estado    = (('Rescatado','rescatado'),('Disponible','disponible'),('Adoptado','adoptado'))          
    id_lomito          = models.AutoField(primary_key=True)
    imagen_lomito      = models.ImageField(blank=True,null=True,upload_to = "lomito/%Y/%m/$d/")
    nombre_lomito      = models.CharField(max_length=15)
    raza_lomito        = models.CharField(max_length=30)
    descripcion_lomito = models.TextField()
    estado_lomito      = models.CharField(max_length=15, choices= opciones_estado)        
    
    def __str__(self):
        return self.nombre_lomito 

    
    

    
    
    