lista_del_mandado = []

while True:
    print("\n deseas crear lista del mandado?")
    print("1. si")
    print("2. no")

    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        producto1 = input("agrega productos a tu carrito de compras: ")
        lista_del_mandado.append(producto1)
        print(f"✅ producto '{producto1}' agregado.")

        producto2 = input("agrega productos a tu carrito de compras: ")
        lista_del_mandado.append(producto2)
        print(f"✅ producto '{producto2}' agregado.")

        producto3 = input("agrega productos a tu carrito de compras: ")
        lista_del_mandado.append(producto3)
        print(f"✅ producto '{producto3}' agregado.")

        producto4 = input("agrega productos a tu carrito de compras: ")
        lista_del_mandado.append(producto4)
        print(f"✅ producto '{producto4}' agregado.")

    elif opcion == "2":
        print("saliendo del programa")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")

    
    print("\n Tu lista del mando  es:")
    for producto in lista_del_mandado:
        print(f"- {producto}")
        

   