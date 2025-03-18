hora_inicial, minuto_inicial = int(input()), int(input())
hora_final, minuto_final = int(input()), int(input())

hora_duracao = hora_final - hora_inicial
minuto_duracao = minuto_final - minuto_inicial

if hora_duracao < 0:
    hora_duracao += 24

if minuto_duracao < 0:
    minuto_duracao += 60
    hora_duracao -= 1

print(f"TEMPO: {hora_duracao}:{minuto_duracao}")
