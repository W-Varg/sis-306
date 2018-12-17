from django.conf.urls import url
from ..views import (CatalogoLamparaListView, CatalogoLamparaCreateView, CatalogoLamparaDetailView,
                     CatalogoLamparaUpdateView, CatalogoLamparaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoLamparaCreateView.as_view()),
        name="catalogo_lampara_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoLamparaUpdateView.as_view()),
        name="catalogo_lampara_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoLamparaDeleteView.as_view()),
        name="catalogo_lampara_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoLamparaDetailView.as_view(),
        name="catalogo_lampara_detail"),

    url(r'^$',
        CatalogoLamparaListView.as_view(),
        name="catalogo_lampara_list"),
]
