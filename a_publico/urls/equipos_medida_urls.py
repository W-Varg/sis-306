from django.conf.urls import url
from ..views import (EquiposMedidaListView, EquiposMedidaCreateView, EquiposMedidaDetailView,
                     EquiposMedidaUpdateView, EquiposMedidaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(EquiposMedidaCreateView.as_view()),
        name="equipos_medida_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(EquiposMedidaUpdateView.as_view()),
        name="equipos_medida_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(EquiposMedidaDeleteView.as_view()),
        name="equipos_medida_delete"),

    url(r'^(?P<pk>\d+)/$',
        EquiposMedidaDetailView.as_view(),
        name="equipos_medida_detail"),

    url(r'^$',
        EquiposMedidaListView.as_view(),
        name="equipos_medida_list"),
]
