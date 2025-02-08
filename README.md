# ⚠️Precaución

![WARNING-12-12-2024 (1)](https://github.com/user-attachments/assets/148e670a-8284-47b0-9080-e8fbd738d85b)

========================================================================

### 👮 Usa la herramienta con Autorización o en Entornos Seguros
### 👮 Esta herramienta solo se debe emplear con fines Éticos o de Investigación
### 👮 No recomendamos su uso en zonas no autorizadas

========================================================================

------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔍️ Descubre directorios ocultos con RsyncForce 

![RsyncForce-8-2-2025](https://github.com/user-attachments/assets/38b324cd-a53d-4e8c-9286-179077abae0a)

------------------------------------------------------------------------------------------------------------------------------------------------------------

### 🌐 RsyncForce 🌐
RsyncForce es una herramienta que automatiza:

#### ⭐ Directorios que no se pueden listar dentro del servicio Rsync.
#### ⭐ Diccionario con palabras claves para reitarar en la enumeracion.
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

![1](https://github.com/user-attachments/assets/431caf9f-8525-42b7-9073-37a04673721e)

------------------------------------------------------------------------------------------------------------------------------------------------------------

✅ 2 -> Ejemplo de como listar y descargar contenido:

![2](https://github.com/user-attachments/assets/34e73675-b2da-4d46-9b88-a0ca367bfa68)

------------------------------------------------------------------------------------------------------------------------------------------------------------

# ❤️ Hasta aqui todo!
