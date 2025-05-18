def calcula_divisor_quadrado(numero):
    print(f'{numero} / {numero * numero}')
    return numero / (numero * numero)

def inverte_controle(controle):
    return not controle

def soma_intervalo(inicial, final):
    soma, controle = 0, True

    for n in range(inicial, final + 1):
        termo = calcula_divisor_quadrado(n)

        if controle:
            soma += termo
        else:
            soma -= termo

        controle = inverte_controle(controle)
    return round(soma, 2)

print(f'RESULTANTE = {soma_intervalo(1, 15)}')