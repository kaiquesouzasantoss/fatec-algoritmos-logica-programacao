def calcula_soma_reciprocos(numero):
    soma = 0

    for i in range(1, numero + 1):
        soma += 1 / i

    '''
        i, soma = 1, 0
        
        while (i <= numero):
        soma += (1/i)
        i += 1
    '''

    return round(soma, 2)

numero = int(input())

if numero > 0:
    print(f'SUM = {calcula_soma_reciprocos(numero)}')