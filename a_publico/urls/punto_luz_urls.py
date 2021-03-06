from django.conf.urls import url
from ..views import (PuntoLuzListView, PuntoLuzCreateView, PuntoLuzDetailView,
                     PuntoLuzUpdateView, PuntoLuzDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        (PuntoLuzCreateView.as_view()),
        name="punto_luz_create"),

    url(r'^(?P<pk>\d+)/update/$',
        (PuntoLuzUpdateView.as_view()),
        name="punto_luz_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        (PuntoLuzDeleteView.as_view()),
        name="punto_luz_delete"),

    url(r'^(?P<pk>\d+)/$',
        PuntoLuzDetailView.as_view(),
        name="punto_luz_detail"),

    url(r'^$',
        PuntoLuzListView.as_view(),
        name="punto_luz_list"),
]
