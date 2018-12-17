from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoLuminaria
from ..forms import CatalogoLuminariaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoLuminariaListView(ListView):
    model = CatalogoLuminaria
    template_name = "a_publico/catalogo_luminaria_list.html"
    paginate_by = 20
    context_object_name = "catalogo_luminaria_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoLuminariaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoLuminariaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoLuminariaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoLuminariaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoLuminariaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoLuminariaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoLuminariaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoLuminariaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariaListView, self).get_template_names()


class CatalogoLuminariaDetailView(DetailView):
    model = CatalogoLuminaria
    template_name = "a_publico/catalogo_luminaria_detail.html"
    context_object_name = "catalogo_luminaria"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoLuminariaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariaDetailView, self).get_template_names()


class CatalogoLuminariaCreateView(CreateView):
    model = CatalogoLuminaria
    form_class = CatalogoLuminariaForm
    # fields = ['nombreluminaria', 'pvp', 'amortizacion', 'codigolampara']
    template_name = "a_publico/catalogo_luminaria_create.html"
    success_url = reverse_lazy("catalogo_luminaria_list")

    def __init__(self, **kwargs):
        return super(CatalogoLuminariaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoLuminariaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoLuminariaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLuminariaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLuminariaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLuminariaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLuminariaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLuminariaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminaria_detail", args=(self.object.pk,))


class CatalogoLuminariaUpdateView(UpdateView):
    model = CatalogoLuminaria
    form_class = CatalogoLuminariaForm
    # fields = ['nombreluminaria', 'pvp', 'amortizacion', 'codigolampara']
    template_name = "a_publico/catalogo_luminaria_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_luminaria"

    def __init__(self, **kwargs):
        return super(CatalogoLuminariaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLuminariaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoLuminariaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLuminariaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLuminariaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLuminariaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLuminariaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLuminariaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminaria_detail", args=(self.object.pk,))


class CatalogoLuminariaDeleteView(DeleteView):
    model = CatalogoLuminaria
    template_name = "a_publico/catalogo_luminaria_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_luminaria"

    def __init__(self, **kwargs):
        return super(CatalogoLuminariaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLuminariaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoLuminariaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoLuminariaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLuminariaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLuminariaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLuminariaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLuminariaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLuminariaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLuminariaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLuminariaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_luminaria_list")
