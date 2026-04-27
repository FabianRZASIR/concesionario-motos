# 🏍️ Proyecto Concesionario de Motos (Infraestructura Distribuida)

Este proyecto es una aplicación web desarrollada en **Flask** con una base de datos **MariaDB**, distribuida en dos Máquinas Virtuales (Linux) y accesible desde internet mediante túneles seguros.

## 🏗️ Arquitectura del Sistema

El sistema se divide en dos servidores independientes para simular un entorno real:

1.  **VM 1 (Base de Datos):** Gestiona la persistencia de datos con MariaDB.
2.  **VM 2 (Servidor Web):** Ejecuta la lógica de la aplicación en Python/Flask.

---

## 🔗 Enlaces de Acceso en Vivo

Para facilitar la corrección, los servicios están expuestos mediante túneles:

### 🌐 Aplicación Web (Frontend)
* **URL:** `https://recast-bonelike-audience.ngrok-free.dev`
* *(Servicio gestionado mediante Ngrok en la VM 2)*

### 🗄️ Acceso a Base de Datos (DBeaver/Gestores)
Si desea conectar directamente a la base de datos para verificar las tablas:
* **Host:** `zbklecgsnl.localto.net`
* **Puerto:** `8688`
* **Usuario:** `moto_admin`
* **Password:** `Admin123!`
* **Base de Datos:** `concesionario_motos`
* *(Servicio gestionado mediante Localtonet en la VM 1)*

---

## 🛠️ Tecnologías Utilizadas

* **Backend:** Python 3.x con Flask.
* **Base de Datos:** MariaDB.
* **Frontend:** HTML5 / CSS3 (Plantillas Jinja2).
* **Conectividad:** Ngrok (HTTP) y Localtonet (TCP).
* **Gestión de Versiones:** Git / GitHub.

## 🚀 Cómo ejecutarlo localmente

1. **Clonar el repo:** `git clone https://github.com/FabianRZASIR/concesionario-motos.git`
2. **Instalar dependencias:** `pip install flask mysql-connector-python`
3. **Configurar DB:** Asegurarse de que MariaDB esté corriendo y tenga el esquema `concesionario_motos` creado.
4. **Lanzar App:** `python3 app.py`
