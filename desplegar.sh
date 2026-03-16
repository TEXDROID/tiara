#!/bin/bash

echo "--- 1. Limpiando contenedores anteriores ---"
docker rm -f el-naming el-server el-cliente 2>/dev/null

echo "--- 2. Levantando Naming Service (el-naming) ---"
cd names
docker build -t tiara-names .
docker run -d --name el-naming --network red-corba tiara-names
cd ..

# Esperar un momento a que el Naming Service respire
sleep 2

echo "--- 3. Levantando Servidor (el-server) ---"
cd server
docker build -t tiara-server .
docker run -d --name el-server --network red-corba tiara-server
# Crear paquetes Python necesarios y reiniciar para que los vea
docker exec el-server bash -c "touch _GlobalIDL/__init__.py _GlobalIDL__POA/__init__.py"
docker restart el-server
cd ..

echo "--- 4. Levantando Cliente (el-cliente) ---"
cd client
docker build -t tiara-client .
docker run -d --name el-cliente --network red-corba tiara-client
# Crear paquetes Python necesarios
docker exec el-cliente bash -c "touch _GlobalIDL/__init__.py _GlobalIDL__POA/__init__.py"
cd ..

echo "--- 5. Verificando estado ---"
docker ps

echo "------------------------------------------------"
echo "Todo listo. Ejecuta el cliente con:"
echo "docker exec -it el-cliente python3 client_ns.py"
echo "------------------------------------------------"
