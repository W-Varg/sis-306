from django.contrib import admin
from .models import BarrioPedania, ViaPublica, CatalogoCalle, CatalogoLampara, CatalogoLuminaria, CatalogoSoporte, EquiposMedida, CuadroMando, PuntoLuz
from django_baker.admin import ExtendedModelAdminMixin


# class BarrioPedaniaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class ViaPublicaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class CatalogoCalleAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class CatalogoLamparaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class CatalogoLuminariaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class CatalogoSoporteAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class EquiposMedidaAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class CuadroMandoAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


# class PuntoLuzAdmin(ExtendedModelAdminMixin, admin.ModelAdmin):
#     extra_list_display = []
#     extra_list_filter = []
#     extra_search_fields = []
#     list_editable = []
#     raw_id_fields = []
#     inlines = []
#     filter_vertical = []
#     filter_horizontal = []
#     radio_fields = {}
#     prepopulated_fields = {}
#     formfield_overrides = {}
#     readonly_fields = []


admin.site.register(BarrioPedania)
admin.site.register(ViaPublica)
admin.site.register(CatalogoCalle)
admin.site.register(CatalogoLampara)
admin.site.register(CatalogoLuminaria)
admin.site.register(CatalogoSoporte)
admin.site.register(EquiposMedida)
admin.site.register(CuadroMando)
admin.site.register(PuntoLuz)
