from django.contrib import admin
from django.contrib.auth.models import Group

from .models import BarrioPedania, ViaPublica, CatalogoCalle, CatalogoLampara, CatalogoLuminaria, CatalogoSoporte, EquiposMedida, CuadroMando, PuntoLuz

admin.site.unregister(Group)
admin.site.site_header = "Administracion de Alumbrado Publico, Base de Datos III"
admin.site.register(BarrioPedania)
admin.site.register(ViaPublica)
admin.site.register(CatalogoCalle)
admin.site.register(CatalogoLampara)
admin.site.register(CatalogoLuminaria)
admin.site.register(CatalogoSoporte)
admin.site.register(EquiposMedida)
admin.site.register(CuadroMando)
admin.site.register(PuntoLuz)
