from math import e as _e
from perceptron_multicapa.neurona import Neurona
from perceptron_multicapa.capa import Capa
from perceptron_multicapa.perceptron import Perceptron
from random import uniform


factor = 0.4


def peso_aleatorio():
    return uniform(0., 1.)


def sigmoide(x):
    return 1./(1.+pow(_e, -x))


def d_sigmoide(x):
    return sigmoide(x) * (1. - sigmoide(x))
