from perceptron_multicapa import Neurona, sigmoide, d_sigmoide
from typing import List


class Capa:
    def __init__(self, es_ultima=False):
        self.neuronas: List[Neurona] = []
        self.es_ultima: bool = es_ultima

    def add_neurona(self):
        neurona = Neurona()
        self.neuronas.append(neurona)
        return neurona

    def deltas(self, esperados=None, ):
        deltas = []
        if self.es_ultima:
            for idx, neurona in enumerate(self.neuronas):
                resultado = neurona.salida()
                delta = - (sigmoide(esperados[idx]) - sigmoide(resultado)) * d_sigmoide(resultado)
                deltas.append(delta)
            return deltas



        return d_sigmoide(res_anterior) * deltas_pesos
