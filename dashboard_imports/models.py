from django.db import models
from django.forms import model_to_dict

class Country(models.Model):
    cod = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100, db_column="nombre")

    class Meta:
        managed = False
        db_table = 'cods_paises'

class ImportProcess(models.Model):
    fech = models.IntegerField()
    adua = models.IntegerField()
    paisgen = models.IntegerField()
    #paispro = models.IntegerField()
    paispro = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, db_column='paispro', default=None)
    paiscom = models.IntegerField()
    deptodes = models.IntegerField()
    regimen = models.CharField(max_length=50)
    naban = models.DecimalField(max_digits=15, decimal_places=2)
    vafodo = models.DecimalField(max_digits=15, decimal_places=2)
    flete = models.DecimalField(max_digits=15, decimal_places=2)
    vacid = models.DecimalField(max_digits=15, decimal_places=2)
    vacip = models.DecimalField(max_digits=15, decimal_places=2)
    imp1 = models.DecimalField(max_digits=15, decimal_places=2)
    cuidaimp = models.CharField(max_length=50)
    cuidaexp = models.CharField(max_length=50)
    actecon = models.IntegerField()
    codadad = models.IntegerField()
    vadua = models.DecimalField(max_digits=15, decimal_places=2)
    vrajus = models.DecimalField(max_digits=15, decimal_places=2)
    baseiva = models.DecimalField(max_digits=15, decimal_places=2)
    totalivayo = models.DecimalField(max_digits=15, decimal_places=2)
    seguros = models.DecimalField(max_digits=15, decimal_places=2)
    otrosg = models.DecimalField(max_digits=15, decimal_places=2)
    luin = models.CharField(max_length=20)
    codluin = models.CharField(max_length=50)
    depim = models.IntegerField()
    copaex = models.CharField(max_length=50)
    tipoim = models.IntegerField()
    porara = models.DecimalField(max_digits=5, decimal_places=2)
    derel = models.DecimalField(max_digits=15, decimal_places=2)

    def toJSON(self):
        item = model_to_dict(self)
        return item
