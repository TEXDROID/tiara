# Tiara - Sistema Distribuido con CORBA (omniorb)

Este proyecto es una implementación de un sistema distribuido utilizando el estándar **CORBA** y la librería **omniORB** para Python. El sistema permite la comunicación entre objetos distribuidos a través de un servicio de nombres (`naming service`).

## Arquitectura del Proyecto

El sistema está compuesto por tres componentes principales desplegados en contenedores Docker independientes:

* **Names (Servicio de Nombres):** Actúa como el directorio donde se registran los servicios.
* **Server (Servidor):** Implementa la lógica de negocio y registra su objeto en el servicio de nombres.
* **Client (Cliente):** Localiza el servicio a través del `Names` y ejecuta métodos remotos.

## 🛠️equisitos

* Docker y Docker Compose.
* Python 3.x.
* omniORB y omniORBpy (incluidos en la imagen base).

## Despliegue con Docker

Para levantar el entorno completo, asegúrate de estar en la raíz del proyecto y ejecuta:

```bash
docker-compose up -d
