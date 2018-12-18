
from .barrio_pedania_views import *  # NOQA
from .via_publica_views import *  # NOQA
from .catalogo_calle_views import *  # NOQA
from .catalogo_lampara_views import *  # NOQA
from .catalogo_luminaria_views import *  # NOQA
from .catalogo_soporte_views import *  # NOQA
from .equipos_medida_views import *  # NOQA
from .cuadro_mando_views import *  # NOQA
from .punto_luz_views import *  # NOQA
from django.shortcuts import render

from ..models import PuntoLuz

def index(request):
    list_luz = PuntoLuz.objects.order_by('-implanterenovacion')
    context = {'puntos_luz':list_luz}
    return render(request, 'index.html',context)