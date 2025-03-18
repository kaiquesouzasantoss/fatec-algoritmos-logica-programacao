preco_atual, media_mensal = float(input()), float(input())

if (media_mensal < 500) and (preco_atual < 30):
    print(f'NOVO PRECO: R$ {preco_atual * 1.1}')
elif (media_mensal >= 500) and (media_mensal < 1000) and (preco_atual >= 30) and (preco_atual < 80):
    print(f'NOVO PRECO: R$ {preco_atual * 1.15}')
elif (media_mensal >= 1000) and (preco_atual >= 80):
    print(f'NOVO PRECO: R$ {preco_atual * 0.95}')
else:
    print(f'NOVO PRECO: R$ {preco_atual}')