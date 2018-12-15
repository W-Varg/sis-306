from django.conf.urls import url
from ..views import (ViaPublicaListView, ViaPublicaCreateView, ViaPublicaDetailView,
                     ViaPublicaUpdateView, ViaPublicaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ViaPublicaCreateView.as_view()),
        name="via_publica_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ViaPublicaUpdateView.as_view()),
        name="via_publica_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ViaPublicaDeleteView.as_view()),
        name="via_publica_delete"),

    url(r'^(?P<pk>\d+)/$',
        ViaPublicaDetailView.as_view(),
        name="via_publica_detail"),

    url(r'^$',
        ViaPublicaListView.as_view(),
        name="via_publica_list"),
]
