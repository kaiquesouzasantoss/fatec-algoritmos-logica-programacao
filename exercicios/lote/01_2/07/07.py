def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

comprimento, largura, altura = float(input()), float(input()), float(input())

print(f'VOLUME = {calcula_volume(comprimento, largura, altura)}')