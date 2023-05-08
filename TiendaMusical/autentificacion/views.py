from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
from tienda.models import Disco,FormatoDisco
from django.contrib.auth.models import User 
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
# Create your views here.

def registro(request):
    if request.method =='GET': 
        form = UserCreationCustom()  
        context = {  'form':form  }  

        return render(request,"registro.html",context)
    if request.method =='POST': 
        form = UserCreationCustom(request.POST) 
        if form.is_valid():
            print("valid")
            form.save()  
            user=form.save()  
            my_group = Group.objects.get(name='admins')
            my_group.user_set.add(user) 
            messages.success(request, 'Account created successfully')  
            return redirect ('Home')
        



def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("email")    
            contra=form.cleaned_data.get("password")    
            user=authenticate(email=nombre_usuario,password=contra)
            if user is not None:
                login(request,user)
                return redirect("Home")
            else:
                messages.error(request,"Usuario no valido")
        else:
            messages.error(request,"Informacion incorrecta")
    else:
        form=AuthenticationForm()
        return render(request,"login.html",{"form":form})
    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})



def productosAdmin(request):
    all_discos=Disco.objects.all()   

    return render(request,"productos.html",{"discos":all_discos})

def Crearproducto(request):
  
    return render(request,"CrearProducto.html")

def eliminarUsuario(request,disco_id):

    disc=User.objects.get(id=int(disco_id))
    disc.delete()

    return redirect('ListaUsuarios')


def eliminarProducto(request,disco_id):

    disc=Disco.objects.get(id=int(disco_id))
    disc.delete()

    return redirect('productosAdmin')

def CrearDisco(request):

    nnombre=request.POST['nombre']
    nalbum=request.POST['nombreAlbum']
    nartista=request.POST['artista']
    nprecio=request.POST['precio']
    nstock=request.POST['stock']
    nanno=request.POST['annopublicacion']
    nimagen=request.POST['imagen']
    nformato=request.POST['formatos']

    formatin=FormatoDisco.objects.get(id=int(nformato))

    dis= Disco(nombre=nnombre,nombreAlbum=nalbum,artista=nartista,formatos=formatin,precio=int(nprecio),vendidos=0,stock=int(nstock),annopublicacion='2023-05-15',imagen='null',oferta=True)
    dis.save()



    return redirect('productosAdmin')


def ListaUsuarios (request):
    lista=User.objects.all()
    return render(request,'listaUsuarios.html',{"users":lista})