def calcula_consumo(tempo, velocidade, consumo_carro):
    return (tempo * velocidade) / consumo_carro

tempo_hora, velocidade_media = float(input()), float(input())

print(f'{calcula_consumo(tempo_hora, velocidade_media, 12)} L')