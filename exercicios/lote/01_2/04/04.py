def celsius_fahr(celsius):
    return ((9 * celsius) + 160) / 5

celsius = float(input())

print(f'{celsius_fahr(celsius)}')