from django.shortcuts import render

from .models import Disco 
from .models import FormatoDisco 

# Create your views here.
def tienda(request):

    all_tipos=FormatoDisco.objects.all()
    all_discos=Disco.objects.all()   

    return render(request,"tienda.html",{"discos":all_discos,"formatos":all_tipos})

def formato(request,formato_id):
    all_tipos=FormatoDisco.objects.all()
    all_formats=FormatoDisco.objects.get(id=formato_id)
    all_discos=Disco.objects.filter(formatos=formato_id)
    return render(request,"tienda.html",{"formato":all_formats,"discos":all_discos,"formatos":all_tipos})
