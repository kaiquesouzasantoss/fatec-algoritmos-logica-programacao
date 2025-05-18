import math

def calcula_comprimento(raio):
    return math.pi * raio ** 2

raio = float(input())

print(f'{calcula_comprimento(raio)}')