from math import fabs

menu = [
    [1, "CARREGAR NOTAS"],
    [2, "RETIRAR NOTAS"],
    [3, "ESTATÍSTICAS"],
    [9, "FIM"]
]

bancos = [
    [1, "BANCO DO BRASIL"],
    [2, "SANTANDER"],
    [3, "ITAÚ"],
    [4, "CAIXA"]
]

valor_notas = [2, 5, 10, 20, 50, 100]

# Matriz tridimensional: [banco][atributo][valores]
caixas = [
    [
        [0 for _ in range(6)],  # Notas
        [0],                    # Saldo inicial
        [0],                    # Maior saque
        [float('inf')],         # Menor saque
        [0],                    # Soma dos saques
        [0],                    # Média dos saques
        [0]                     # Contador de saques
    ] for _ in bancos
]

banco_atual = 0

def escolher_banco():
    global banco_atual
    exibe_titulo("SELECIONE O BANCO")

    [print(f"{banco[0]} - {banco[1]}") for banco in bancos]

    banco_atual = int(input("[REQUEST] ESCOLHA O BANCO: "))
    print(f"[INFO] BANCO SELECIONADO: {bancos[banco_atual][1]}")

def carrega_notas():
    exibe_titulo(menu[0][1])

    for i in range(6):
        quantidade = int(input(f"[REQUEST] DIGITE A QUANTIDADE DE NOTAS DE R$ {valor_notas[i]},00: "))
        caixas[banco_atual][0][i] = quantidade

    caixas[banco_atual][1][0] = sum(caixas[banco_atual][0][i] * valor_notas[i] for i in range(6))
    print("[SUCCESS] NOTAS CARREGADAS.")

def retira_notas():
    exibe_titulo(menu[1][1])
    saque = 0

    for i in range(6):
        quantidade = int(input(f"[REQUEST] DIGITE A QUANTIDADE DE NOTAS DE R$ {valor_notas[i]},00: "))

        if quantidade > caixas[banco_atual][0][i]:
            print(f"[WARNING] NÃO HÁ NOTAS SUFICIENTES DE R$ {valor_notas[i]},00. DISPONÍVEL: {caixas[banco_atual][0][i]}")
            quantidade = caixas[banco_atual][0][i]

        caixas[banco_atual][0][i] -= quantidade
        saque += quantidade * valor_notas[i]

    if saque > 0:
        caixas[banco_atual][2][0] = max(caixas[banco_atual][2][0], saque)
        caixas[banco_atual][3][0] = min(caixas[banco_atual][3][0], saque)
        caixas[banco_atual][6][0] += 1
        print(f"[SUCCESS] SAQUE DE R$ {saque} REALIZADO.")
    else:
        print("[INFO] NENHUMA NOTA FOI RETIRADA.")

def sumarizacao():
    exibe_titulo(menu[2][1])
    saldo_final = sum(caixas[banco_atual][0][i] * valor_notas[i] for i in range(6))

    if caixas[banco_atual][6][0] > 0:
        caixas[banco_atual][4][0] = fabs(saldo_final - caixas[banco_atual][1][0])
        caixas[banco_atual][5][0] = caixas[banco_atual][4][0] / caixas[banco_atual][6][0]

    print(f"[INFO] MAIOR: R$ {caixas[banco_atual][2][0]}")
    print(f"[INFO] MENOR: R$ {caixas[banco_atual][3][0] if caixas[banco_atual][3][0] != float('inf') else 0}")
    print(f"[INFO] SOMA: R$ {caixas[banco_atual][4][0]}")
    print(f"[INFO] MÉDIA: R$ {caixas[banco_atual][5][0]}")
    print(f"[INFO] SALDO DO CAIXA: R$ {saldo_final}")

def encerra_operacao():
    exibe_titulo("ENCERRANDO CAIXA")
    exit()

def gerencia_operacao():
    while True:
        exibe_menu()
        exibe_titulo("OPERAÇÃO")

        try:
            operacao = int(input("[REQUEST] ESCOLHA UMA OPÇÃO: "))
        except ValueError:
            print("[ERROR] ENTRADA INVÁLIDA.")
            continue

        match operacao:
            case 1:
                carrega_notas()
            case 2:
                retira_notas()
            case 3:
                sumarizacao()
            case 9:
                encerra_operacao()
            case _:
                print("[ERROR] OPÇÃO INVÁLIDA.")

def exibe_menu():
    exibe_titulo("MENU PRINCIPAL")

    for item in menu:
        print(f'{item[0]} - {item[1]}')

def exibe_titulo(texto):
    print(f"{'-' * 10}| {texto} |{'-' * 10}")

if __name__ == "__main__":
    exibe_titulo("CAIXA ELETRÔNICO")
    escolher_banco()
    gerencia_operacao()