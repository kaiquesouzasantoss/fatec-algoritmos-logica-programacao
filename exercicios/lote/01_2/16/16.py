horas, valor_hora, desconto, dependentes = int(input()), float(input()), float(input()), int(input())

def calcula_salario_bruto(horas, valor_hora):
    return horas * valor_hora

def calcula_salario_liquido(salario_bruto, desconto, dependentes):
    return (round(
        (salario_bruto - (salario_bruto * (desconto / 100)))
        , 3
    ) + (dependentes * 100))

print(f'SALARIO LIQUIDO: R$ {
    calcula_salario_liquido(
        calcula_salario_bruto(horas, valor_hora),
        desconto, dependentes
    )
}')