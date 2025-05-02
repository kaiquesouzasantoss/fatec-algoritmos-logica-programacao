def calcula_soma(num) -> int:
    if num < 100:
        return num + calcula_soma(num + 1)
    return num

print(f'SOMATORIA: {calcula_soma(num = 1)}')