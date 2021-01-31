class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')
        
        
class Conductor(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi auto')


def main():
    persona = Persona('David')
    persona.avanza()

    conductor = Conductor('Pedro')
    conductor.avanza()


if __name__ == '__main__':
    main()