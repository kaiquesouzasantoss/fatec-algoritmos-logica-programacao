potencia, base, expoente = 1, int(input()), int(input())

while expoente > 0:
    print(f'{base} x {expoente} = {base * expoente}')
    potencia *= base
    expoente -= 1
print(f'POTENCIA = {potencia}')