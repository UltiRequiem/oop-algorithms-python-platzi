class Perro():
    def __init__(self, nombre, color, raza):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.comida = 10

    def dormir(self):
        return 'zZZZzzzZZZzzzZZZ'

    def ladrar(self):
        return 'El perro dice wuao wuao'

    def comer(self, cantidad):
        self.comida = self.comida - cantidad
        return self.comida


if __name__ == '__main__':
    perro = Perro('Lucas', 'Negro', 'Bulldog')

    croquetas = int(input('¿Cuantas croquetas va a comer el perro? \n'))

    if croquetas < 10:
        print('El perro comio '+str(croquetas)+' croquetas.' +'Ahora al Perro le quedan '+str(perro.comer(croquetas))+' croquetas.')
    else:
        print('¡El perro No puede comer tantas Croquetas!')

# https://platzi.com/comentario/2224673
