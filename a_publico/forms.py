from django import forms
from .models import BarrioPedania, ViaPublica, CatalogoCalle, CatalogoLampara, CatalogoLuminaria, CatalogoSoporte, EquiposMedida, CuadroMando, PuntoLuz


class BarrioPedaniaForm(forms.ModelForm):

    class Meta:
        model = BarrioPedania
        fields = ['nombrebarrio']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(BarrioPedaniaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(BarrioPedaniaForm, self).is_valid()

    def full_clean(self):
        return super(BarrioPedaniaForm, self).full_clean()

    def clean_nombrebarrio(self):
        nombrebarrio = self.cleaned_data.get("nombrebarrio", None)
        return nombrebarrio

    def clean(self):
        return super(BarrioPedaniaForm, self).clean()

    def validate_unique(self):
        return super(BarrioPedaniaForm, self).validate_unique()

    def save(self, commit=True):
        return super(BarrioPedaniaForm, self).save(commit)


class ViaPublicaForm(forms.ModelForm):

    class Meta:
        model = ViaPublica
        fields = ['nombretipovia']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(ViaPublicaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(ViaPublicaForm, self).is_valid()

    def full_clean(self):
        return super(ViaPublicaForm, self).full_clean()

    def clean_nombretipovia(self):
        nombretipovia = self.cleaned_data.get("nombretipovia", None)
        return nombretipovia

    def clean(self):
        return super(ViaPublicaForm, self).clean()

    def validate_unique(self):
        return super(ViaPublicaForm, self).validate_unique()

    def save(self, commit=True):
        return super(ViaPublicaForm, self).save(commit)


class CatalogoCalleForm(forms.ModelForm):

    class Meta:
        model = CatalogoCalle
        fields = ['codigotipovia', 'nombrecalle']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CatalogoCalleForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CatalogoCalleForm, self).is_valid()

    def full_clean(self):
        return super(CatalogoCalleForm, self).full_clean()

    def clean_codigotipovia(self):
        codigotipovia = self.cleaned_data.get("codigotipovia", None)
        return codigotipovia

    def clean_nombrecalle(self):
        nombrecalle = self.cleaned_data.get("nombrecalle", None)
        return nombrecalle

    def clean(self):
        return super(CatalogoCalleForm, self).clean()

    def validate_unique(self):
        return super(CatalogoCalleForm, self).validate_unique()

    def save(self, commit=True):
        return super(CatalogoCalleForm, self).save(commit)


class CatalogoLamparaForm(forms.ModelForm):

    class Meta:
        model = CatalogoLampara
        fields = ['nombrelampara', 'pvp', 'amortizacion']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CatalogoLamparaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CatalogoLamparaForm, self).is_valid()

    def full_clean(self):
        return super(CatalogoLamparaForm, self).full_clean()

    def clean_nombrelampara(self):
        nombrelampara = self.cleaned_data.get("nombrelampara", None)
        return nombrelampara

    def clean_pvp(self):
        pvp = self.cleaned_data.get("pvp", None)
        return pvp

    def clean_amortizacion(self):
        amortizacion = self.cleaned_data.get("amortizacion", None)
        return amortizacion

    def clean(self):
        return super(CatalogoLamparaForm, self).clean()

    def validate_unique(self):
        return super(CatalogoLamparaForm, self).validate_unique()

    def save(self, commit=True):
        return super(CatalogoLamparaForm, self).save(commit)


class CatalogoLuminariaForm(forms.ModelForm):

    class Meta:
        model = CatalogoLuminaria
        fields = ['nombreluminaria', 'pvp', 'amortizacion', 'codigolampara']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CatalogoLuminariaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CatalogoLuminariaForm, self).is_valid()

    def full_clean(self):
        return super(CatalogoLuminariaForm, self).full_clean()

    def clean_nombreluminaria(self):
        nombreluminaria = self.cleaned_data.get("nombreluminaria", None)
        return nombreluminaria

    def clean_pvp(self):
        pvp = self.cleaned_data.get("pvp", None)
        return pvp

    def clean_amortizacion(self):
        amortizacion = self.cleaned_data.get("amortizacion", None)
        return amortizacion

    def clean_codigolampara(self):
        codigolampara = self.cleaned_data.get("codigolampara", None)
        return codigolampara

    def clean(self):
        return super(CatalogoLuminariaForm, self).clean()

    def validate_unique(self):
        return super(CatalogoLuminariaForm, self).validate_unique()

    def save(self, commit=True):
        return super(CatalogoLuminariaForm, self).save(commit)


class CatalogoSoporteForm(forms.ModelForm):

    class Meta:
        model = CatalogoSoporte
        fields = ['nombresoporte', 'pvp', 'amortizacion']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CatalogoSoporteForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CatalogoSoporteForm, self).is_valid()

    def full_clean(self):
        return super(CatalogoSoporteForm, self).full_clean()

    def clean_nombresoporte(self):
        nombresoporte = self.cleaned_data.get("nombresoporte", None)
        return nombresoporte

    def clean_pvp(self):
        pvp = self.cleaned_data.get("pvp", None)
        return pvp

    def clean_amortizacion(self):
        amortizacion = self.cleaned_data.get("amortizacion", None)
        return amortizacion

    def clean(self):
        return super(CatalogoSoporteForm, self).clean()

    def validate_unique(self):
        return super(CatalogoSoporteForm, self).validate_unique()

    def save(self, commit=True):
        return super(CatalogoSoporteForm, self).save(commit)


