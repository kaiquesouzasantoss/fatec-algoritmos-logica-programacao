def expoenencia(base, expoente):
    return base ** expoente

base, expoente = int(input()), int(input())

for numero in range(1, expoente + 1):
    print(f'{base} x {numero} = {expoenencia(base, numero)}')