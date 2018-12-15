from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import PuntoLuz
from ..forms import PuntoLuzForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class PuntoLuzListView(ListView):
    model = PuntoLuz
    template_name = "a_publico/punto_luz_list.html"
    paginate_by = 20
    context_object_name = "punto_luz_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(PuntoLuzListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PuntoLuzListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PuntoLuzListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(PuntoLuzListView, self).get_queryset()

    def get_allow_empty(self):
        return super(PuntoLuzListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(PuntoLuzListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(PuntoLuzListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(PuntoLuzListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(PuntoLuzListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(PuntoLuzListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(PuntoLuzListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PuntoLuzListView, self).get_template_names()


class PuntoLuzDetailView(DetailView):
    model = PuntoLuz
    template_name = "a_publico/punto_luz_detail.html"
    context_object_name = "punto_luz"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(PuntoLuzDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PuntoLuzDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PuntoLuzDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PuntoLuzDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(PuntoLuzDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(PuntoLuzDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PuntoLuzDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PuntoLuzDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PuntoLuzDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PuntoLuzDetailView, self).get_template_names()


class PuntoLuzCreateView(CreateView):
    model = PuntoLuz
    form_class = PuntoLuzForm
    # fields = ['codigopuntodeluz', 'codigosoporte', 'codigoluminaria', 'codigocuadro', 'codigocalle', 'numero', 'codigobarrio', 'implanterenovacion']
    template_name = "a_publico/punto_luz_create.html"
    success_url = reverse_lazy("punto_luz_list")

    def __init__(self, **kwargs):
        return super(PuntoLuzCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(PuntoLuzCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PuntoLuzCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PuntoLuzCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(PuntoLuzCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PuntoLuzCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PuntoLuzCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PuntoLuzCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(PuntoLuzCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PuntoLuzCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PuntoLuzCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(PuntoLuzCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PuntoLuzCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:punto_luz_detail", args=(self.object.pk,))


class PuntoLuzUpdateView(UpdateView):
    model = PuntoLuz
    form_class = PuntoLuzForm
    # fields = ['codigopuntodeluz', 'codigosoporte', 'codigoluminaria', 'codigocuadro', 'codigocalle', 'numero', 'codigobarrio', 'implanterenovacion']
    template_name = "a_publico/punto_luz_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "punto_luz"

    def __init__(self, **kwargs):
        return super(PuntoLuzUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PuntoLuzUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(PuntoLuzUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(PuntoLuzUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PuntoLuzUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(PuntoLuzUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(PuntoLuzUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(PuntoLuzUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(PuntoLuzUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(PuntoLuzUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(PuntoLuzUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(PuntoLuzUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(PuntoLuzUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PuntoLuzUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PuntoLuzUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PuntoLuzUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PuntoLuzUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:punto_luz_detail", args=(self.object.pk,))


class PuntoLuzDeleteView(DeleteView):
    model = PuntoLuz
    template_name = "a_publico/punto_luz_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "punto_luz"

    def __init__(self, **kwargs):
        return super(PuntoLuzDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(PuntoLuzDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(PuntoLuzDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(PuntoLuzDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(PuntoLuzDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(PuntoLuzDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(PuntoLuzDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(PuntoLuzDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(PuntoLuzDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(PuntoLuzDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(PuntoLuzDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:punto_luz_list")
