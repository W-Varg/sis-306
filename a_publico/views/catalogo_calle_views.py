from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoCalle
from ..forms import CatalogoCalleForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoCalleListView(ListView):
    model = CatalogoCalle
    template_name = "a_publico/catalogo_calle_list.html"
    paginate_by = 20
    context_object_name = "catalogo_calle_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoCalleListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCalleListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCalleListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoCalleListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoCalleListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoCalleListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoCalleListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoCalleListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoCalleListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoCalleListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCalleListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCalleListView, self).get_template_names()


class CatalogoCalleDetailView(DetailView):
    model = CatalogoCalle
    template_name = "a_publico/catalogo_calle_detail.html"
    context_object_name = "catalogo_calle"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoCalleDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCalleDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCalleDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCalleDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCalleDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCalleDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCalleDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCalleDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCalleDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCalleDetailView, self).get_template_names()


class CatalogoCalleCreateView(CreateView):
    model = CatalogoCalle
    form_class = CatalogoCalleForm
    # fields = ['codigotipovia', 'nombrecalle']
    template_name = "a_publico/catalogo_calle_create.html"
    success_url = reverse_lazy("catalogo_calle_list")

    def __init__(self, **kwargs):
        return super(CatalogoCalleCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoCalleCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCalleCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoCalleCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoCalleCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoCalleCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoCalleCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoCalleCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoCalleCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoCalleCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCalleCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCalleCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCalleCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calle_detail", args=(self.object.pk,))


class CatalogoCalleUpdateView(UpdateView):
    model = CatalogoCalle
    form_class = CatalogoCalleForm
    # fields = ['codigotipovia', 'nombrecalle']
    template_name = "a_publico/catalogo_calle_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_calle"

    def __init__(self, **kwargs):
        return super(CatalogoCalleUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCalleUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCalleUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoCalleUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCalleUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCalleUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCalleUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoCalleUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoCalleUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoCalleUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoCalleUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoCalleUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoCalleUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCalleUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCalleUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCalleUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCalleUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calle_detail", args=(self.object.pk,))


class CatalogoCalleDeleteView(DeleteView):
    model = CatalogoCalle
    template_name = "a_publico/catalogo_calle_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_calle"

    def __init__(self, **kwargs):
        return super(CatalogoCalleDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCalleDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoCalleDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoCalleDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCalleDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCalleDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCalleDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCalleDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCalleDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCalleDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCalleDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calle_list")
