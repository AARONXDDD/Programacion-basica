# Herencia
# Clase base o padre
class electronico:
    def __init__(self, pantalla, prosesador, ):
        self.pantalla = pantalla
        self.prosesador = prosesador

    def presentacion(self):
        return f"Nuestros electronicos {self.pantalla} y tenen{self.prosesador}."

# Clase derivada o hija
class Celular(electronico):
    def __init__(self, pantalla, prosesador, camara):
        super().__init__(pantalla, prosesador)  # Llamada al constructor de la clase padre
        self.camara = camara

    def presentacion(self):
        # Sobrescribimos el método de la clase padre
        return f"Este celular tienes esta carracteristica {self.pantalla}, tiene un{self.prosesador} y {self.camara} de 50mpx."

# Otra clase derivada
class computadora(electronico):
    def __init__(self, pantalla, prosesador, teclado):
        super().__init__(pantalla, prosesador)
        self.teclado = teclado

    def presentarse(self):
        return f"Eata computadora es {self.pantalla}, tiene un {self.prosesador} y {self. teclado}."

# Programa principal
if __name__ == "__main__":
    electronico = electronico("elecronicos", "texturizado")
    celular = celular("Amoled", "elite 855", "camara de 50mpx")
    computadora = computadora("full hd 32", "intel 9", "teclado mecanico")

    print(electronico.presentacion())
    print(celular.presentacion())
    print(computadora.presentacion())