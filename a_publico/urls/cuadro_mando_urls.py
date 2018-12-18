from django.conf.urls import url
from ..views import (CuadroMandoListView, CuadroMandoCreateView, CuadroMandoDetailView,
                     CuadroMandoUpdateView, CuadroMandoDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        (CuadroMandoCreateView.as_view()),
        name="cuadro_mando_create"),

    url(r'^(?P<pk>\d+)/update/$',
        (CuadroMandoUpdateView.as_view()),
        name="cuadro_mando_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        (CuadroMandoDeleteView.as_view()),
        name="cuadro_mando_delete"),

    url(r'^(?P<pk>\d+)/$',
        CuadroMandoDetailView.as_view(),
        name="cuadro_mando_detail"),

    url(r'^$',
        CuadroMandoListView.as_view(),
        name="cuadro_mando_list"),
]
