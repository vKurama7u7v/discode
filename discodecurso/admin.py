from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

###############   CATEGORIA    #################
class CategoriaCursoResource(resources.ModelResource):
    class Meta:
        model = CategoriaCurso

class CategoriaCursoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class = CategoriaCursoResource



###############   CURSO    #################
class CursoResource(resources.ModelResource):
    class Meta:
        model = Curso

class CursoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','categoria']
    list_display = ('id','titulo','slug','categoria','estado','fecha_creacion')
    resource_class = CursoResource



###############   TEMA    #################
class TemaResource(resources.ModelResource):
    class Meta:
        model = Tema

class TemaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','identificador']
    list_display = ('id', 'identificador','titulo','estado','fecha_creacion')
    resource_class = TemaResource



###############   LECCION    #################
class LeccionResource(resources.ModelResource):
    class Meta:
        model = Leccion

class LeccionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['subtitulo','identificador']
    list_display = ('id', 'identificador','subtitulo','slug','estado','fecha_creacion')
    resource_class = LeccionResource


admin.site.register(CategoriaCurso, CategoriaCursoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Leccion, LeccionAdmin)
