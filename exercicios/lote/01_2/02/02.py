lista = list()
iteracoes = 100

for i in range(iteracoes):
    lista.append(int(input()))

maior, menor, media = lista[0], lista[0], 0

for item in lista:
    if item > maior:
        maior = item
    
    if item < menor:
        menor = item

    media += item

media = round(media / iteracoes, 2)

print(f'MAIOR: {maior} | MENOR: {menor} | MEDIA: {media}')