from django.conf.urls import url
from ..views import (CatalogoCalleListView, CatalogoCalleCreateView, CatalogoCalleDetailView,
                     CatalogoCalleUpdateView, CatalogoCalleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoCalleCreateView.as_view()),
        name="catalogo_calle_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoCalleUpdateView.as_view()),
        name="catalogo_calle_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoCalleDeleteView.as_view()),
        name="catalogo_calle_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoCalleDetailView.as_view(),
        name="catalogo_calle_detail"),

    url(r'^$',
        CatalogoCalleListView.as_view(),
        name="catalogo_calle_list"),
]
