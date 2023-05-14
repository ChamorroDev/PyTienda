from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from tienda.models import Disco,FormatoDisco
from django.contrib.auth.models import User 
from datetime import datetime
# Create your views here.


## PRODUCTOS

@login_required(redirect_field_name='login_required',login_url='Home')
def productosAdmin(request):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            all_discos=Disco.objects.all()   
            return render(request,"productos.html",{"discos":all_discos})
            
    return redirect('Home')


@login_required(login_url='Home')
def Crearproducto(request):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
  
            return render(request,"CrearProducto.html")
    return redirect('Home')



@login_required(login_url='Home')
def editar_producto(request, disco_id):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            if request.method == 'POST':
                noferta = request.POST.get('oferta') 
                noferta = bool(noferta)  
                nnombre=request.POST['nombre']
                nalbum=request.POST['nombreAlbum']
                nartista=request.POST['artista']
                nprecio=request.POST['precio']
                nstock=request.POST['stock']
                nanno=request.POST['annopublicacion']
                nimagen=request.POST['imagen']
                nformato=request.POST['formatos']
                nformato=FormatoDisco.objects.get(id=int(nformato))
                now = datetime.now()
            
                Disco.objects.filter(id=disco_id).update(oferta=noferta,nombre=nnombre,nombreAlbum=nalbum,artista=nartista,precio=nprecio,stock=nstock,annopublicacion=nanno,imagen=nimagen,formatos_id=nformato,updated=now)
                return redirect('productosAdmin')
            if  request.method == 'GET':
                disco = Disco.objects.filter(id=disco_id).values().first()
                return render(request,'EditarProducto.html',{"disco":disco})         
    return redirect('Home')



@login_required(login_url='Home')
def eliminarProducto(request,disco_id):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            disc=Disco.objects.get(id=int(disco_id))
            disc.delete()
            return redirect('productosAdmin')
    return redirect('Home')



@login_required(login_url='Home')
def CrearDisco(request):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            nnombre=request.POST['nombre']
            nalbum=request.POST['nombreAlbum']
            nartista=request.POST['artista']
            nprecio=request.POST['precio']
            nstock=request.POST['stock']
            nanno=request.POST['annopublicacion']
            nimagen=request.POST['imagen']
            nformato=request.POST['formatos']
            noferta = request.POST.get('oferta') 
            noferta = bool(noferta) 
            formatin=FormatoDisco.objects.get(id=int(nformato))
            dis= Disco(oferta=noferta,nombre=nnombre,nombreAlbum=nalbum,artista=nartista,formatos=formatin,precio=int(nprecio),vendidos=0,stock=int(nstock),annopublicacion='2023-05-15',imagen='null')
            dis.save()
            return redirect('productosAdmin')
    return redirect('Home')

## USUARIO 

@login_required(login_url='Home')
def ListaUsuarios (request):
    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            lista=User.objects.all()
            return render(request,'listaUsuarios.html',{"users":lista})

    return redirect('Home')

        
@login_required(login_url='Home')
def eliminarUsuario(request,disco_id):

    for grupo in request.user.groups.all():
        if grupo.name == 'admins':
            disc=User.objects.get(id=int(disco_id))
            disc.delete()
            return redirect('ListaUsuarios')
    return redirect('Home')
 