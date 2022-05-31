from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Double, Unicode, Boolean, Short
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from .models import Tarjeta
from datetime import date


class BancoSoapService(ServiceBase):
    # Métodos del servicio
    # Método para verificar que una tarjeta existe en DB
    @rpc(Unicode(nilablle=False, ), _returns=Boolean)
    def consulta_tarjeta(ctx, n_tarjeta):
        try:
            Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return True
        except Tarjeta.DoesNotExist:
            return False

    # Método para verificar que la tarjeta está verificada
    # Simula la verificación del chip de una tarjeta
    @rpc(Unicode(nillable=False,), _returns=Boolean)
    def verifica_tarjeta(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return t.es_verificada
        except Tarjeta.DoesNotExist:
            return False
    
    # Método para verificar si la tarjeta se encuentra bloqueada
    # Se bloquea debido a que se sobrepasa los intentos el cliente
    @rpc(Unicode(nillable=False,), _returns=Boolean)
    def verifica_tarjeta_bloqueada(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return t.es_bloqueada
        except Tarjeta.DoesNotExist:
            return False

    # Método que verifica si la fecha de vencimiento de la tarjeta
    # se encuentra vigente
    @rpc(Unicode(nillable=False,), _returns=Boolean)
    def verifica_fecha(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            if date.today() < t.f_vencimiento:
                return True
            else:
                return False

        except Tarjeta.DoesNotExist:
            return False

    # Método que verifica si el nip es correcto, en caso de que no
    # aumenta el número de intentos
    @rpc(Unicode(nillable=False,), Short(nillable=False,), _returns=Boolean)
    def consulta_nip(ctx, n_tarjeta, nip):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            band = False
            if t.nip == nip:
                t.intento = 0
                band = True
            else:
                t.intento += 1
            if t.intento >= 3:
                t.es_bloqueada = True
            t.save()
            return band
        except Tarjeta.DoesNotExist:
            return False

    # Método que devuelve el número de intentos fallidos al
    # digitar el nip
    @rpc(Unicode(nillable=False,),_returns=Short)
    def consulta_intentos(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return t.intento
        except Tarjeta.DoesNotExist:
            return -1
    
    # Método que realiza el retiro de efectivo de un cliente
    @rpc(Unicode(nillable=False,), Double(nillable=False), _returns=Double)
    def realiza_pago(ctx, n_tarjeta, pago):
        try:
            r = 0.0
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            if pago <= t.limite and pago <= t.saldo:
                t.saldo -= pago
                r = t.saldo
                t.save()
            return r
        except Tarjeta.DoesNotExist:
            return -1

    # Método que verifica el limite establecido que puede retirar el cliente
    @rpc(Unicode(nillable=False,), _returns=Double)
    def verifica_limite(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return t.limite
        except Tarjeta.DoesNotExist:
            return -1
    # Método que devuelve el saldo de la tarjeta
    @rpc(Unicode(nillable=False,), _returns=Double)
    def consulta_saldo(ctx, n_tarjeta):
        try:
            t=Tarjeta.objects.get(n_tarjeta=n_tarjeta)
            return t.saldo
        except Tarjeta.DoesNotExist:
            return -1

    

soap_app = Application(
    [BancoSoapService],
    tns='www.uacm.edu.mx/banco_soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
    )

django_soap_application = DjangoApplication(soap_app)
my_soap_app = csrf_exempt(django_soap_application)