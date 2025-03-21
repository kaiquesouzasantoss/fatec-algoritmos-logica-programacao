possibilidade = 0

for n in range(1, 7):
    for j in range(1, 7):
        if (n + j) == 7:
            possibilidade += 1
            print(f'{n} + {j} = 7')