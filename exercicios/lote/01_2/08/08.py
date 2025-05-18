def calcula_rendimento(deposito):
    return round(deposito * 1.13, 2)

deposito = float(input())

print(f'RENDIMENTO: R$ {calcula_rendimento(deposito)}')