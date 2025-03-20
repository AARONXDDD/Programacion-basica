
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