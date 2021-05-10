from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

###############   DIFICULTAD    #################
class DificultadResource(resources.ModelResource):
    class Meta:
        model = Dificultad

class DificultadAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class = DificultadResource


###############   CATEGORIA    #################
class CategoriaRetoResource(resources.ModelResource):
    class Meta:
        model = CategoriaReto

class CategoriaRetoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class = CategoriaRetoResource



###############   CHALLENGE    #################
class ChallengeResource(resources.ModelResource):
    class Meta:
        model = Challenge

class ChallengeAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','categoria']
    list_display = ('id','titulo','slug','dificultad','categoria','estado','fecha_creacion')
    resource_class = ChallengeResource


admin.site.register(Dificultad, DificultadAdmin)
admin.site.register(CategoriaReto, CategoriaRetoAdmin)
admin.site.register(Challenge, ChallengeAdmin)