def calcula_soma(num, denominador) -> float:
    # print(f'1/{denominador}')

    if denominador < num:
        return (1/denominador) + calcula_soma(num, denominador + 1)
    return (1/denominador)

num = int(input())

print(f'SOMATORIA: {round(calcula_soma(num, 1), 2)}')