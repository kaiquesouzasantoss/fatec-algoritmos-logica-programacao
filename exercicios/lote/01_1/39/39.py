grao, sum = 1, 1

for n in range(1, 65):
    grao *= 2
    # print(f'{grao} x 2 = {sum + grao}')
    sum += grao

print(f'SOMA DE GRAOS = {sum}')