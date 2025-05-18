def metro_centimentro(metro):
    return metro * 100

def calcula_tempo_crescimento(ana, maria):
    tempo = 0

    while ana <= maria:
        tempo += 1
        ana += 3
        maria += 2
        print(f'ANA = {ana}CM | MARIA = {maria}CM')
    return tempo

print(f'{calcula_tempo_crescimento(
    ana=metro_centimentro(1.1),
    maria=metro_centimentro(1.5)
)} ANOS')