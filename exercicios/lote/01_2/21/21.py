def calcula_media(notas):
    return sum(notas) / len(notas)

def retorna_status(media):
    if media < 3:
        return "RETIDO"
    elif media >= 6:
        return "APROVADO"
    else:
        return "EXAME"

media = calcula_media([float(input()) for _ in range(4)])

print(f'MÉDIA: {media} | STATUS: {retorna_status(media)}')