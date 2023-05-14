from django.shortcuts import render,redirect 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import Group
from .forms import *
from django.contrib.auth.decorators import login_required
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
            my_group = Group.objects.get(name='normal')
            my_group.user_set.add(user) 
            messages.success(request, 'Account created successfully')  
            return redirect ('Home')
        
    return redirect ('')  



def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        print (request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")    
            contra=form.cleaned_data.get("password")    
            user=authenticate(username=nombre_usuario,password=contra)
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

@login_required(redirect_field_name='login_required',login_url='Home')
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')



