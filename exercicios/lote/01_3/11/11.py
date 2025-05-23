tamanho = 8
matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

valor_camada = 1

for camada in range((tamanho + 1) // 2):
    for indice in range(camada, tamanho - camada):
        matriz[camada][indice] = valor_camada
        matriz[tamanho - camada - 1][indice] = valor_camada
        matriz[indice][camada] = valor_camada
        matriz[indice][tamanho - camada - 1] = valor_camada
    valor_camada += 1

[print(matriz[linha]) for linha in range(tamanho)]