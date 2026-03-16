import sys
from omniORB import CORBA
import CosNaming
import _GlobalIDL
import Echo_idl, _GlobalIDL

# Inicialización del ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Obtener referencia al Naming Service
try:
    obj = orb.resolve_initial_references("NameService")
    rootContext = obj._narrow(CosNaming.NamingContext)

    # Buscar el servicio "EchoService"
    name = [CosNaming.NameComponent("EchoService", "")]
    obj_referencia = rootContext.resolve(name)

    # Narrow a la interfaz Echo usando el módulo generado Echo_idl
    echo_obj = obj_referencia._narrow(_GlobalIDL.Echo)

    if echo_obj is None:
        print("Error: El objeto no es de tipo Echo")
        sys.exit(1)

    # Invocar el método
    mensaje = "Hola desde el contenedor Cliente"
    resultado = echo_obj.echoString(mensaje)
    print(f"Respuesta recibida: {resultado}")

except Exception as e:
    print(f"Error en el cliente: {str(e)}")

