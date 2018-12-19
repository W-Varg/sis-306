
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

from ..models import PuntoLuz, CuadroMando, CatalogoLampara, BarrioPedania

def index(request):
    list_luz = PuntoLuz.objects.order_by('-implanterenovacion')
    context = {'puntos_luz':list_luz}
    return render(request, 'index.html',context)

def inf_mando(request):
    list_r = CuadroMando.objects.select_related('codigocalle','codigobarrio','codigocalle__codigotipovia').order_by('codigobarrio__nombrebarrio')
    # list_total = Registry.objects.count()
    context = {'list_cuadro' : list_r}
    return render(request, 'inf_cuadro.html',context)

def inf_lampara(request):
    lam_r = PuntoLuz.objects.select_related('codigocalle','codigobarrio', 'codigoluminaria','codigoluminaria__codigolampara','codigocalle__codigotipovia','codigocuadro').order_by('codigocuadro__codigoindentificacion')
    context = {'lamparas' : lam_r}
    return render(request,'inf_lampara.html',context)
