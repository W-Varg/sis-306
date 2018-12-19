
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
    # id_tarjeta = Tarjeta.objects.filter(number=code).values_list('id', flat=True)
    # if id_tarjeta:
    #     id_usuario = Persona.objects.filter(tarjetas_id=id_tarjeta[0]).values_list('id', flat=True)
        
    #     if id_usuario:
    #         registro = Registry()
    #         registro.user_name = Persona.objects.get(pk=id_usuario[0])
    #         registro.tarjeta = code
    #         registro.save()
    #         msg = 'Registro Exitoso: '+code
    #         alarma(2300,1000)
    #         status = True
    
    list_r = CuadroMando.objects.prefetch_related('codigocalle__barriopedania')
    # list_total = Registry.objects.count()

    context = {'list_cuadro' : list_r}
    return render(request,'inf_cuadro.html',context)

def inf_lampara(request):
    context = {'lamparas' : 'lam'}
    return render(request,'inf_lampara.html',context)
