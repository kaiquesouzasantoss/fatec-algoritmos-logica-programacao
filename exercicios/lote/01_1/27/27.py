voltas, extensao, tempo = float(input()), float(input()), int(input())
velocidade = ((extensao / 1000) * voltas) / (tempo / 60)

print(f'{velocidade} KM/H')