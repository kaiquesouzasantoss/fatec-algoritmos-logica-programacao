tamanho = 8
tabuleiro = []
soma_pecas = tamanho ** 2
contagem_vazio = 0

[tabuleiro.append(list(map(int, input().split(" ")))) for _ in range(tamanho)]

for linha in range(tamanho):
    contagem_vazio += tabuleiro[linha].count(7)

print("-" * 40)
print(f'TOTAL DE PECAS: {soma_pecas - contagem_vazio}')