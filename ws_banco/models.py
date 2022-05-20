from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    n_tarjeta = models.CharField(max_length=4, primary_key=True)
    f_vencimiento = models.DateField()
    saldo = models.FloatField()
    limite = models.FloatField()
    es_bloqueada = models.BooleanField()
    es_verificada = models.BooleanField()
    intento = models.IntegerField()
    nip = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('-n_tarjeta',)

        def __str__(self):
            return self.n_tarjeta

