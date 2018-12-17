from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import CatalogoLampara
from ..forms import CatalogoLamparaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class CatalogoLamparaListView(ListView):
    model = CatalogoLampara
    template_name = "a_publico/catalogo_lampara_list.html"
    paginate_by = 20
    context_object_name = "catalogo_lampara_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(CatalogoLamparaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(CatalogoLamparaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(CatalogoLamparaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(CatalogoLamparaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(CatalogoLamparaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(CatalogoLamparaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(CatalogoLamparaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(CatalogoLamparaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparaListView, self).get_template_names()


class CatalogoLamparaDetailView(DetailView):
    model = CatalogoLampara
    template_name = "a_publico/catalogo_lampara_detail.html"
    context_object_name = "catalogo_lampara"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(CatalogoLamparaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparaDetailView, self).get_template_names()


class CatalogoLamparaCreateView(CreateView):
    model = CatalogoLampara
    form_class = CatalogoLamparaForm
    # fields = ['nombrelampara', 'pvp', 'amortizacion']
    template_name = "a_publico/catalogo_lampara_create.html"
    success_url = reverse_lazy("catalogo_lampara_list")

    def __init__(self, **kwargs):
        return super(CatalogoLamparaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(CatalogoLamparaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(CatalogoLamparaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLamparaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLamparaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLamparaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLamparaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLamparaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lampara_detail", args=(self.object.pk,))


class CatalogoLamparaUpdateView(UpdateView):
    model = CatalogoLampara
    form_class = CatalogoLamparaForm
    # fields = ['nombrelampara', 'pvp', 'amortizacion']
    template_name = "a_publico/catalogo_lampara_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_lampara"

    def __init__(self, **kwargs):
        return super(CatalogoLamparaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CatalogoLamparaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CatalogoLamparaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CatalogoLamparaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CatalogoLamparaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CatalogoLamparaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CatalogoLamparaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(CatalogoLamparaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lampara_detail", args=(self.object.pk,))


class CatalogoLamparaDeleteView(DeleteView):
    model = CatalogoLampara
    template_name = "a_publico/catalogo_lampara_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "catalogo_lampara"

    def __init__(self, **kwargs):
        return super(CatalogoLamparaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CatalogoLamparaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(CatalogoLamparaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CatalogoLamparaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CatalogoLamparaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CatalogoLamparaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CatalogoLamparaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CatalogoLamparaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CatalogoLamparaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CatalogoLamparaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CatalogoLamparaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:catalogo_lampara_list")
