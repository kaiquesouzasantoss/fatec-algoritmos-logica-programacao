def retorna_maior(numero, maior):
    return max(numero, maior)

def retorna_menor(numero, menor):
    return min(numero, menor)

maior, menor = 0, 0

for n in range(0, 3):
    num = int(input())

    if n == 0:
        maior, menor = num, num

    maior = retorna_maior(num, maior)
    menor = retorna_menor(num, menor)

print(f'MAIOR = {maior} | MENOR = {menor}')