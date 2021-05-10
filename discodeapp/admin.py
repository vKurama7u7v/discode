from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

###############   CATEGORIA    #################
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class = CategoriaResource


###############   AUTOR    #################
class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','apellidos','correo']
    list_display = ('id','nombre','apellidos','correo','estado','fecha_creacion')
    resource_class = AutorResource


###############   POST    #################
class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','categoria','autor']
    list_display = ('id','titulo','slug','autor','categoria','estado','fecha_creacion')
    resource_class = PostResource


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)

