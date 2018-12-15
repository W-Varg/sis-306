from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoCalles
from ..forms import CatalogoCallesForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoCallesListView(ListView):
    model = CatalogoCalles
    template_name = "a_publico/catalogo_calles_list.html"
    paginate_by = 20
    context_object_name = "catalogo_calles_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoCallesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCallesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCallesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoCallesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoCallesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoCallesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoCallesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoCallesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoCallesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoCallesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCallesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCallesListView, self).get_template_names()


class CatalogoCallesDetailView(DetailView):
    model = CatalogoCalles
    template_name = "a_publico/catalogo_calles_detail.html"
    context_object_name = "catalogo_calles"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoCallesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCallesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCallesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCallesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCallesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCallesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCallesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCallesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCallesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCallesDetailView, self).get_template_names()


class CatalogoCallesCreateView(CreateView):
    model = CatalogoCalles
    form_class = CatalogoCallesForm
    # fields = ['codigocalle', 'codigotipovia', 'nombrecalle']
    template_name = "a_publico/catalogo_calles_create.html"
    success_url = reverse_lazy("catalogo_calles_list")

    def __init__(self, **kwargs):
        return super(CatalogoCallesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoCallesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCallesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoCallesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoCallesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoCallesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoCallesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoCallesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoCallesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoCallesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCallesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCallesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCallesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calles_detail", args=(self.object.pk,))


class CatalogoCallesUpdateView(UpdateView):
    model = CatalogoCalles
    form_class = CatalogoCallesForm
    # fields = ['codigocalle', 'codigotipovia', 'nombrecalle']
    template_name = "a_publico/catalogo_calles_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_calles"

    def __init__(self, **kwargs):
        return super(CatalogoCallesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCallesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoCallesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoCallesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCallesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCallesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCallesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoCallesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoCallesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoCallesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoCallesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoCallesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoCallesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCallesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCallesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCallesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCallesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calles_detail", args=(self.object.pk,))


class CatalogoCallesDeleteView(DeleteView):
    model = CatalogoCalles
    template_name = "a_publico/catalogo_calles_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_calles"

    def __init__(self, **kwargs):
        return super(CatalogoCallesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoCallesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoCallesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoCallesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoCallesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoCallesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoCallesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoCallesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoCallesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoCallesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoCallesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_calles_list")
