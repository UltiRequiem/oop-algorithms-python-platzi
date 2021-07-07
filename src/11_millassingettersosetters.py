class Millas:
    def __init__(self, distancia=0):
        self.distancia = distancia

    def convertir_a_kilometros(self):
        return self.distancia * 1.609344


if __name__ == "__main__":
    avion = Millas()
    avion.distancia = int(input("¿Cuantas millas vas a viajar? "))

    print("Tus " + str(avion.distancia) + " millas equivalen a:")
    print(str(avion.convertir_a_kilometros()) + " Kilometros.")
