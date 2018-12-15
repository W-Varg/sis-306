from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import ViaPublica
from ..forms import ViaPublicaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class ViaPublicaListView(ListView):
    model = ViaPublica
    template_name = "a_publico/via_publica_list.html"
    paginate_by = 20
    context_object_name = "via_publica_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ViaPublicaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ViaPublicaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ViaPublicaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ViaPublicaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ViaPublicaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ViaPublicaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ViaPublicaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ViaPublicaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ViaPublicaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ViaPublicaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ViaPublicaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ViaPublicaListView, self).get_template_names()


class ViaPublicaDetailView(DetailView):
    model = ViaPublica
    template_name = "a_publico/via_publica_detail.html"
    context_object_name = "via_publica"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ViaPublicaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ViaPublicaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ViaPublicaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ViaPublicaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ViaPublicaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ViaPublicaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ViaPublicaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ViaPublicaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ViaPublicaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ViaPublicaDetailView, self).get_template_names()


class ViaPublicaCreateView(CreateView):
    model = ViaPublica
    form_class = ViaPublicaForm
    # fields = ['codigotipovia', 'nombretipovia']
    template_name = "a_publico/via_publica_create.html"
    success_url = reverse_lazy("via_publica_list")

    def __init__(self, **kwargs):
        return super(ViaPublicaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ViaPublicaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ViaPublicaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ViaPublicaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ViaPublicaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ViaPublicaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ViaPublicaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ViaPublicaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ViaPublicaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ViaPublicaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ViaPublicaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ViaPublicaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ViaPublicaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:via_publica_detail", args=(self.object.pk,))


class ViaPublicaUpdateView(UpdateView):
    model = ViaPublica
    form_class = ViaPublicaForm
    # fields = ['codigotipovia', 'nombretipovia']
    template_name = "a_publico/via_publica_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "via_publica"

    def __init__(self, **kwargs):
        return super(ViaPublicaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ViaPublicaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ViaPublicaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ViaPublicaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ViaPublicaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ViaPublicaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ViaPublicaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ViaPublicaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ViaPublicaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ViaPublicaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ViaPublicaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ViaPublicaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ViaPublicaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ViaPublicaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ViaPublicaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ViaPublicaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ViaPublicaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:via_publica_detail", args=(self.object.pk,))


class ViaPublicaDeleteView(DeleteView):
    model = ViaPublica
    template_name = "a_publico/via_publica_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "via_publica"

    def __init__(self, **kwargs):
        return super(ViaPublicaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ViaPublicaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ViaPublicaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ViaPublicaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ViaPublicaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ViaPublicaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ViaPublicaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ViaPublicaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ViaPublicaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ViaPublicaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ViaPublicaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:via_publica_list")
