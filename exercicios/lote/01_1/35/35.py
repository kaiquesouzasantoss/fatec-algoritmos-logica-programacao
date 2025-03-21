num_a, num_b = int(input()), int(input())
maior, menor = 0, 0

if num_a >= num_b:
    maior = num_a
    menor = num_b
else:
    maior = num_b
    menor = num_a

sum = 0

while menor < maior:
    if menor % 2 != 0:
        print(f'{menor} + {sum} = {sum+menor}')
        sum += menor
    menor += 1
print(f'SUM = {sum}')