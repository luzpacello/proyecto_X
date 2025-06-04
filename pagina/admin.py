from django.contrib import admin
from .models import Publicacion
# Register your models here.

class paginaAdmin(admin.ModelAdmin):
    list_display = ('name', 'descrip')

admin.site.register(Publicacion, paginaAdmin)