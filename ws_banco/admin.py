from django.contrib import admin
from .models import Tarjeta
# Register your models here.

# Se realiza el registro con un decorador
@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
    list_display = ('n_tarjeta', 'nip', 'f_vencimiento', 'saldo',
                    'limite', 'es_bloqueada', 'es_verificada',
                    'intento')
    list_filter = ('n_tarjeta', 'es_bloqueada', 'es_verificada')
    search_fields = ('n_tarjeta',)
    ordering = ('n_tarjeta', 'saldo', 'es_bloqueada', 'es_verificada')