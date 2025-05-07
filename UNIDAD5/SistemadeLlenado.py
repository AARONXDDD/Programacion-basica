import time
BOMBA = 100 

def leer_boton():
    print("\npreciona un boton")
    print("1. 500 ml")
    print("2. 1L")
    print("3. 1.5L")
    print("4. Apagar")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        return 500
    elif opcion == "2":
        return 1000
    elif opcion == "3":
        return 1500
    elif opcion == "0":
        return 0
    else:
        print("Opcion no invalida")
        return leer_boton()

def prender_sistema():
    print("dispensando agua.")

def desactivar_sistema():
    print("apagando.")

def main():
    while True:
        volumen = leer_boton()
        if volumen == 0:
            print("Saliendo del sistema.")
            break
        tiempo_llenado = volumen / BOMBA
        print(f"Llenando {volumen} ml. Tiempo esperado: {tiempo_llenado:.2f} segundos.")
        print("Llenado completado.\n")

if __name__ == "__main__":
    main()
