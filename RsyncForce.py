import multiprocessing
import os
import subprocess
import time
import sys
from itertools import cycle

# Función para hacer las peticiones con rsync
def check_path(path, start_time, total_files, processed_files):
    rsync_cmd = f"rsync -av --list-only rsync://{TARGET}:{PORT}/{path} 2>/dev/null"
    result = subprocess.run(rsync_cmd, shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        print(f"\n\033[92m[✔️] ¡Encontrado! Ruta: {path}\033[0m")
        os._exit(0)

# Función para mostrar animación de carga
def loading_animation(stop_event):
    try:
        for frame in cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]):
            if stop_event.is_set():
                break
            sys.stdout.write(f"\r⏳ Escaneando... {frame}")
            sys.stdout.flush()
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass

# Función que procesará el archivo
def update_time_left(path, start_time, total_files, processed_files):
    try:
        processed_files.value += 1
        check_path(path, start_time, total_files, processed_files)
    except KeyboardInterrupt:
        pass

# Función para pedir entradas al usuario de manera segura
def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\n🚨 ¡Proceso detenido por el usuario! 🚨")
        sys.exit(0)

# Función principal
def main():
    global TARGET, PORT
    print("🌟 ¡Bienvenido al escáner de rutas con rsync! 🌟")
    
    dict_path = safe_input("📁 Introduce la ruta del diccionario de rutas a escanear: ")
    target = safe_input("🌐 Introduce la IP del host objetivo (Ej: 192.168.0.52): ")
    TARGET = target
    port = safe_input("🔒 Introduce el puerto donde se aloja el servicio rsync (Ej: 873): ")
    PORT = port

    try:
        with open(dict_path, "r", encoding="utf-8") as file:
            paths = [line.strip() for line in file if line.strip()]
        print(f"🔍 Se encontraron {len(paths)} rutas en el diccionario.")
    except FileNotFoundError:
        print("\033[91m[✘] Error: No se encontró el diccionario. 😔\033[0m")
        sys.exit(1)

    total_files = len(paths)
    start_time = time.time()

    manager = multiprocessing.Manager()
    processed_files = manager.Value('i', 0)
    stop_event = manager.Event()

    loader_process = multiprocessing.Process(target=loading_animation, args=(stop_event,))
    loader_process.start()

    try:
        with multiprocessing.Pool(200) as pool:
            pool.starmap(update_time_left, [(path, start_time, total_files, processed_files) for path in paths])
    except KeyboardInterrupt:
        print("\n\n🚨 ¡Proceso detenido por el usuario! 🚨")
        stop_event.set()
        loader_process.terminate()
        loader_process.join()
        sys.exit(0)

    stop_event.set()
    loader_process.terminate()
    loader_process.join()
    end_time = time.time()
    print(f"\n⏳ Tiempo total de escaneo: {round(end_time - start_time, 2)} segundos. 🚀")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🚨 ¡Proceso detenido por el usuario! 🚨")
        sys.exit(0)
