from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import BarrioPedania
from ..forms import BarrioPedaniaForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class BarrioPedaniaListView(ListView):
    model = BarrioPedania
    template_name = "a_publico/barrio_pedania_list.html"
    paginate_by = 20
    context_object_name = "barrio_pedania_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(BarrioPedaniaListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BarrioPedaniaListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BarrioPedaniaListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(BarrioPedaniaListView, self).get_queryset()

    def get_allow_empty(self):
        return super(BarrioPedaniaListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(BarrioPedaniaListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(BarrioPedaniaListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(BarrioPedaniaListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(BarrioPedaniaListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(BarrioPedaniaListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(BarrioPedaniaListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BarrioPedaniaListView, self).get_template_names()


class BarrioPedaniaDetailView(DetailView):
    model = BarrioPedania
    template_name = "a_publico/barrio_pedania_detail.html"
    context_object_name = "barrio_pedania"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(BarrioPedaniaDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BarrioPedaniaDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BarrioPedaniaDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BarrioPedaniaDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(BarrioPedaniaDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(BarrioPedaniaDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(BarrioPedaniaDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BarrioPedaniaDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BarrioPedaniaDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BarrioPedaniaDetailView, self).get_template_names()


class BarrioPedaniaCreateView(CreateView):
    model = BarrioPedania
    form_class = BarrioPedaniaForm
    # fields = ['nombrebarrio']
    template_name = "a_publico/barrio_pedania_create.html"
    success_url = reverse_lazy("barrio_pedania_list")

    def __init__(self, **kwargs):
        return super(BarrioPedaniaCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(BarrioPedaniaCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BarrioPedaniaCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(BarrioPedaniaCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(BarrioPedaniaCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(BarrioPedaniaCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(BarrioPedaniaCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(BarrioPedaniaCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(BarrioPedaniaCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(BarrioPedaniaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(BarrioPedaniaCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(BarrioPedaniaCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BarrioPedaniaCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:barrio_pedania_detail", args=(self.object.pk,))


class BarrioPedaniaUpdateView(UpdateView):
    model = BarrioPedania
    form_class = BarrioPedaniaForm
    # fields = ['nombrebarrio']
    template_name = "a_publico/barrio_pedania_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "barrio_pedania"

    def __init__(self, **kwargs):
        return super(BarrioPedaniaUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BarrioPedaniaUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BarrioPedaniaUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(BarrioPedaniaUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BarrioPedaniaUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(BarrioPedaniaUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(BarrioPedaniaUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(BarrioPedaniaUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(BarrioPedaniaUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(BarrioPedaniaUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(BarrioPedaniaUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(BarrioPedaniaUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(BarrioPedaniaUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(BarrioPedaniaUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BarrioPedaniaUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BarrioPedaniaUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BarrioPedaniaUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:barrio_pedania_detail", args=(self.object.pk,))


class BarrioPedaniaDeleteView(DeleteView):
    model = BarrioPedania
    template_name = "a_publico/barrio_pedania_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "barrio_pedania"

    def __init__(self, **kwargs):
        return super(BarrioPedaniaDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BarrioPedaniaDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(BarrioPedaniaDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(BarrioPedaniaDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BarrioPedaniaDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(BarrioPedaniaDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(BarrioPedaniaDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(BarrioPedaniaDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BarrioPedaniaDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BarrioPedaniaDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BarrioPedaniaDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("a_publico:barrio_pedania_list")
