from django.conf.urls import url
from ..views import (CatalogoCallesListView, CatalogoCallesCreateView, CatalogoCallesDetailView,
                     CatalogoCallesUpdateView, CatalogoCallesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoCallesCreateView.as_view()),
        name="catalogo_calles_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoCallesUpdateView.as_view()),
        name="catalogo_calles_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoCallesDeleteView.as_view()),
        name="catalogo_calles_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoCallesDetailView.as_view(),
        name="catalogo_calles_detail"),

    url(r'^$',
        CatalogoCallesListView.as_view(),
        name="catalogo_calles_list"),
]
