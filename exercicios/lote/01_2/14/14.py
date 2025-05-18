def angulo_complementar(ang_01, ang_02):
    return 180 - (angulo_01 + angulo_02)

angulo_01, angulo_02 = float(input()), float(input())

print(f'3° ANGULO: {angulo_complementar(angulo_01, angulo_02)}')