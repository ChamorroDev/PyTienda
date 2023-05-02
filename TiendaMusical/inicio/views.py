from django.shortcuts import render
from tienda.models import Disco 


def home(request):
    all_discos=Disco.objects.all()   
 
    return render(request,"home.html",{"discos":all_discos})