class EquiposMedidaForm(forms.ModelForm):

    class Meta:
        model = EquiposMedida
        fields = ['codigoidentificacion', 'codigocalle', 'numero', 'codigobarrio', 'kwcontrato', 'numeroactiva', 'numeroreactiva', 'monofasico', 'lecturadirecta', 'lecturaindirecta']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(EquiposMedidaForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(EquiposMedidaForm, self).is_valid()

    def full_clean(self):
        return super(EquiposMedidaForm, self).full_clean()

    def clean_codigoidentificacion(self):
        codigoidentificacion = self.cleaned_data.get("codigoidentificacion", None)
        return codigoidentificacion

    def clean_codigocalle(self):
        codigocalle = self.cleaned_data.get("codigocalle", None)
        return codigocalle

    def clean_numero(self):
        numero = self.cleaned_data.get("numero", None)
        return numero

    def clean_codigobarrio(self):
        codigobarrio = self.cleaned_data.get("codigobarrio", None)
        return codigobarrio

    def clean_kwcontrato(self):
        kwcontrato = self.cleaned_data.get("kwcontrato", None)
        return kwcontrato

    def clean_numeroactiva(self):
        numeroactiva = self.cleaned_data.get("numeroactiva", None)
        return numeroactiva

    def clean_numeroreactiva(self):
        numeroreactiva = self.cleaned_data.get("numeroreactiva", None)
        return numeroreactiva

    def clean_monofasico(self):
        monofasico = self.cleaned_data.get("monofasico", None)
        return monofasico

    def clean_lecturadirecta(self):
        lecturadirecta = self.cleaned_data.get("lecturadirecta", None)
        return lecturadirecta

    def clean_lecturaindirecta(self):
        lecturaindirecta = self.cleaned_data.get("lecturaindirecta", None)
        return lecturaindirecta

    def clean(self):
        return super(EquiposMedidaForm, self).clean()

    def validate_unique(self):
        return super(EquiposMedidaForm, self).validate_unique()

    def save(self, commit=True):
        return super(EquiposMedidaForm, self).save(commit)


class CuadroMandoForm(forms.ModelForm):

    class Meta:
        model = CuadroMando
        fields = ['codigoindentificacion', 'codigocontadores', 'codigocalle', 'numero', 'codigobarrio', 'tipocuadro', 'salidasutilizadas', 'mgtentrada', 'fachada', 'alimentacionfn', 'alimentacion3fn']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(CuadroMandoForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CuadroMandoForm, self).is_valid()

    def full_clean(self):
        return super(CuadroMandoForm, self).full_clean()

    def clean_codigoindentificacion(self):
        codigoindentificacion = self.cleaned_data.get("codigoindentificacion", None)
        return codigoindentificacion

    def clean_codigocontadores(self):
        codigocontadores = self.cleaned_data.get("codigocontadores", None)
        return codigocontadores

    def clean_codigocalle(self):
        codigocalle = self.cleaned_data.get("codigocalle", None)
        return codigocalle

    def clean_numero(self):
        numero = self.cleaned_data.get("numero", None)
        return numero

    def clean_codigobarrio(self):
        codigobarrio = self.cleaned_data.get("codigobarrio", None)
        return codigobarrio

    def clean_tipocuadro(self):
        tipocuadro = self.cleaned_data.get("tipocuadro", None)
        return tipocuadro

    def clean_salidasutilizadas(self):
        salidasutilizadas = self.cleaned_data.get("salidasutilizadas", None)
        return salidasutilizadas

    def clean_mgtentrada(self):
        mgtentrada = self.cleaned_data.get("mgtentrada", None)
        return mgtentrada

    def clean_fachada(self):
        fachada = self.cleaned_data.get("fachada", None)
        return fachada

    def clean_alimentacionfn(self):
        alimentacionfn = self.cleaned_data.get("alimentacionfn", None)
        return alimentacionfn

    def clean_alimentacion3fn(self):
        alimentacion3fn = self.cleaned_data.get("alimentacion3fn", None)
        return alimentacion3fn

    def clean(self):
        return super(CuadroMandoForm, self).clean()

    def validate_unique(self):
        return super(CuadroMandoForm, self).validate_unique()

    def save(self, commit=True):
        return super(CuadroMandoForm, self).save(commit)


class PuntoLuzForm(forms.ModelForm):

    class Meta:
        model = PuntoLuz
        fields = ['codigosoporte', 'codigoluminaria', 'codigocuadro', 'codigocalle', 'numero', 'codigobarrio', 'lat', 'lng']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(PuntoLuzForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(PuntoLuzForm, self).is_valid()

    def full_clean(self):
        return super(PuntoLuzForm, self).full_clean()

    def clean_codigosoporte(self):
        codigosoporte = self.cleaned_data.get("codigosoporte", None)
        return codigosoporte

    def clean_codigoluminaria(self):
        codigoluminaria = self.cleaned_data.get("codigoluminaria", None)
        return codigoluminaria

    def clean_codigocuadro(self):
        codigocuadro = self.cleaned_data.get("codigocuadro", None)
        return codigocuadro

    def clean_codigocalle(self):
        codigocalle = self.cleaned_data.get("codigocalle", None)
        return codigocalle

    def clean_numero(self):
        numero = self.cleaned_data.get("numero", None)
        return numero

    def clean_codigobarrio(self):
        codigobarrio = self.cleaned_data.get("codigobarrio", None)
        return codigobarrio

    def clean_lat(self):
        lat = self.cleaned_data.get("lat", None)
        return lat

    def clean_lng(self):
        lng = self.cleaned_data.get("lng", None)
        return lng

    def clean(self):
        return super(PuntoLuzForm, self).clean()

    def validate_unique(self):
        return super(PuntoLuzForm, self).validate_unique()

    def save(self, commit=True):
        return super(PuntoLuzForm, self).save(commit)

