def verifica_divisivel(dividendo, divisor):
    return dividendo % divisor == 0

numero = int(input())

if (verifica_divisivel(numero, 2)) and (verifica_divisivel(numero, 3)):
    print("DIVISIVEL POR 2 E 3!")
else:
    print("NÃO É DIVISIVEL POR 2 E 3")