def soma_numeros_primos(maior, menor):
    soma, primo_possibilidade = 0, 0

    for numero in range(menor, maior+1):
        for divisor in range(1, numero+1):
            if numero % divisor == 0:
                primo_possibilidade += 1

        if primo_possibilidade <= 2:
            # print(f'{soma} + {numero} = {soma + numero}')
            soma += numero

        primo_possibilidade = 0
    
    return soma

entradas = [int(input()) for _ in range(2)]

print(f'SOMA = {soma_numeros_primos(max(entradas), min(entradas))}')