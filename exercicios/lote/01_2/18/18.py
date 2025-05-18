def subtracao(x, y):
    return x - y

def ordena_valores(x, y):
    lista = [x, y]
    lista.reverse()
    return lista

num_a, num_b = int(input()), int(input())

valores = ordena_valores(num_a, num_b)

print(f'{valores[0]} - {valores[1]} = {subtracao(valores[0], valores[1])}')