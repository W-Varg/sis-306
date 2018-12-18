from django.conf.urls import url
from ..views import (CatalogoSoporteListView, CatalogoSoporteCreateView, CatalogoSoporteDetailView,
                     CatalogoSoporteUpdateView, CatalogoSoporteDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        (CatalogoSoporteCreateView.as_view()),
        name="catalogo_soporte_create"),

    url(r'^(?P<pk>\d+)/update/$',
        (CatalogoSoporteUpdateView.as_view()),
        name="catalogo_soporte_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        (CatalogoSoporteDeleteView.as_view()),
        name="catalogo_soporte_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoSoporteDetailView.as_view(),
        name="catalogo_soporte_detail"),

    url(r'^$',
        CatalogoSoporteListView.as_view(),
        name="catalogo_soporte_list"),
]
