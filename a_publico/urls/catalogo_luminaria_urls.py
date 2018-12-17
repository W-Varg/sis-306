from django.conf.urls import url
from ..views import (CatalogoLuminariaListView, CatalogoLuminariaCreateView, CatalogoLuminariaDetailView,
                     CatalogoLuminariaUpdateView, CatalogoLuminariaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoLuminariaCreateView.as_view()),
        name="catalogo_luminaria_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoLuminariaUpdateView.as_view()),
        name="catalogo_luminaria_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoLuminariaDeleteView.as_view()),
        name="catalogo_luminaria_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoLuminariaDetailView.as_view(),
        name="catalogo_luminaria_detail"),

    url(r'^$',
        CatalogoLuminariaListView.as_view(),
        name="catalogo_luminaria_list"),
]
