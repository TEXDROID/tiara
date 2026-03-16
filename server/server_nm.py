import sys
from omniORB import CORBA
import CosNaming
import Echo_idl, _GlobalIDL__POA

# Implementacion de la interfaz Echo
class Echo_i(_GlobalIDL__POA.Echo):
    def echoString(self, mesg):
        print(f"Invocacion recibida: {mesg}")
        return f"Servidor CORBA (Docker) dice: Recibido '{mesg}'"

# Inicializacion del ORB
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
# Obtenemos el RootPOA directamente desde el ORB
poa = orb.resolve_initial_references("RootPOA")

# Crear el objeto y activarlo
ei = Echo_i()
eo = ei._this()

# Obtener referencia al Naming Service
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

# Registrar el servicio con el nombre "EchoService"
name = [CosNaming.NameComponent("EchoService", "")]
rootContext.rebind(name, eo)

print("Servidor Echo registrado y listo...")

# Activar el POA y correr el ORB
poa._get_the_POAManager().activate()
orb.run()
