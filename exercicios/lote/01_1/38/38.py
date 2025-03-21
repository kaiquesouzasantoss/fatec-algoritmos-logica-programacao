maior, menor = 0,0

for n in range(1, 101):
    num = int(input())

    if n == 1:
        maior, menor = num, num

    if num > maior:
        maior = num

    if num < menor:
        menor = num

print(f'MAIOR = {maior} | MENOR = {menor}')