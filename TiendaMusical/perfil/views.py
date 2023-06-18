from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from autentificacion.models import Direccion
from .forms import DireccionForm
from django.contrib import messages

@login_required
def perfil (request):
    if request.method =='GET': 
        user = request.user
        direcciones = Direccion.objects.filter(user=user)
        form=DireccionForm()
        context = {
        'user': user,
        'direcciones': direcciones,
        'form': form
        }  
        return render(request,"perfil.html",context)
    if request.method =='POST': 
        datos_formulario = DireccionForm(data=request.POST)
        es_valido = datos_formulario.is_valid()
        if es_valido:
            direccion = request.POST.get('direccion')
            numeracion = request.POST.get('numeracion') 
            ciudad = request.POST.get('ciudad') 
            dir= Direccion(user_id=request.user.id,direccion=direccion,numeracion=numeracion,ciudad=ciudad)
            dir.save()
            messages.add_message(request=request,level=messages.SUCCESS,message="Registrado Correctamente")
            return redirect ('perfil')
         
        contexto = {
            'formulario': datos_formulario
        }
        return render(request, 'perfil.html', contexto)  

 