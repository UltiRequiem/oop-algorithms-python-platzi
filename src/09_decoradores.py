def decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)")

    return wrapper


@decoradora
def zumbido():
    print("Buzzzzzz")


zumbido()
