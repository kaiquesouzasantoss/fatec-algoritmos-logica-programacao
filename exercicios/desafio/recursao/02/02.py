def calcula_soma_decremental(num) -> int:
    if num > 1:
        return num + calcula_soma_decremental(num - 1)
    return num

num = int(input())

print(f'SOMATORIA: {calcula_soma_decremental(num)}')