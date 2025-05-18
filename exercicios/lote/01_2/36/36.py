def fatorial(numero):
    if numero > 1:
        return numero * fatorial(numero - 1)
    return numero

num = int(input())
sum = 0

for contador in range(1, num+1):
    # print(f'1 / {contador}! = {1/fatorial(contador)}')
    sum += (1 / fatorial(contador))

print(f'SOMA = {round(sum, 2)}')