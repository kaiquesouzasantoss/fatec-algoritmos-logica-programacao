preco_atual, media_mensal = float(input()), float(input())

def reajusta_preco(preco, percentual):
    return preco * (percentual / 100)

if (media_mensal < 500) and (preco_atual < 30):
    print(f'NOVO PRECO: R$ {reajusta_preco(preco_atual, 100)}')
elif (media_mensal >= 500) and (media_mensal < 1000) and (preco_atual >= 30) and (preco_atual < 80):
    print(f'NOVO PRECO: R$ {reajusta_preco(preco_atual, 150)}')
elif (media_mensal >= 1000) and (preco_atual >= 80):
    print(f'NOVO PRECO: R$ {reajusta_preco(preco_atual, 95)}')
else:
    print(f'NOVO PRECO: R$ {preco_atual}')