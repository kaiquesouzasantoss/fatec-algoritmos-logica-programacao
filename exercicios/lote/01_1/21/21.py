nota_a, nota_b, nota_c, nota_d = float(input()), float(input()), float(input()), float(input())

media = sum([nota_a, nota_b, nota_c, nota_d]) / 4

if media < 3:
    print("RETIDO")
elif media >= 6:
    print("APROVADO")
else:
    print("EXAME")