# ⚠️Precaución

![WARNING-12-12-2024 (1)](https://github.com/user-attachments/assets/148e670a-8284-47b0-9080-e8fbd738d85b)

========================================================================

### 👮 Usa la herramienta con Autorización o en Entornos Seguros
### 👮 Esta herramienta solo se debe emplear con fines Éticos o de Investigación
### 👮 No recomendamos su uso en zonas no autorizadas

========================================================================

------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔍️ Descubre directorios ocultos con RsyncForce 

![RsyncForce-8-2-2025](https://github.com/user-attachments/assets/97fc3ba5-ce29-462e-a216-cf2f395731c7)

------------------------------------------------------------------------------------------------------------------------------------------------------------

### 🌐 RsyncForce 🌐
RsyncForce es una herramienta que automatiza:

#### ⭐ Directorios que no se pueden listar dentro del servicio Rsync.
#### ⭐ Diccionario con palabras claves para reiterar en la enumeracion.
#### ⭐ IP privada del objetivo para apuntar.
#### ⭐ Puerto donde se aloja el servicio Rsync (Si no se pone nada lo hara en el puerto predeterminado 873)

------------------------------------------------------------------------------------------------------------------------------------------------------------

Para usar la herramienta seguiremos los siguientes comandos:

🔴 Clonamos el repositorio

```bash
git clone https://github.com/MatthyGD/RsyncForce.git
```

🔴 Entramos dentro del repositorio

```bash
cd RsyncForce/
```

🔴 Garantizamos permisos de Ejecucción

```bash
python3 RsyncForce.py
```

------------------------------------------------------------------------------------------------------------------------------------------------------------

Hemos descubierto una ruta? Veamos sus archivos internos!

🔴 Vemos que archivos se alojan dentro de la ruta descubierta

```bash
rsync rsync://rsync-connect@<IP victima>/<Directorio descubierto>/
```

------------------------------------------------------------------------------------------------------------------------------------------------------------

Hemos descubierto archivos? Vamos a pasarlo a nuestra maquina!

🔴 Descargamos los archivos que se alojan dentro de la ruta descubierta

```bash
rsync rsync://rsync-connect@<IP victima>/<Directorio descubierto>/<Archivo que queramos descargar> .
```

------------------------------------------------------------------------------------------------------------------------------------------------------------

✅ 1 -> Ejemplo de uso de la herramienta RsyncForce:

![1](https://github.com/user-attachments/assets/44f242ad-aab0-4f7b-aefe-daffdb9135ca)

------------------------------------------------------------------------------------------------------------------------------------------------------------

✅ 2 -> Ejemplo de como listar y descargar contenido:

![2](https://github.com/user-attachments/assets/48ca7ac1-b965-4f01-aa77-b4eabe6ef4a4)

------------------------------------------------------------------------------------------------------------------------------------------------------------

# ❤️ Hasta aqui todo!
