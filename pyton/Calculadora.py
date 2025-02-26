def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def menu():
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

while True:
    menu()
    opcion = input("Ingrese su opción (1/2/3/4/5): ")

    if opcion == '5':
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción no válida, por favor intente de nuevo.")