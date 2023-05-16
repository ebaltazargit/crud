from django.db import models

#Create your models here.
class altaEnsayos(models.Model):
    IDaltaEnsayos = models.IntegerField(primary_key=True)
    nombreSolicitante = models.CharField(max_length=100, null=False)
    areaSolicitante = models.CharField(max_length=100, null=False)
    fechaSolicitud = models.DateField(null=False)
    opciones = models.CharField(max_length=100, null=False, default='null')
    proyecto = models.CharField(max_length=100, null=False)
    claveEnsayo = models.CharField(max_length=100, null=False)
    nombreEnsayo = models.CharField(max_length=100, null=False)
    ensayooperfil = models.CharField(max_length=100, null=False)
    laboratorio = models.CharField(max_length=100, null=False)
    tipoMuestra = models.CharField(max_length=100, null=False)
    condiciones = models.CharField(max_length=100, null=False)
    motivosRechazo = models.CharField(max_length=100, null=False)
    tiempoEntrega = models.CharField(max_length=100, null=False)
    precio = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'altaEnsayos'

class altaInter(models.Model):
    IDaltaInter = models.IntegerField(primary_key=True)
    ensayo = models.CharField(max_length=100, null=False)
    host = models.CharField(max_length=100, null=False)
    analizador = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'altaInter'

class valoresRef(models.Model):
    IDvaloresRef = models.IntegerField(primary_key=True)
    nombreSolicitante = models.CharField(max_length=100, null=False)
    fechaSolicitud = models.DateField(null=False)
    area = models.CharField(max_length=100, null=False)
    sistema = models.CharField(max_length=100, null=False)
    anexos = models.CharField(max_length=100, null=False)
    claveCatalogo = models.CharField(max_length=100, null=False)
    labSubrogacion = models.CharField(max_length=100, null=False)
    ensayo = models.CharField(max_length=100, null=False)
    motivodecambios = models.CharField(max_length=100, null=False)
    cambio = models.CharField(max_length=100, null=False)
    metodologia = models.CharField(max_length=100, null=False)
    unidades = models.CharField(max_length=100, null=False)
    ValoresReferencia = models.TextField(null=False)
    class Meta:
        db_table = 'valoresRef'

class altaEnsayos2(models.Model):
    IDaltaEnsayos2 = models.IntegerField(primary_key=True)
    nombreSolicitante = models.CharField(max_length=100, null=False)
    areaSolicitante = models.CharField(max_length=100, null=False)
    fechaSolicitud = models.DateField(null=False)
    
    intercambio = models.CharField(max_length=100, null=False)
    porCobrar = models.CharField(max_length=100, null=False)
    pasteur = models.CharField(max_length=100, null=False)
    modulab = models.CharField(max_length=100, null=False)

    proyecto = models.CharField(max_length=100, null=False)
    claveEnsayo = models.CharField(max_length=100, null=False)
    nombreEnsayo = models.CharField(max_length=100, null=False)
    ensayooperfil = models.CharField(max_length=100, null=False)
    laboratorio = models.CharField(max_length=100, null=False)
    tipoMuestra = models.CharField(max_length=100, null=False)
    condiciones = models.CharField(max_length=100, null=False)
    motivosRechazo = models.CharField(max_length=100, null=False)
    tiempoEntrega = models.CharField(max_length=100, null=False)
    precio = models.CharField(max_length=100, null=False)
    class Meta:
        db_table = 'altaEnsayos2'