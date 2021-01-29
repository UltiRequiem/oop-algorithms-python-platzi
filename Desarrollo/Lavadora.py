class Lavadora:
    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self_lavar()
        self._centrifugar()
