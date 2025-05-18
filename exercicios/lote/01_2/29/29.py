def calcula_rendimento(valor, percentual):
    print(percentual/100)
    return valor * (percentual / 100)

def retorna_rentabilidade_investimento(tipo):
    if tipo == 1:
        return 103
    elif tipo == 2:
        return 105
    return 100

tipo_investimento, valor = int(input()), float(input())

print(f'R$ {
    calcula_rendimento(
        valor, retorna_rentabilidade_investimento(tipo_investimento)
    )
}')