
from .barrio_pedania_views import *  # NOQA
from .catalogo_calles_views import *  # NOQA
from .catalogo_lamparas_views import *  # NOQA
from .catalogo_luminarias_views import *  # NOQA
from .catalogo_soportes_views import *  # NOQA
from .cuadro_mando_views import *  # NOQA
from .equipos_medida_views import *  # NOQA
from .punto_luz_views import *  # NOQA
from .via_publica_views import *  # NOQA
from django.shortcuts import render

from ..models import PuntoLuz

def index(request):
    list_luz = PuntoLuz.objects.order_by('-implanterenovacion')[:5]
    context = {'puntos_luz':list_luz}
    return render(request, 'index.html',context)