from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoLuminarias
from ..forms import CatalogoLuminariasForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoLuminariasListView(ListView):
    model = CatalogoLuminarias
    template_name = "a_publico/catalogo_luminarias_list.html"
    paginate_by = 20
    context_object_name = "catalogo_luminarias_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoLuminariasListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariasListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariasListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoLuminariasListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoLuminariasListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoLuminariasListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoLuminariasListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoLuminariasListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoLuminariasListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoLuminariasListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariasListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariasListView, self).get_template_names()


class CatalogoLuminariasDetailView(DetailView):
    model = CatalogoLuminarias
    template_name = "a_publico/catalogo_luminarias_detail.html"
    context_object_name = "catalogo_luminarias"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoLuminariasDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariasDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariasDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariasDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariasDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariasDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariasDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariasDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariasDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariasDetailView, self).get_template_names()


class CatalogoLuminariasCreateView(CreateView):
    model = CatalogoLuminarias
    form_class = CatalogoLuminariasForm
    # fields = ['codigoluminaria', 'nombreluminaria', 'pvp', 'amortizacion', 'actualprecio', 'codigolampara']
    template_name = "a_publico/catalogo_luminarias_create.html"
    success_url = reverse_lazy("catalogo_luminarias_list")

    def __init__(self, **kwargs):
        return super(CatalogoLuminariasCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoLuminariasCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariasCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariasCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoLuminariasCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLuminariasCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLuminariasCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLuminariasCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLuminariasCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLuminariasCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariasCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariasCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariasCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminarias_detail", args=(self.object.pk,))


class CatalogoLuminariasUpdateView(UpdateView):
    model = CatalogoLuminarias
    form_class = CatalogoLuminariasForm
    # fields = ['codigoluminaria', 'nombreluminaria', 'pvp', 'amortizacion', 'actualprecio', 'codigolampara']
    template_name = "a_publico/catalogo_luminarias_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_luminarias"

    def __init__(self, **kwargs):
        return super(CatalogoLuminariasUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariasUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariasUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariasUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariasUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariasUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariasUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoLuminariasUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLuminariasUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLuminariasUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLuminariasUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLuminariasUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLuminariasUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariasUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariasUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariasUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariasUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminarias_detail", args=(self.object.pk,))


class CatalogoLuminariasDeleteView(DeleteView):
    model = CatalogoLuminarias
    template_name = "a_publico/catalogo_luminarias_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_luminarias"

    def __init__(self, **kwargs):
        return super(CatalogoLuminariasDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariasDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariasDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoLuminariasDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariasDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariasDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariasDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariasDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariasDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariasDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariasDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminarias_list")
