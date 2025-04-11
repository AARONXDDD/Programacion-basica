# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con algunos elementos
estudiantes = {
    "Juan": 20,
    "Ana": 22,
    "Luis": 19
}

# Acceder a un valor usando una clave
print("Edad de Juan:", estudiantes["Juan"])

# Agregar un nuevo par clave-valor
estudiantes["Maria"] = 21
print("Diccionario después de agregar a Maria:", estudiantes)

# Modificar un valor existente
estudiantes["Ana"] = 23
print("Diccionario después de modificar la edad de Ana:", estudiantes)

# Eliminar un par clave-valor
del estudiantes["Luis"]
print("Diccionario después de eliminar a Luis:", estudiantes)

# Iterar sobre un diccionario
print("Iterar sobre el diccionario:")
for nombre, edad in estudiantes.items():
    print(f"{nombre} tiene {edad} años")

# Verificar si una clave existe en el diccionario
if "Juan" in estudiantes:
    print("Juan está en el diccionario")

# Obtener todas las claves del diccionario
claves = estudiantes.keys()
print("Claves del diccionario:", claves)

# Obtener todos los valores del diccionario
valores = estudiantes.values()
print("Valores del diccionario:", valores)

# Obtener todos los pares clave-valor del diccionario
items = estudiantes.items()
print("Pares clave-valor del diccionario:", items)
 