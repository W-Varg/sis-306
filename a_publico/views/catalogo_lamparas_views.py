from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoLamparas
from ..forms import CatalogoLamparasForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoLamparasListView(ListView):
    model = CatalogoLamparas
    template_name = "a_publico/catalogo_lamparas_list.html"
    paginate_by = 20
    context_object_name = "catalogo_lamparas_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoLamparasListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparasListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparasListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoLamparasListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoLamparasListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoLamparasListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoLamparasListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoLamparasListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoLamparasListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoLamparasListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparasListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparasListView, self).get_template_names()


class CatalogoLamparasDetailView(DetailView):
    model = CatalogoLamparas
    template_name = "a_publico/catalogo_lamparas_detail.html"
    context_object_name = "catalogo_lamparas"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoLamparasDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparasDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparasDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparasDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparasDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparasDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparasDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparasDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparasDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparasDetailView, self).get_template_names()


class CatalogoLamparasCreateView(CreateView):
    model = CatalogoLamparas
    form_class = CatalogoLamparasForm
    # fields = ['codigolampara', 'nombrelampara', 'pvp', 'amortizacion', 'actualprecio']
    template_name = "a_publico/catalogo_lamparas_create.html"
    success_url = reverse_lazy("catalogo_lamparas_list")

    def __init__(self, **kwargs):
        return super(CatalogoLamparasCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoLamparasCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparasCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparasCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoLamparasCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLamparasCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLamparasCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLamparasCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLamparasCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLamparasCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparasCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparasCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparasCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lamparas_detail", args=(self.object.pk,))


class CatalogoLamparasUpdateView(UpdateView):
    model = CatalogoLamparas
    form_class = CatalogoLamparasForm
    # fields = ['codigolampara', 'nombrelampara', 'pvp', 'amortizacion', 'actualprecio']
    template_name = "a_publico/catalogo_lamparas_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_lamparas"

    def __init__(self, **kwargs):
        return super(CatalogoLamparasUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparasUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparasUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparasUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparasUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparasUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparasUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoLamparasUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLamparasUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLamparasUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLamparasUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLamparasUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLamparasUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparasUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparasUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparasUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparasUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lamparas_detail", args=(self.object.pk,))


class CatalogoLamparasDeleteView(DeleteView):
    model = CatalogoLamparas
    template_name = "a_publico/catalogo_lamparas_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_lamparas"

    def __init__(self, **kwargs):
        return super(CatalogoLamparasDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparasDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparasDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoLamparasDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparasDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparasDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparasDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparasDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparasDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparasDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparasDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lamparas_list")
