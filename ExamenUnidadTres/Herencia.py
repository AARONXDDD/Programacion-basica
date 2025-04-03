# Herencia
# Clase base o padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# Clase derivada o hija
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase padre
        self.grado = grado

    def presentarse(self):
        # Sobrescribimos el método de la clase padre
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y estudio en {self.grado}."

# Otra clase derivada
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        return f"Hola, soy el profesor {self.nombre}, tengo {self.edad} años y enseño {self.materia}."

# Programa principal
if __name__ == "__main__":
    persona = Persona("Carlos", 40)
    estudiante = Estudiante("Ana", 20, "3er año de Ingeniería")
    profesor = Profesor("Luis", 50, "Matemáticas")

    print(persona.presentarse())
    print(estudiante.presentarse())
    print(profesor.presentarse())