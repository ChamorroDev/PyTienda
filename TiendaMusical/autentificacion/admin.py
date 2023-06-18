from django.contrib import admin

from .models import Direccion



class DireccionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Direccion,DireccionAdmin)

