def fatorial(num) -> int:
    # print(f'FAT: {num}')

    if num > 1:
        return num * fatorial(num - 1)
    return num

def calcula_soma(num) -> int:
    # print(f'CS: {num}')

    if num > 1:
        return fatorial(num) + calcula_soma(num - 1)
    return fatorial(num)

num = int(input())

print(f'SOMATORIA: {calcula_soma(num)}')