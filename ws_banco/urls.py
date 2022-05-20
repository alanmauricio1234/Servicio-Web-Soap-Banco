from django.urls import path
from . import service
app_name = 'ws_banco'
urlpatterns = [
    path('soap_banco/', service.my_soap_app),
]