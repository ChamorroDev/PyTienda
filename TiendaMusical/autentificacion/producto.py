

def deleteDisco(request,disco_id):

    disc=Disco.objects.get(id=disco_id)
    disc.delete()

    return redirect('/')
    
    
    Disco(nombre='nombre',nombreAlbum='album',artista='artista',formatos=formatin,precio=1,vendidos=0,stock=1,annopublicacion='2023-05-15',imagen='null',oferta=True)
