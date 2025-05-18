num = int(input())

def fibonnaci(numero):
    atual, termo, posterior = 0, 1, 1

    while termo <= numero:
        posterior += atual
        atual = posterior - atual
        print(f'TERMO = {termo} | ATUAL = {atual} | POSTERIOR = {posterior}')
        
        termo += 1
fibonnaci(num)