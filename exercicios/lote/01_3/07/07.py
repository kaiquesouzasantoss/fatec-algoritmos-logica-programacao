def bubble(lista):
    tamanho = len(lista)

    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if lista[j] >  lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def search(numero, lista):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == numero:
            return "EXISTE"
        elif lista[meio] < numero:
            inicio = meio + 1
        else:
            fim = meio - 1
    return "NÃO EXISTE"

valores = list()
interacoes, soma = 20, 0

for i in range(interacoes):
    valores.append(int(input()))

valores = bubble(valores)

valor_procurado = int(input("[REQUEST] DIGITE UM VALOR A SER BUSCADO: "))

print(f'[INFO] O VALOR {valor_procurado} NA LISTA {search(valor_procurado, valores)}')