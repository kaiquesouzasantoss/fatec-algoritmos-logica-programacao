def multiplicao(numero, vezes):
    return numero * vezes

num = int(input())

for n in range(1, 11):
    print(f'{num} x {n} = {multiplicao(num, n)}')