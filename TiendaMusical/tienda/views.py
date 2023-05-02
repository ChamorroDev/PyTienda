from django.shortcuts import render

from .models import Disco 

# Create your views here.
def tienda(request):

 
    all_discos=Disco.objects.all()   

    return render(request,"tienda.html",{"discos":all_discos})

