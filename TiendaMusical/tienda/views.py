from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import Http404

from .models import Disco 
from .models import FormatoDisco 



# Create your views here.
def tienda(request):

    all_tipos=FormatoDisco.objects.all()
    all_discos=Disco.objects.all()   
    page= request.GET.get ('page',1)
    try:
        paginator= Paginator (all_discos,10)
        all_discos = paginator.page(page)
    except:
        raise Http404
    data ={
        'entity':all_discos,
        'paginator':paginator,
        "formatos":all_tipos
    }
    
    return render(request,"tienda.html",data)

def formato(request,formato_id):
    

    
    all_tipos=FormatoDisco.objects.all()
    all_formats=FormatoDisco.objects.get(id=formato_id)
    all_discos=Disco.objects.filter(formatos=formato_id)
    page= request.GET.get ('page',1)
    try:
        paginator= Paginator (all_discos,10)
        all_discos = paginator.page(page)
    except:
        raise Http404
    data ={
        'entity':all_discos,
        'paginator':paginator,
        "formatos":all_tipos
    }
    return render(request,"tienda.html",data)
