def calcula_soma_impares(entradas):
    maior, menor, soma = max(entradas), min(entradas), 0

    while menor < maior:
        if menor % 2 != 0:
            soma += menor
        menor += 1

    return soma

entradas = [int(input()) for _ in range(2)]
print(f'SOMA DOS IMPARES = {calcula_soma_impares(entradas)}')