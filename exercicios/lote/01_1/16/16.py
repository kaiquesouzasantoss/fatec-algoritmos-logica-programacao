horas, valor_hora, desconto, dependentes = int(input()), float(input()), float(input()), int(input())

salario_bruto = horas * valor_hora
salario_liquido = round(
    (salario_bruto - (salario_bruto * (desconto / 100))),
    3
)
salario_liquido = (salario_liquido + (dependentes * 100))

print(f'SALARIO LIQUIDO: R$ {salario_liquido}')