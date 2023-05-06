from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from tienda.models import Disco
# Create your views here.

def registro(request):
    return render(request,"registro.html")
"""
    def get(self,request):
        form=UserCreationForm()


    def post(self,request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request,usuario)
            return redirect("Home")
        else:
            for msg in form.error_messages:

                messages.error(request,form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})

        """


def logear(request):
    return render(request,"login.html")



def productosAdmin(request):
    all_discos=Disco.objects.all()   

    return render(request,"productos.html",{"discos":all_discos})

def Crearproducto(request):
  

    return render(request,"CrearProducto.html")