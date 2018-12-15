from django.conf.urls import url
from ..views import (CatalogoLuminariasListView, CatalogoLuminariasCreateView, CatalogoLuminariasDetailView,
                     CatalogoLuminariasUpdateView, CatalogoLuminariasDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(CatalogoLuminariasCreateView.as_view()),
        name="catalogo_luminarias_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(CatalogoLuminariasUpdateView.as_view()),
        name="catalogo_luminarias_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(CatalogoLuminariasDeleteView.as_view()),
        name="catalogo_luminarias_delete"),

    url(r'^(?P<pk>\d+)/$',
        CatalogoLuminariasDetailView.as_view(),
        name="catalogo_luminarias_detail"),

    url(r'^$',
        CatalogoLuminariasListView.as_view(),
        name="catalogo_luminarias_list"),
]
