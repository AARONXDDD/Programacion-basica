from Archivos import guardar_diccionarios_en_csv, leer_diccionarios_de_csv
import datetime
import random
import os 

archivo = "almacen"
# Diccionarios de productos
accesorios = {
    "0001": {"producto": "s44+", "presio":15000, "existencias" : 5},
    "0002": {"producto": "xbox series s", "presio":6000, "existencias" : 12},
    "0003": {"producto": "mac", "presio":100, "existencias" : 2},
    "0004": {"producto": "audifonos genericos", "presio":60, "existencias" : 132},
    "0005": {"producto": "bateris recargables", "presio":120, "existencias" : 50},
    "0006": {"producto": "baterias", "presio":12, "existencias" : 12},
    "0007": {"producto": "botella de agua", "presio":12, "existencias" : 200},
}

juegos = {
    "0008": {"producto": "The wicher 3", "presio":70, "existencias" : 2},
    "0009": {"producto": "halo infinite", "presio":1200, "existencias" : 50},
    "0010": {"producto": "jedi suvivor", "presio":12, "existencias" : 12},
    "0011": {"producto": "Ninja gaiden 2 black", "presio":1300, "existencias" : 20},
    "0012": {"producto": "mario kart 8", "presio":1500, "existencias" : 2},
    "0013": {"producto": "gta v", "presio":1200, "existencias" : 50},
    "0014": {"producto": "mario partie", "presio":1500, "existencias" : 10},
    "0015": {"producto": "skyrim", "presio":300, "existencias" : 2},
}
guardar_diccionarios_en_csv(archivo, juegos, accesorios)

carrito_de_compras = []

while True:
    print("\n 👾 Bienvenido a Game Store Online 👾")
    print("1. Mostrar juegos")
    print("2. Mostrar accesorios")
    print("3. Agregar producto al carrito")
    print("4. Eliminar de tu carrito")
    print("5. Mostrar carrito")
    print("6. Finalizar compra")
    print("7. Salir")

    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("\n Juegos disponibles:")
        for codigo, producto in juegos.items():
            print(f"{codigo}: {producto['producto']} - ${producto['presio']} | Existencias: {producto['existencias']}")

    elif opcion == "2":
        print("\n Accesorios disponibles:")
        for codigo, producto in accesorios.items():
            print(f"{codigo}: {producto['producto']} - ${producto['presio']} | Existencias: {producto['existencias']}")

    elif opcion == "3":
        codigo = input("Ingrese el código del producto: ")
        producto_encontrado = False
        
        for tienda in [juegos, accesorios]:
            if codigo in tienda:
                producto = tienda[codigo]
                cantidad = int(input("Cantidad a agregar: "))
                
                if producto["existencias"] >= cantidad:
                    encontrado = False
                    for item in carrito_de_compras:
                        if item["codigo"] == codigo:
                            item["cantidad"] += cantidad
                            encontrado = True
                            break
                    
                    if not encontrado:
                        carrito_de_compras.append({
                            "codigo": codigo,
                            "cantidad": cantidad,
                            "precio_unitario": producto["presio"],
                            "clase": 'juegos' if tienda == juegos else 'accesorios'
                        })
                    
                    producto["existencias"] -= cantidad
                    print(f" {cantidad} {producto['producto']} agregado(s) al carrito")
                    producto_encontrado = True
                    break
                else:
                    print(f" Sin stock disponible: {producto['existencias']}")
                    producto_encontrado = True
                    break
        
        if not producto_encontrado:
            print("Producto no encontrado")

    elif opcion == "4":
        if not carrito_de_compras:
            print("El carrito está vacío")
            continue
            
        codigo = input("Ingrese el código del producto: ")
        for item in carrito_de_compras:
            if item["codigo"] == codigo:
                cantidad = int(input("Cantidad a eliminar: "))
                
                if cantidad >= item["cantidad"]:
                    carrito_de_compras.remove(item)
                else:
                    item["cantidad"] -= cantidad
                
                almacen = accesorios if item["clase"] == 'accesorios' else juegos
                almacen[codigo]["existencias"] += cantidad
                print(f" {cantidad} {almacen[codigo]['producto']} eliminado(s)")
                break
        else:
            print("Producto no encontrado en el carrito")

    elif opcion == "5":
        if not carrito_de_compras:
            print("El carrito está vacío")
            continue
            
        total = 0
        print("\n Artículos seleccionados:")
        for item in carrito_de_compras:
            tienda = juegos if item["clase"] == 'juegos' else accesorios
            producto = tienda[item["codigo"]]
            subtotal = item["cantidad"] * item["precio_unitario"]
            total += subtotal
            print(f"{producto['producto']} x{item['cantidad']} | ${subtotal:.2f} | Almacén: {item['clase']}")
        
        print(f"\nTOTAL: ${total:.2f}")

    elif opcion == "6":
        if not carrito_de_compras:
            print("No hay artículos para comprar")
            continue
            
        print("\n Tu compra fue:")
        total = sum(item["cantidad"] * item["precio_unitario"] for item in carrito_de_compras)
        
        for item in carrito_de_compras:
            tienda = juegos if item["clase"] == 'juegos' else accesorios
            producto = tienda[item["codigo"]]
            print(f"- {producto['producto']} x{item['cantidad']} | ${item['cantidad'] * producto['presio']:.2f}")
        
        print(f"\nFecha: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M')}")
        print(f"Su cuenta es un total de: ${total:.2f}")
        print(f"Gracias por su compra. Vuelva pronto. N° de pedido: {random.randint(1000,9999)}")
        break

    elif opcion == "7":
        print("Saliendo de la tienda. Vuelva pronto.")
        break
        
    else:
        print("Opción inválida. Intenta de nuevo.")

