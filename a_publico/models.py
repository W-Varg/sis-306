
from django.db import models

class BarrioPedania(models.Model):
    nombrebarrio = models.CharField(max_length=25)

    def __str__(self):
        return self.nombrebarrio

class ViaPublica(models.Model):
    nombretipovia = models.CharField(max_length=15)

    def __str__(self):
        return self.nombretipovia

class CatalogoLampara(models.Model):
    nombrelampara = models.CharField(max_length=20)
    pvp = models.FloatField(blank=True, null=True, default=0)
    amortizacion = models.PositiveSmallIntegerField(blank=True, null=True,default=0,)
    actualprecio = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.nombrelampara

class CatalogoCalle(models.Model):
    codigotipovia = models.ForeignKey('ViaPublica', on_delete=models.CASCADE)
    nombrecalle = models.CharField(max_length=35)
    
    def __str__(self):
        return '%s %s' % (self.codigotipovia, self.nombrecalle)

class CatalogoLuminaria(models.Model):
    nombreluminaria = models.CharField(max_length=30)
    pvp = models.FloatField(blank=True, null=True, default=0)
    amortizacion = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    actualprecio = models.DateTimeField(auto_now_add=True, blank=True)
    codigolampara = models.ForeignKey('CatalogoLampara', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombreluminaria,self.actualprecio)

class CatalogoSoporte(models.Model):
    nombresoporte = models.CharField(max_length=30)
    pvp = models.FloatField(blank=True, null=True, default=0)
    amortizacion = models.PositiveSmallIntegerField(blank=True, null=True)
    actualprecio = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.nombresoporte, self.actualprecio)

class EquiposMedida(models.Model):
    codigoidentificacion = models.CharField(max_length=12)
    codigocalle = models.ForeignKey('CatalogoCalle', on_delete=models.CASCADE)
    numero = models.SmallIntegerField(blank=True, null=True)
    codigobarrio = models.ForeignKey('BarrioPedania', on_delete=models.CASCADE)
    kwcontrato = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    numeroactiva = models.CharField(max_length=10, blank=True, null=True)
    numeroreactiva = models.CharField(max_length=10, blank=True, null=True)
    monofasico = models.BooleanField(blank=True, null=True)
    lecturadirecta = models.BooleanField(blank=True, null=True)
    lecturaindirecta = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.codigoidentificacion, self.kwcontrato)        

class CuadroMando(models.Model):
    codigoindentificacion = models.CharField(max_length=12)
    codigocontadores = models.ForeignKey('EquiposMedida', on_delete=models.CASCADE)
    codigocalle = models.ForeignKey('CatalogoCalle', on_delete=models.CASCADE)
    numero = models.SmallIntegerField(blank=True, null=True)
    codigobarrio = models.ForeignKey('BarrioPedania', on_delete=models.CASCADE)
    tipocuadro = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    salidasutilizadas = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    mgtentrada = models.FloatField(blank=True, null=True, default=0)
    fachada = models.BooleanField(blank=True, null=True)
    alimentacionfn = models.BooleanField(blank=True, null=True)
    alimentacion3fn = models.BooleanField(blank=True, null=True)
    def __str__(self):
        return '%s %s %s' % (self.codigoindentificacion, self.codigocontadores, self.codigobarrio)


class PuntoLuz(models.Model):
    codigosoporte = models.ForeignKey('CatalogoSoporte', on_delete=models.CASCADE)
    codigoluminaria = models.ForeignKey('CatalogoLuminaria', on_delete=models.CASCADE)
    codigocuadro = models.ForeignKey('CuadroMando', on_delete=models.CASCADE)
    codigocalle = models.ForeignKey('CatalogoCalle', on_delete=models.CASCADE)
    numero = models.CharField(max_length=5, blank=True, null=True)
    codigobarrio = models.ForeignKey('BarrioPedania', on_delete=models.CASCADE)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    implanterenovacion = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.codigobarrio, self.codigocalle)

# ================LISTOS============
