from django.contrib import admin

from .models import Disco,FormatoDisco



class DiscoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class FormatoDiscoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Disco,DiscoAdmin)
admin.site.register(FormatoDisco,FormatoDiscoAdmin)

