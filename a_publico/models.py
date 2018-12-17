# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BarrioPedania(models.Model):
    codigobarrio = models.AutoField(primary_key=True)
    nombrebarrio = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'barrio_pedania'
    
    def __str__(self):
        return self.nombrebarrio

class CatalogoCalles(models.Model):
    codigocalle = models.AutoField(primary_key=True)
    codigotipovia = models.ForeignKey('ViaPublica', models.DO_NOTHING, db_column='codigotipovia')
    nombrecalle = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'catalogo_calles'
    
    def __str__(self):
        return '%s %s' % (self.codigotipovia, self.nombrecalle)

class CatalogoLamparas(models.Model):
    codigolampara = models.AutoField(primary_key=True)
    nombrelampara = models.CharField(max_length=20)
    pvp = models.SmallIntegerField(blank=True, null=True)
    amortizacion = models.SmallIntegerField(blank=True, null=True)
    actualprecio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_lamparas'

    def __str__(self):
        return self.nombrelampara

class CatalogoLuminarias(models.Model):
    codigoluminaria = models.AutoField(primary_key=True)
    nombreluminaria = models.CharField(max_length=30)
    pvp = models.SmallIntegerField(blank=True, null=True)
    amortizacion = models.SmallIntegerField(blank=True, null=True)
    actualprecio = models.DateField(blank=True, null=True)
    codigolampara = models.ForeignKey(CatalogoLamparas, models.DO_NOTHING, db_column='codigolampara', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_luminarias'

    def __str__(self):
        return self.nombreluminaria
        

class CatalogoSoportes(models.Model):
    codigosoporte = models.AutoField(primary_key=True)
    nombresoporte = models.CharField(max_length=30)
    pvp = models.SmallIntegerField(blank=True, null=True)
    amortizacion = models.SmallIntegerField(blank=True, null=True)
    actualprecio = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo_soportes'

    def __str__(self):
        return self.nombresoporte
        

class CuadroMando(models.Model):
    cuadrocodigo = models.AutoField(primary_key=True)
    codigoindentificacion = models.CharField(max_length=12)
    codigocontadores = models.ForeignKey('EquiposMedida', models.DO_NOTHING, db_column='codigocontadores')
    codigocalle = models.ForeignKey(CatalogoCalles, models.DO_NOTHING, db_column='codigocalle')
    numero = models.SmallIntegerField(blank=True, null=True)
    codigobarrio = models.ForeignKey(BarrioPedania, models.DO_NOTHING, db_column='codigobarrio')
    tipocuadro = models.SmallIntegerField()
    salidasutilizadas = models.SmallIntegerField(blank=True, null=True)
    mgtentrada = models.SmallIntegerField(blank=True, null=True)
    fachada = models.BooleanField(blank=True, null=True)
    alimentacionfn = models.BooleanField(db_column='alimentacionFN', blank=True, null=True)  # Field name made lowercase.
    alimentacion3fn = models.BooleanField(db_column='alimentacion3FN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cuadro_mando'

    def __str__(self):
        return '%s %s %s' % (self.codigoindentificacion, self.codigocontadores, self.codigobarrio)


class EquiposMedida(models.Model):
    codigocontadores = models.AutoField(primary_key=True)
    codigoidentificacion = models.CharField(max_length=12)
    codigocalle = models.ForeignKey(CatalogoCalles, models.DO_NOTHING, db_column='codigocalle', blank=True, null=True)
    numero = models.SmallIntegerField(blank=True, null=True)
    codigobarrio = models.ForeignKey(BarrioPedania, models.DO_NOTHING, db_column='codigobarrio', blank=True, null=True)
    kwcontrato = models.SmallIntegerField(blank=True, null=True)
    numeroactiva = models.CharField(max_length=10, blank=True, null=True)
    numeroreactiva = models.CharField(max_length=10, blank=True, null=True)
    monofasico = models.BooleanField(blank=True, null=True)
    lecturadirecta = models.BooleanField(blank=True, null=True)
    lecturaindirecta = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipos_medida'

    def __str__(self):
        return '%s %s' % (self.codigoidentificacion, self.codigobarrio)


class PuntoLuz(models.Model):
    codigopuntodeluz = models.AutoField(primary_key=True)
    codigosoporte = models.ForeignKey(CatalogoSoportes, models.DO_NOTHING, db_column='codigosoporte')
    codigoluminaria = models.ForeignKey(CatalogoLuminarias, models.DO_NOTHING, db_column='codigoluminaria')
    codigocuadro = models.ForeignKey(CuadroMando, models.DO_NOTHING, db_column='codigocuadro')
    codigocalle = models.ForeignKey(CatalogoCalles, models.DO_NOTHING, db_column='codigocalle')
    numero = models.CharField(max_length=5, blank=True, null=True)
    codigobarrio = models.ForeignKey(BarrioPedania, models.DO_NOTHING, db_column='codigobarrio')
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    implanterenovacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'punto_luz'

    def __str__(self):
        return '%s %s' % (self.codigobarrio, self.codigocalle)

class ViaPublica(models.Model):
    codigotipovia = models.AutoField(primary_key=True)
    nombretipovia = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'via_publica'

    def __str__(self):
        return self.nombretipovia
