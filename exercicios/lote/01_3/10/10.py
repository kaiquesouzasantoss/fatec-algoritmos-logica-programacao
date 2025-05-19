lista = [[0 for _ in range(8)] for _ in range(2)]

for i in range(len(lista[0])):
    lista[0][i] = i + 1

lista[1][0] = 1

for i in range(1, len(lista[1])):
    lista[1][i] = lista[1][i-1] * 2

for i in range(2):
    print(lista[i])

print(f'SOMA DE CASAS: {sum(lista[0])}')
print(f'SOMA DE VALORES: {sum(lista[1])}')