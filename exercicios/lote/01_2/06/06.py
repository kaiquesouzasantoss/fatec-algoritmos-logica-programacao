def inversao_valores(x, y):
    auxiliar = x
    x = y
    y = auxiliar

    return [x, y]

x, y = int(input()), int(input())

retorno = inversao_valores(x, y)

print(f'X = {retorno[0]} | Y = {retorno[1]}')