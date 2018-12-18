from django.conf.urls import url
from ..views import (CatalogoCalleListView, CatalogoCalleCreateView, CatalogoCalleDetailView,
                     CatalogoCalleUpdateView, CatalogoCalleDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        (CatalogoCalleCreateView.as_view()),
        name="catalogo_calle_create"),

    url(r'^(?P<pk>\d+)/update/$',
        (CatalogoCalleUpdateView.as_view()),
        name="catalogo_calle_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        (CatalogoCalleDeleteView.as_view()),
        name="catalogo_calle_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoCalleDetailView.as_view(),
        name="catalogo_calle_detail"),

    url(r'^$',
        CatalogoCalleListView.as_view(),
        name="catalogo_calle_list"),
]
