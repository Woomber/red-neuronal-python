from typing import List
from perceptron_multicapa import peso_aleatorio, sigmoide, d_sigmoide


class Neurona:
    def __init__(self):
        self.entradas: List[float] = []
        self.pesos: List[float] = []
        self.sesgo: float = peso_aleatorio()

    def add_entrada(self):
        self.entradas.append(0.)
        self.pesos.append(peso_aleatorio())

    def num_entradas(self):
        return len(self.entradas)

    def salida(self):
        suma = 0.

        for idx, entrada in enumerate(self.entradas):
            suma += entrada * self.pesos[idx]

        return suma + self.sesgo
