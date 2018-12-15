from django.conf.urls import url
from ..views import (CatalogoSoportesListView, CatalogoSoportesCreateView, CatalogoSoportesDetailView,
                     CatalogoSoportesUpdateView, CatalogoSoportesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoSoportesCreateView.as_view()),
        name="catalogo_soportes_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoSoportesUpdateView.as_view()),
        name="catalogo_soportes_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoSoportesDeleteView.as_view()),
        name="catalogo_soportes_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoSoportesDetailView.as_view(),
        name="catalogo_soportes_detail"),

    url(r'^$',
        CatalogoSoportesListView.as_view(),
        name="catalogo_soportes_list"),
]
