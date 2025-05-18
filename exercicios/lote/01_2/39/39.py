def calcula_soma_graos(soma, grao, quantidade_graos):
    for _ in range(1, quantidade_graos + 1):
        grao *= 2
        # print(f'{grao} x 2 = {soma + grao}')
        soma += grao
    return soma

print(f'SOMA DE GRAOS = {calcula_soma_graos(0, 1, 64)}')