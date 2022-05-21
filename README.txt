¡¡¡Hola!!!
Este proyecto es realizado en Python, específicamente en Django, y es un 
servicio web soap.
En este servicio web expone una interfaz con los métodos para simular un
cajero automático (ATM) de un banco.
Los servicios que expone son los siguientes:
-> consulta_tarjeta: Método donde verifica si el número de tarjeta existe en la BD
-> verifica_tarjeta: Método para verificar que la tarjeta está verificada. 
    Simula la verificación del chip de una tarjeta.
-> verifica_tarjeta_bloqueada: Método para verificar si la tarjeta se encuentra bloqueada.
    Se bloquea debido a que se sobrepasa los intentos el cliente.
-> verifica_fecha: Método que verifica si la fecha de vencimiento de la tarjeta
    se encuentra vigente.
-> consulta_nip: Método que verifica si el nip es correcto, en caso de que no
    aumenta el número de intentos. Si el número de intentos es mayor a 3
    se bloquea la tarjeta.
-> consulta_intentos: Método que devuelve el número de intentos fallidos al
    digitar el nip
-> realiza_pago: Método que realiza el retiro de efectivo de un cliente.
-> verifica_limite: Método que verifica el limite establecido que puede retirar el cliente.
-> consulta_saldo: Método que devuelve el saldo de la tarjeta.
    
    <<Requerimientos del Proyecto>>>
Los requerimientos necesarios para ejecutar la aplicación web los encuentra en el
archivo requirements.txt, para instarlos solo tiene que ejecutar el siguiente comando
    pip install -r requirements.txt
Con esto comenzará la descarga de todas las dependencias para el funcionamiento del
proyecto.

    Nota importante: Se recomienda crear un entorno virtual donde pueda descargar
    todas las dependencias del proyecto. Para la creación de un entorno virtual en
    python se tienen que ejecutar los siguientes comandos:
        pip install virtualenv
        python -m venv nom_carpeta

    <<Forma de Ejecutarlo>>
La manera de ejecutar un proyecto en Django es la siguiente:
    python manage.py runserver
Por defecto Django corre el servidor en el puerto 8000.

    <<WSDL>>
El wsdl del servicio web soap se encuentra en el siguiente enlace:
    http://localhost:8000/soap_banco/?wsdl

