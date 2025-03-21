soma, numerador, denominador = 0, 1, 1

while denominador < 100:
    print(f'{numerador} / {denominador} = {round(numerador/denominador, 2)}')
    soma += (numerador/denominador)
    numerador += 1
    denominador += 2

print(f'SOMA = {round(soma, 2)}')