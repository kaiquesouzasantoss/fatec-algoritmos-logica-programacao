num_a, num_b = int(input()), int(input())

maior = max(num_a, num_b)
menor = min(num_a, num_b)

primo_possibilidade, sum = 0, 0

while menor <= maior:
    for n in range(1, menor+1):
        if menor % 2 == 0:
            primo_possibilidade += 1

    if primo_possibilidade <= 2:
        print(f'{sum} + {menor} = {sum + menor}')
        sum += menor

    menor += 1
    primo_possibilidade = 0
print(f'SOMA = {sum}')