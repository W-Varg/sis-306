from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import EquiposMedida
from ..forms import EquiposMedidaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class EquiposMedidaListView(ListView):
    model = EquiposMedida
    template_name = "a_publico/equipos_medida_list.html"
    paginate_by = 20
    context_object_name = "equipos_medida_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(EquiposMedidaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EquiposMedidaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EquiposMedidaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(EquiposMedidaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(EquiposMedidaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(EquiposMedidaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(EquiposMedidaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(EquiposMedidaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(EquiposMedidaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(EquiposMedidaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(EquiposMedidaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EquiposMedidaListView, self).get_template_names()


class EquiposMedidaDetailView(DetailView):
    model = EquiposMedida
    template_name = "a_publico/equipos_medida_detail.html"
    context_object_name = "equipos_medida"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(EquiposMedidaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EquiposMedidaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EquiposMedidaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EquiposMedidaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(EquiposMedidaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(EquiposMedidaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(EquiposMedidaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EquiposMedidaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EquiposMedidaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EquiposMedidaDetailView, self).get_template_names()


class EquiposMedidaCreateView(CreateView):
    model = EquiposMedida
    form_class = EquiposMedidaForm
    # fields = ['codigoidentificacion', 'codigocalle', 'numero', 'codigobarrio', 'kwcontrato', 'numeroactiva', 'numeroreactiva', 'monofasico', 'lecturadirecta', 'lecturaindirecta']
    template_name = "a_publico/equipos_medida_create.html"
    success_url = reverse_lazy("equipos_medida_list")

    def __init__(self, **kwargs):
        return super(EquiposMedidaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(EquiposMedidaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EquiposMedidaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EquiposMedidaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(EquiposMedidaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EquiposMedidaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EquiposMedidaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EquiposMedidaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(EquiposMedidaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EquiposMedidaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EquiposMedidaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(EquiposMedidaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EquiposMedidaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:equipos_medida_detail", args=(self.object.pk,))


class EquiposMedidaUpdateView(UpdateView):
    model = EquiposMedida
    form_class = EquiposMedidaForm
    # fields = ['codigoidentificacion', 'codigocalle', 'numero', 'codigobarrio', 'kwcontrato', 'numeroactiva', 'numeroreactiva', 'monofasico', 'lecturadirecta', 'lecturaindirecta']
    template_name = "a_publico/equipos_medida_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "equipos_medida"

    def __init__(self, **kwargs):
        return super(EquiposMedidaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EquiposMedidaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(EquiposMedidaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(EquiposMedidaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EquiposMedidaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(EquiposMedidaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(EquiposMedidaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(EquiposMedidaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(EquiposMedidaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(EquiposMedidaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(EquiposMedidaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(EquiposMedidaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(EquiposMedidaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(EquiposMedidaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EquiposMedidaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EquiposMedidaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EquiposMedidaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:equipos_medida_detail", args=(self.object.pk,))


class EquiposMedidaDeleteView(DeleteView):
    model = EquiposMedida
    template_name = "a_publico/equipos_medida_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "equipos_medida"

    def __init__(self, **kwargs):
        return super(EquiposMedidaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(EquiposMedidaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(EquiposMedidaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(EquiposMedidaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(EquiposMedidaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(EquiposMedidaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(EquiposMedidaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(EquiposMedidaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(EquiposMedidaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(EquiposMedidaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(EquiposMedidaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:equipos_medida_list")
