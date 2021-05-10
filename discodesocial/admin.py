from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

###############   PERFIL    #################
class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile

class ProfileAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','user','estado')
    resource_class = ProfileResource


###############   PUBLICACIONES    #################
class PublicacionResource(resources.ModelResource):
    class Meta:
        model = Publicacion

class PublicacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['id']
    list_display = ('id','user','estado','fecha_creacion')
    resource_class = PublicacionResource




admin.site.register(Profile, ProfileAdmin)
admin.site.register(Publicacion, PublicacionAdmin)