def bubble(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] >  lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

lista = list()
interacoes, soma = 20, 0

for i in range(interacoes):
    lista.append(int(input()))

print(bubble(lista))