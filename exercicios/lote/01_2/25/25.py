hora_inicial, minuto_inicial = int(input()), int(input())
hora_final, minuto_final = int(input()), int(input())

def subtracao(final, inicial):
    return final - inicial

def calcula_hora(duracao_hora):
    if duracao_hora < 0:
        return 24 + duracao_hora
    return duracao_hora

def calcula_minuto(duracao_hora, duracao_minuto):
    if duracao_hora < 0:
        return [duracao_hora - 1, duracao_minuto + 60]
    return [duracao_hora, duracao_minuto]

tempo = calcula_minuto(
    duracao_hora=calcula_hora(subtracao(hora_final, hora_inicial)),
    duracao_minuto=subtracao(minuto_final, minuto_inicial)
)


print(f"TEMPO: {tempo[0]:02d}:{tempo[1]:02d}")