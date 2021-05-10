from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
###############   CATEGORIA FAQS    #################
class CategoriaFAQResource(resources.ModelResource):
    class Meta:
        model = CategoriaFAQ

class CategoriaFAQAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('id','nombre','estado','fecha_creacion')
    resource_class = CategoriaFAQResource


###############   FAQS    #################
class FAQResource(resources.ModelResource):
    class Meta:
        model = Faqs

class FAQAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['pregunta','categoria']
    list_display = ('id','pregunta','categoria','estado','fecha_creacion')
    resource_class = FAQResource

admin.site.register(CategoriaFAQ, CategoriaFAQAdmin)
admin.site.register(Faqs, FAQAdmin)