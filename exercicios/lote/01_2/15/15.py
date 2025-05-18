from math import sqrt

cateto_01, cateto_02 = float(input()), float(input())

def calcula_hipotenusa(catato_01, cateto_02):
    return round(
    sqrt(
        (cateto_01 * cateto_01) + (cateto_02 * cateto_02)
        ),4
)

print(f'HIPOTENUSA: {calcula_hipotenusa(cateto_01, cateto_02)}')