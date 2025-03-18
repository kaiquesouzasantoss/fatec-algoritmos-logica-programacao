from math import sqrt

cateto_01, cateto_02 = float(input()), float(input())

hipotenusa = round(
    sqrt((cateto_01 * cateto_01) + (cateto_02 * cateto_02)),
    4
)

print(f'HIPOTENUSA: {hipotenusa}')