num = int(input())

if num > 0:
    fatorial = 1
    num_inicial = num

    while num > 1:
        fatorial*=num
        num-=1

    print(f'{num_inicial}! = {fatorial}')