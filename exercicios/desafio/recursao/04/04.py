def calcula_soma(num, numerador, denominador) -> float:
    if numerador > 1:
        # print(f'{numerador}/{denominador}')
        return (numerador / denominador) + calcula_soma(num, numerador - 1, denominador + 1)
    # print(f'{numerador}/{num}')
    return (numerador/num)

num = int(input())

print(f'SOMATORIA: {round(calcula_soma(num, num, 1), 2)}')