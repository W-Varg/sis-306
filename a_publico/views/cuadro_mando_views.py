from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CuadroMando
from ..forms import CuadroMandoForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CuadroMandoListView(ListView):
    model = CuadroMando
    template_name = "a_publico/cuadro_mando_list.html"
    paginate_by = 20
    context_object_name = "cuadro_mando_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CuadroMandoListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CuadroMandoListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CuadroMandoListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CuadroMandoListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CuadroMandoListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CuadroMandoListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CuadroMandoListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CuadroMandoListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CuadroMandoListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CuadroMandoListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CuadroMandoListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CuadroMandoListView, self).get_template_names()


class CuadroMandoDetailView(DetailView):
    model = CuadroMando
    template_name = "a_publico/cuadro_mando_detail.html"
    context_object_name = "cuadro_mando"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CuadroMandoDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CuadroMandoDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CuadroMandoDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CuadroMandoDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CuadroMandoDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CuadroMandoDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CuadroMandoDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CuadroMandoDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CuadroMandoDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CuadroMandoDetailView, self).get_template_names()


class CuadroMandoCreateView(CreateView):
    model = CuadroMando
    form_class = CuadroMandoForm
    # fields = ['codigoindentificacion', 'codigocontadores', 'codigocalle', 'numero', 'codigobarrio', 'tipocuadro', 'salidasutilizadas', 'mgtentrada', 'fachada', 'alimentacionfn', 'alimentacion3fn']
    template_name = "a_publico/cuadro_mando_create.html"
    success_url = reverse_lazy("cuadro_mando_list")

    def __init__(self, **kwargs):
        return super(CuadroMandoCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CuadroMandoCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CuadroMandoCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CuadroMandoCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CuadroMandoCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CuadroMandoCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CuadroMandoCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CuadroMandoCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CuadroMandoCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CuadroMandoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CuadroMandoCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CuadroMandoCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CuadroMandoCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:cuadro_mando_detail", args=(self.object.pk,))


class CuadroMandoUpdateView(UpdateView):
    model = CuadroMando
    form_class = CuadroMandoForm
    # fields = ['codigoindentificacion', 'codigocontadores', 'codigocalle', 'numero', 'codigobarrio', 'tipocuadro', 'salidasutilizadas', 'mgtentrada', 'fachada', 'alimentacionfn', 'alimentacion3fn']
    template_name = "a_publico/cuadro_mando_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "cuadro_mando"

    def __init__(self, **kwargs):
        return super(CuadroMandoUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CuadroMandoUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CuadroMandoUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CuadroMandoUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CuadroMandoUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CuadroMandoUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CuadroMandoUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CuadroMandoUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CuadroMandoUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CuadroMandoUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CuadroMandoUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CuadroMandoUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CuadroMandoUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CuadroMandoUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CuadroMandoUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CuadroMandoUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CuadroMandoUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:cuadro_mando_detail", args=(self.object.pk,))


class CuadroMandoDeleteView(DeleteView):
    model = CuadroMando
    template_name = "a_publico/cuadro_mando_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "cuadro_mando"

    def __init__(self, **kwargs):
        return super(CuadroMandoDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CuadroMandoDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CuadroMandoDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CuadroMandoDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CuadroMandoDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CuadroMandoDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CuadroMandoDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CuadroMandoDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CuadroMandoDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CuadroMandoDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CuadroMandoDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:cuadro_mando_list")
