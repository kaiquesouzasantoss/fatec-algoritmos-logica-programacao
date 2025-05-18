ano_nascimento, ano_atual = int(input()), int(input())

def calcula_idade(ano_atual, ano_nascimento):
    return ano_atual - ano_nascimento

idade = calcula_idade(ano_atual, ano_nascimento)
idade_futura = idade + 17

print(f'IDADE: {idade} ANOS | FUTURO: {idade_futura} ANOS') 