linhas, colunas = 200, 5
avaliacoes, media_provas, media_alunos = [], [], []

menu = [
    [1, "CARREGA AVALIAÇÕES"],
    [2, "CALCULA E MOSTRA MÉDIAS"],
    [3, "FINALIZA"]
]

def carrega_avaliacoes(linhas, colunas):
    avaliacoes = []

    for _ in range(linhas):
        aluno = []

        for _ in range(colunas):
            aluno.append(int(input()))
        avaliacoes.append(aluno)
    return avaliacoes

def sumariza_media_aluno(avaliacoes, linhas, colunas):
    media_aluno = []

    for linha in range(linhas):
        soma = 0

        for coluna in range(colunas):
            soma += avaliacoes[linha][coluna] 

        media_aluno.append(soma / colunas)
    
    return media_aluno

def sumariza_media_prova(avaliacoes, linhas, colunas):
    media_prova = []

    for coluna in range(colunas):
        soma = 0

        for linha in range(linhas):
            soma += avaliacoes[linha][coluna] 
        media_prova.append(soma / linhas)

    return media_prova

def calcula_media_aluno(media_alunos, colunas):
    media = 0 

    for coluna in range(colunas):
        media += media_alunos[coluna]

    return media / colunas

def calcula_media_prova(media_prova, colunas):
    media = 0 

    for coluna in range(colunas):
        media += media_prova[coluna]

    return media / colunas

def exibe_media_aluno(media_alunos, colunas):
    for coluna in range(colunas):
        print(f"ALUNO {coluna + 1} | MEDIA: {media_alunos[coluna]}")
    
def exibe_media_prova(media_provas, colunas):
    for coluna in range(colunas):
        print(f"PROVA {coluna + 1} | MEDIA: {media_provas[coluna]}")

def encerra():
    print("SIGA FINALIZADO!")

def exibe_menu():
    exibe_titulo("MENU PRINCIPAL")

    for item in menu:
        print(f'{item[0]} - {item[1]}')

def exibe_titulo(texto):
    print(f"{'-' * 10}| {texto} |{'-' * 10}")

def gerencia_operacao():
    global avaliacoes, media_alunos, media_alunos, linhas, colunas

    while True:
        exibe_menu()
        exibe_titulo("OPERAÇÃO")

        try:
            operacao = int(input("[REQUEST] ESCOLHA UMA OPÇÃO: "))
        except ValueError:
            print("[ERROR] OPÇÃO INVÁLIDA.")
            continue

        match operacao:
            case 1:
                exibe_titulo(menu[0][1])
                avaliacoes = carrega_avaliacoes(linhas, colunas)
            case 2:
                media_alunos = sumariza_media_aluno(avaliacoes, linhas, colunas)
                media_provas = sumariza_media_prova(avaliacoes, linhas, colunas)

                exibe_titulo(menu[1][1])

                print(f"MEDIA GERAL DOS ALUNOS: {calcula_media_aluno(media_alunos, linhas)}")
                print(f"MEDIA GERAL DAS PROVAS: {calcula_media_prova(media_provas, linhas)}")

                print(f"MEDIA DE CADA ALUNO: ")
                exibe_media_aluno(media_alunos, linhas)

                print(f"MEDIA DE CADA PROVA: ")
                exibe_media_prova(media_provas, linhas)
            case 3:
                encerra()
                exit(0)
            case _:
                print("[ERROR] OPÇÃO INVÁLIDA.")

if __name__ == "__main__":
    exibe_titulo("SIGA")
    gerencia_operacao()