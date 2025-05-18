def ajusta_salario(salario, percentual = 1.15):
    return round(salario * percentual, 2)

salario = float(input())

print(f'R$ {(ajusta_salario(salario))}')