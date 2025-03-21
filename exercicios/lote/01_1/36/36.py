num = int(input())
sum = 1

for cont in range(1, num+1):
    fatorial = 1
    cont_inicial = cont

    while cont_inicial > 0:
        fatorial *= cont_inicial
        cont_inicial -= 1

    print(f'1 / {cont}! = {1/fatorial}')
    sum += (1/fatorial)

print(f'SUM = {sum}')