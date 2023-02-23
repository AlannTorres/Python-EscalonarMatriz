import math

# Metodo Eliminação de Gauss
matriz = []
quantLinha = int(4) # quantLinha = int(input("Digite a quantidade de linhas:"))
quantColunas = int(5) # quantColunas = int(input("Digite a quantidade de colunas:"))

# Printar matriz
def PrintarMatriz():
    print("--------------------")
    for linha in matriz:
        print(linha)
    print("--------------------")

# Criar Matriz
def CriarMatriz():
    matriz.append([4, 2, 1, -2, 3])
    matriz.append([3, -3, -1, -1, 2])
    matriz.append([3, 5, 1, 1, 0])
    matriz.append([1, -1, -1, 4, -2])

    # for l in range(linhasTamanho):
    #     lmatriz = []
    #     for c in range(colunasTamanho):
    #         lmatriz.append(int(input(f"Valor da linha: {l} coluna: {c}: ")))
    #     matriz.append(lmatriz)

# Mudar posição da linha
def InverteLinhas(l1, l2):
    linhaAntiga = matriz[l1]
    matriz.remove(matriz[l1])
    matriz.insert(l2, linhaAntiga)

# Somar Linha (l1) com linha (l2):
def SomarLinha(l1, l2):
    for cont in range(quantLinha):
        matriz[l2][cont] = round((matriz[l2][cont] + matriz[l1][cont]), 1)

# Multiplicar linha por um valor
def MultLinha(l, valor):
    for cont in range(quantLinha):
        matriz[l][cont] = round((matriz[l][cont] * valor), 1)

# Pegar linha, multipicar por um valor, e soma a outra linha
def MultLinhaSoma(l1, l2, valor):
    for cont in range(quantLinha):
        matriz[l2][cont] = round((matriz[l2][cont] + (matriz[l1][cont] * valor)), 1)

# Verificar se existe 1 na coluna
def existeUmColuna(coluna):
    for cont in range(quantLinha):
        if ((matriz[cont][coluna] == 1) or (matriz[cont][coluna] == -1)):
            return True
    return False

# Aplicando Eliminação de Gauss
def CalculoEscala(linha):
    primeiroLoop = True
    existeUm = existeUmColuna(linha)

    if (existeUm == True and primeiroLoop == True):
        cont = linha
        while cont < quantLinha:
            if (matriz[cont][linha] == 1):
                InverteLinhas(cont, 0)
            elif (matriz[cont][linha] == -1):
                MultLinha(cont, -1)
                InverteLinhas(cont, 0)
            cont += 1

    if (matriz[linha][linha] > 1 or matriz[linha][linha] < -1):
        if (matriz[linha][linha] < 0):
            MultLinha(linha, (1/(-1 * matriz[linha][linha])))
            if (matriz[linha][linha] == -1):
                MultLinha(linha, -1)
        elif (matriz[linha][linha] > 0):
            MultLinha(linha, (1/matriz[linha][linha]))
        primeiroLoop == False

    if (matriz[linha][linha] == 1 or matriz[linha][linha] == -1):
        if (primeiroLoop == True):
            cont = linha + 1
            while cont < quantLinha:
                if(matriz[cont][linha] == -1):
                    SomarLinha(linha, cont)
                elif (matriz[cont][linha] > 0):
                    MultLinhaSoma(linha, cont, (-1 * matriz[cont][linha]))
                else:
                    MultLinhaSoma(linha, cont, math.fabs(matriz[cont][linha]))
                cont += 1
            primeiroLoop = False

    if (existeUm == False and primeiroLoop == True):
        if (matriz[linha][linha] < 0):
            MultLinha(linha, (1/(-1 * matriz[linha][linha])))
            if (matriz[linha][linha] == -1):
                MultLinha(linha, -1)
        elif (matriz[linha][linha] > 0):
            MultLinha(linha, (1/matriz[linha][linha]))
        primeiroLoop == False
    
# Escalonar matriz
def EscalonarLinha():
    PrintarMatriz()
    for linha in range(quantLinha):
        CalculoEscala(linha)
        PrintarMatriz()
            
# Fazer calculo das incógnitas com matriz escalada
matrizResult = []
def EfetuarCalculo():
    pass
    
CriarMatriz()
EscalonarLinha()
EfetuarCalculo()