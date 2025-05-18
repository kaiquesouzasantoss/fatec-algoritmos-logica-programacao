def calcula_fatorial(numero):
    fatorial = 1

    while numero > 1:
        fatorial *= numero
        numero -= 1

    return fatorial

num = int(input())

if num > 0:
    print(f'{num}! = {calcula_fatorial(num)}')