lista = list()

for i in range(50):
    lista.append(int(input()))

media_intervalo, contador_intervalo, soma_impares = 0, 0, 0

for item in lista:
    if item % 2 != 0: 
        soma_impares += item
    
    if item >= 10 and item <= 200:
        media_intervalo += item
        contador_intervalo += 1

media_intervalo = round(media_intervalo / contador_intervalo, 2)

print(f'MEDIA DO INTERVALO[10-200]: {media_intervalo}')
print(f'SOMA DOS IMPARES: {soma_impares}')