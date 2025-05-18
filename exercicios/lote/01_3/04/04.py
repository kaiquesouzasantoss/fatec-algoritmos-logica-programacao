lista = list()
interacoes, media, acima_media, abaixo_media = 30, 0, 0, 0

for i in range(interacoes):
    lista.append(float(input()))

for item in lista:
    media += item

media = media / interacoes

for item in lista:
    if item >= media:
        acima_media += 1

    if item < media:
        abaixo_media += 1

print(f'MEDIA DO GRUPO: {media} | ACIMA/IGUAL A MEDIA: {acima_media} ps | ABAIXO DA MEDIA: {abaixo_media} ps')