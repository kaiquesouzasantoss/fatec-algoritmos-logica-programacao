def verifica_possibilidades(inicial, final):
    for n in range(inicial, final):
        for j in range(inicial, final):
            if (n + j) == 7:
                print(f'{n} + {j} = 7')

verifica_possibilidades(1, 7)