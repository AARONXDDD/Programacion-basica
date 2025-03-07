# Lista vacía para almacenar las tareas
tareas = []

while True:
    print("\n📋 MENÚ DE TAREAS 📋")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("📝 Escribe la nueva tarea: ")
        tareas.append(tarea)
        print(f"✅ Tarea '{tarea}' agregada.")

    elif opcion == "2":
        if not tareas:
            print("📭 No hay tareas pendientes.")
        else:
            print("\n📌 Lista de Tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

    elif opcion == "3":
        if not tareas:
            print("📭 No hay tareas para completar.")
        else:
            num = int(input("🔹 Número de la tarea completada: ")) - 1
            if 0 <= num < len(tareas):
                print(f"✔️🤓 Tarea '{tareas[num]}' completada y eliminada.")
                tareas.pop(num)
            else:
                print("❌  Número inválido.")

    elif opcion == "4":
        if not tareas:
            print("📭 No hay tareas para eliminar.")
        else:
            num = int(input("🗑️ Número de la tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                print(f"🗑️ Tarea '{tareas[num]}' eliminada.")
                tareas.pop(num)
            else:
                print("❌ Número inválido.")

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")