tempo = 0
ana_cm = 1.1 * 100
maria_cm = 1.5 * 100

while ana_cm <= maria_cm:
    tempo += 1
    ana_cm += 3
    maria_cm += 2
    print(f'ANA = {ana_cm}CM | MARIA = {maria_cm}CM')

print(f'{tempo} ANOS')