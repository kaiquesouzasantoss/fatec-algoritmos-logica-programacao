def calcula_velocidade_media(extensao, voltas, tempo):
    return round(((extensao / 1000) * voltas) / (tempo / 60), 2)

voltas, extensao, tempo = float(input()), float(input()), int(input())

print(f'{calcula_velocidade_media(extensao, voltas, tempo)} KM/H')