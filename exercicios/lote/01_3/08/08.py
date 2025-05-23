produtos = list()
soma_mensal = 0

[produtos.append(list(map(int, input().split(" ")))) for _ in range(4)]

print("-" * 40)

for coluna in range(3):
    soma_semanal = 0

    for linha in range(4):
        soma_semanal += produtos[linha][coluna]
    soma_mensal += soma_semanal

    print(f'PRODUTO: {coluna+1} | {soma_semanal} UNIDADES')

print("-" * 40)

[print(f'SEMANA {linha+1}: {sum(produtos[linha])} UNIDADES VENDIDAS') for linha in range(4)]

print("-" * 40)

print(f"PRODUTOS VENDIDOS MENSALMENTE: {soma_mensal} UNIDADES")