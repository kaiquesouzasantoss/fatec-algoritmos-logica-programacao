tipo_investimento, valor = int(input()), float(input())

if tipo_investimento == 1:
    print(f'R$ {valor * 1.03}')
elif tipo_investimento == 2:
    print(f'R$ {valor * 1.05}')