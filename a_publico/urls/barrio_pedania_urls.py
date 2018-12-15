from django.conf.urls import url
from ..views import (BarrioPedaniaListView, BarrioPedaniaCreateView, BarrioPedaniaDetailView,
                     BarrioPedaniaUpdateView, BarrioPedaniaDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(BarrioPedaniaCreateView.as_view()),
        name="barrio_pedania_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(BarrioPedaniaUpdateView.as_view()),
        name="barrio_pedania_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(BarrioPedaniaDeleteView.as_view()),
        name="barrio_pedania_delete"),

    url(r'^(?P<pk>\d+)/$',
        BarrioPedaniaDetailView.as_view(),
        name="barrio_pedania_detail"),

    url(r'^$',
        BarrioPedaniaListView.as_view(),
        name="barrio_pedania_list"),
]
