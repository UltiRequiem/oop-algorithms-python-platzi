# Polimorfismo

El **polimorfismo** es la habilidad de tomar varias formas, en este caso la habilidad de cambiar el comportamiento de un método. En Python, nos permite cambiar el comportamiento de una _superclase_ para adaptarlo a la subclase solo nombrando el método y escribiendo su comportamiento.

```py
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    # Definimos el método avanzar.
    def avanza(self):
        print('Ando caminando')


# Ciclista extiende de Persona
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)


    # Para aplicar polimorfismo en el método de la superclase
    # simplemente definimos su comportamiento y nombrando el método.
    def avanza(self):
        print('Ando moviendome en mi bicicleta')


def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()
```

- [Capitulo Anterior](./11_Herencia.md)                                                                 

- [Capitulo Siguiente](./../02|ComplejidadAlgorítmica/13_IntroduccionLaComplejidadAlgoritimica.md)