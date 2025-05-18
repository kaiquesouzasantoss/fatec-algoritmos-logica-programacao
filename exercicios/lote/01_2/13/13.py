def distribui_comida(quilos, gramas_dia):
    return int((quilos * 1000) / gramas_dia)

quilo_alimento = float(input())

print(f'{distribui_comida(quilo_alimento, 50)} DIAS')