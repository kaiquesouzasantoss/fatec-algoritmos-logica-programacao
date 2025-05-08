lista = list()
interacoes, soma = 20, 0

for i in range(interacoes):
    lista.append(int(input()))

for i in range(interacoes/2):
    soma += lista[i] + lista[interacoes]
    interacoes -= 1

print(f'SOMA = {soma}')