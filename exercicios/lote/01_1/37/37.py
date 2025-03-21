num = int(input())

atual, termo, posterior = 0, 1, 1

while termo <= num:
    posterior += atual
    atual = posterior - atual
    print(f'TERMO = {termo} | ATUAL = {atual} | POSTERIOR = {posterior}')
    termo += 1
