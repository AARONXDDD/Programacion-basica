import os
import time

# Tiempo en segundos antes de cerrar el navegador (por ejemplo, 10 segundos)
intervalo = 10  

# Nombre del navegador (ejemplo: chrome, firefox, edge)
navegador = "Explorer"

while True:
    print(f"⏳ Esperando {intervalo} segundos antes de cerrar {navegador}...")
    time.sleep(intervalo)  # Espera el tiempo definido

    # Cerrar el navegador según el sistema operativo
    if os.name == "nt":  # Windows
        os.system(f"taskkill /IM {navegador}.exe /F")
    else:  # Linux / Mac
        os.system(f"pkill {navegador}")

    print(f"❌ {navegador} ha sido cerrado.")