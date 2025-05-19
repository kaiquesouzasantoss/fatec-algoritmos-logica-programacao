def retorna_exponencial(posicao):
    return 4 ** posicao

lista = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    x, y = i, i

    for j in range(4):
        if x == i and y == j:
            lista[x][y] = retorna_exponencial(x)
            continue

for i in range(4):
    print(lista[i])