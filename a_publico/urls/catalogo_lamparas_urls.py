from django.conf.urls import url
from ..views import (CatalogoLamparasListView, CatalogoLamparasCreateView, CatalogoLamparasDetailView,
                     CatalogoLamparasUpdateView, CatalogoLamparasDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoLamparasCreateView.as_view()),
        name="catalogo_lamparas_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoLamparasUpdateView.as_view()),
        name="catalogo_lamparas_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoLamparasDeleteView.as_view()),
        name="catalogo_lamparas_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoLamparasDetailView.as_view(),
        name="catalogo_lamparas_detail"),

    url(r'^$',
        CatalogoLamparasListView.as_view(),
        name="catalogo_lamparas_list"),
]
