def criar_matriz():
    matriz = []
    quant_linha = int(input("Digite a quantidade de linhas da matriz: "))
    quant_colunas = int(input("Digite a quantidade de colunas da matriz: "))

    for linha in range(quant_linha):
        lmatriz = []
        for coluna in range(quant_colunas):
            lmatriz.append(float(input(f"Valor da linha {linha + 1} coluna {coluna + 1}: ")))
        matriz.append(lmatriz)

    return matriz

def printar_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            valor = valor if valor != -0 else 0
            print(f"{valor:.1f}", end="\t")
        print()

def inverter_linhas(matriz, l1, l2):
    matriz[l1], matriz[l2] = matriz[l2], matriz[l1]

def multiplicar_linha(matriz, l, valor):
    for coluna in range(len(matriz[l])):
        matriz[l][coluna] *= valor

def multiplicar_e_somar_linha(matriz, l1, l2, valor):
    for coluna in range(len(matriz[l1])):
        matriz[l2][coluna] += matriz[l1][coluna] * valor

def calcular_escala(matriz, linha, coluna):
    if matriz[linha][coluna] == 0:
        for i in range(linha + 1, len(matriz)):
            if matriz[i][coluna] != 0:
                inverter_linhas(matriz, linha, i)
                break

    pivot = matriz[linha][coluna]
    if pivot != 0:
        multiplicar_linha(matriz, linha, 1 / pivot)

        for i in range(len(matriz)):
            if i != linha and matriz[i][coluna] != 0:
                multiplicar_e_somar_linha(matriz, linha, i, -matriz[i][coluna])

def organizar_linhas(matriz):
    matriz.sort(key=lambda row: row.index(next(filter(lambda x: x != 0, row), None)))

def escalonar_linha(matriz):
    for linha in range(len(matriz)):
        calcular_escala(matriz, linha, linha)
        organizar_linhas(matriz)

    return matriz

def main():
    matriz = criar_matriz()

    print("\nMatriz Normal:")
    printar_matriz(matriz)

    matriz_escalonada = escalonar_linha(matriz.copy())

    print("\nMatriz Escalonada:")
    printar_matriz(matriz_escalonada)

if __name__ == "__main__":
    main()
