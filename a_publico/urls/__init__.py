from django.conf.urls import include, url

app_name="a_publico"

urlpatterns = [

    url(r'^barrio_pedanias/', include('a_publico.urls.barrio_pedania_urls')),  # NOQA
    url(r'^catalogo_calless/', include('a_publico.urls.catalogo_calles_urls')),
    url(r'^catalogo_lamparass/', include('a_publico.urls.catalogo_lamparas_urls')),
    url(r'^catalogo_luminariass/', include('a_publico.urls.catalogo_luminarias_urls')),
    url(r'^catalogo_soportess/', include('a_publico.urls.catalogo_soportes_urls')),
    url(r'^cuadro_mandos/', include('a_publico.urls.cuadro_mando_urls')),
    url(r'^equipos_medidas/', include('a_publico.urls.equipos_medida_urls')),
    url(r'^punto_luzs/', include('a_publico.urls.punto_luz_urls')),
    url(r'^via_publicas/', include('a_publico.urls.via_publica_urls')),
]
