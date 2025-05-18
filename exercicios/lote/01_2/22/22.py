def ordena_valores(x, y):
    lista = [x, y]
    lista.reverse()
    return lista

num_a, num_b = int(input()), int(input())

if num_a != num_b:
    print(ordena_valores(num_a, num_b))
else:
    print("OS NÚMEROS SÃO IGUAIS!") 