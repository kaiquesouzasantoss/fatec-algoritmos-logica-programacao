sum, controle = 0, 0

for n in range(1, 16):
    termo = n / (n * n)

    if controle == 0:
        sum += termo
        controle = 1
    else:
        sum -= termo
        controle = 0

print(f'RESULTANTE = {sum}')