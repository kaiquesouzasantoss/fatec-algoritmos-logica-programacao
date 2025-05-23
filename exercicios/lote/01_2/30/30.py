from datetime import date

def calcular_idade(data_nascimento, data_atual):
    anos = data_atual.year - data_nascimento.year
    meses = data_atual.month - data_nascimento.month
    dias = data_atual.day - data_nascimento.day

    # Ajuste para dias negativos
    if dias < 0:
        meses -= 1
        dias += (date(data_atual.year, data_atual.month, 1) - date(data_atual.year, data_atual.month - 1, 1)).days

    # Ajuste para meses negativos
    if meses < 0:
        anos -= 1
        meses += 12

    return anos, meses, dias

dia_nascimento, mes_nascimento, ano_nascimento = map(int, input("DIGITE A DATA DE NASCIMENTO (dd/mm/yyyy): ").split("/"))

data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
data_atual = date.today()

anos, meses, dias = calcular_idade(data_nascimento, data_atual)
print(f"IDADE: {anos} anos | {meses} meses | {dias} dias.")
