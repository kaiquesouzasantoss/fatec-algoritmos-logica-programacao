def soma_termos(numerador, denominador_final):
    soma = 0
    
    for denominador in range(1, denominador_final, 2):
        print(f'{numerador} / {denominador} = {round(numerador/denominador, 2)}')
        soma += (numerador/denominador)
        numerador += 1

    return round(soma, 2)

print(f'SOMA = {soma_termos(1, 100)}')