from django.conf.urls import include, url
from django.urls import path
from ..views import index
app_name="a_publico"

urlpatterns = [
    url(r'/',index, name='index'),
    url(r'^barrio_pedanias/', include('a_publico.urls.barrio_pedania_urls')),  # NOQA
    url(r'^via_publicas/', include('a_publico.urls.via_publica_urls')),
    url(r'^catalogo_calles/', include('a_publico.urls.catalogo_calle_urls')),
    url(r'^catalogo_lamparas/', include('a_publico.urls.catalogo_lampara_urls')),
    url(r'^catalogo_luminarias/', include('a_publico.urls.catalogo_luminaria_urls')),
    url(r'^catalogo_soportes/', include('a_publico.urls.catalogo_soporte_urls')),
    url(r'^equipos_medidas/', include('a_publico.urls.equipos_medida_urls')),
    url(r'^cuadro_mandos/', include('a_publico.urls.cuadro_mando_urls')),
    url(r'^punto_luzs/', include('a_publico.urls.punto_luz_urls')),
]
