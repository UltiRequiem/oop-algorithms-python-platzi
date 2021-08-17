class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada):
        x_diff = self.x - otra_coordenada.x
        y_diff = self.y - otra_coordenada.y
        return (x_diff ** 2 + y_diff ** 2) ** 0.5


def main():
    x1 = float(input("Introduce la coordenada x de tu primer punto: "))
    y1 = float(input("Introduce la coordenada y de tu primer punto: "))
    coordenada1 = Coordenada(x1, y1)
    print()
    x2 = float(input("Introduce la coordenada x del segundo punto: "))
    y2 = float(input("Introduce la coordenada y del segundo punto: "))
    otra_coordenada = Coordenada(x2, y2)
    print()
    distancia = coordenada1.distancia(otra_coordenada)
    print(
        f"La distancia entre el punto ({coordenada1.x}, {coordenada1.y}) y el punto ({otra_coordenada.x}, {otra_coordenada.y}) es {distancia}"
    )


if __name__ == "__main__":
    main()
