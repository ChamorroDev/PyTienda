from django.contrib.auth.models import User
from django.db import models

class Direccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='direcciones')    
    direccion = models.CharField(max_length=100)
    numeracion = models.IntegerField(default=0)
    ciudad = models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'direccion','numeracion', 'ciudad')
        verbose_name="Direccion"
        verbose_name_plural="Direcciones"
