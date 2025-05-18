num_a, num_b = int(input()), int(input())

def verifica_multiplo(x, y):
    return x % y == 0

def verifica_maior(x, y):
    return x >= y

if (verifica_maior(num_a, num_b) and verifica_multiplo(num_a, num_b)):
    print(f'A ({num_a}) É MAIOR E MULTIPLO DE B!')
elif (verifica_maior(num_b, num_a) and verifica_multiplo(num_b, num_b)):
    print(f'B ({num_b}) É MAIOR E MULTIPLO DE A!')