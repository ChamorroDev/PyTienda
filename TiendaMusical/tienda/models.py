from django.db import models



class FormatoDisco(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name="FormatoDisco"
        verbose_name_plural="formatoDiscos"

    def __str__(self)  :
        return self.nombre

class Disco(models.Model):
    nombre=models.CharField(max_length=50)
    nombreAlbum=models.CharField(max_length=50)
    artista=models.CharField(max_length=50,null=True)
    precio=models.IntegerField()
    vendidos=models.IntegerField(default=0)
    stock=models.IntegerField(default=1)
    annopublicacion=models.DateField()
    imagen=models.ImageField(upload_to='imgDiscos', null=True,blank=True)
    formatos=models.ForeignKey(FormatoDisco, on_delete=models.CASCADE)
    oferta=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name="Disco"
        verbose_name_plural="Discos"

    def __str__(self)  :
        return self.nombre
        


