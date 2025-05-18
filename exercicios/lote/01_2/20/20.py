import math

def calcula_delta(a, b, c):
    return (b * b) - 4 * a * c

def calcula_x(a, b, delta, sinal):
    return (-b + sinal * math.sqrt(delta)) / (2 * a)

a, b, c = float(input()), float(input()), float(input())

delta = calcula_delta(a, b, c)

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    print(f'X1 = {calcula_x(a, b, delta, 1)} | X2 = {calcula_x(a, b, delta, -1)}')