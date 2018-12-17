from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoSoporte
from ..forms import CatalogoSoporteForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoSoporteListView(ListView):
    model = CatalogoSoporte
    template_name = "a_publico/catalogo_soporte_list.html"
    paginate_by = 20
    context_object_name = "catalogo_soporte_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoSoporteListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoSoporteListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoSoporteListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoSoporteListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoSoporteListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoSoporteListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoSoporteListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoSoporteListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoSoporteListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoSoporteListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoSoporteListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoSoporteListView, self).get_template_names()


class CatalogoSoporteDetailView(DetailView):
    model = CatalogoSoporte
    template_name = "a_publico/catalogo_soporte_detail.html"
    context_object_name = "catalogo_soporte"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoSoporteDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoSoporteDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoSoporteDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoSoporteDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoSoporteDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoSoporteDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoSoporteDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoSoporteDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoSoporteDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoSoporteDetailView, self).get_template_names()


class CatalogoSoporteCreateView(CreateView):
    model = CatalogoSoporte
    form_class = CatalogoSoporteForm
    # fields = ['nombresoporte', 'pvp', 'amortizacion']
    template_name = "a_publico/catalogo_soporte_create.html"
    success_url = reverse_lazy("catalogo_soporte_list")

    def __init__(self, **kwargs):
        return super(CatalogoSoporteCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoSoporteCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoSoporteCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoSoporteCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoSoporteCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoSoporteCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoSoporteCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoSoporteCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoSoporteCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoSoporteCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoSoporteCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoSoporteCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoSoporteCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_soporte_detail", args=(self.object.pk,))


class CatalogoSoporteUpdateView(UpdateView):
    model = CatalogoSoporte
    form_class = CatalogoSoporteForm
    # fields = ['nombresoporte', 'pvp', 'amortizacion']
    template_name = "a_publico/catalogo_soporte_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_soporte"

    def __init__(self, **kwargs):
        return super(CatalogoSoporteUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoSoporteUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoSoporteUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoSoporteUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoSoporteUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoSoporteUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoSoporteUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoSoporteUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoSoporteUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoSoporteUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoSoporteUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoSoporteUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoSoporteUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoSoporteUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoSoporteUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoSoporteUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoSoporteUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_soporte_detail", args=(self.object.pk,))


class CatalogoSoporteDeleteView(DeleteView):
    model = CatalogoSoporte
    template_name = "a_publico/catalogo_soporte_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_soporte"

    def __init__(self, **kwargs):
        return super(CatalogoSoporteDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoSoporteDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoSoporteDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoSoporteDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoSoporteDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoSoporteDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoSoporteDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoSoporteDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoSoporteDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoSoporteDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoSoporteDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_soporte_list")
