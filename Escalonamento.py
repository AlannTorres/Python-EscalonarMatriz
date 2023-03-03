# Print Matriz:
def PrintarMatriz():
    for l in matriz:
        print(l)
        
# Criar Matriz:
def CriarMatriz():
    for linha in range(quantLinha):
        lmatriz = []
        for coluna in range(quantColunas):
            lmatriz.append(float(input(f"Valor da linha: {linha + 1} coluna: {coluna + 1}: ")))
        matriz.append(lmatriz)
    
# Mudar posição da linha(l1) pela linha(l2):
def InverteLinhas(l1, l2):
    linhaAntiga = matriz[l1]
    matriz.remove(matriz[l1])
    matriz.insert(l2, linhaAntiga)

# Multiplicar linha(l) por um valor:
def MultLinha(l, valor):
    for cont in range(quantColunas):
        matriz[l][cont] = round((matriz[l][cont] * valor), 1)

# Pegar linha(l1), multipicar por um valor, e soma a linha(l2):
def MultLinhaSoma(l1, l2, valor):
    for cont in range(quantColunas):
        matriz[l2][cont] = round((matriz[l2][cont] + (matriz[l1][cont] * valor)), 1)

# Aplicando Eliminação de Gauss:
def CalculoEscala(linha, coluna):
    ## Se pivor for 0, procuar próxima linha diferente de 0 e fazer troca
    if (matriz[linha][coluna] == 0):
        contLinha = linha + 1 
        while contLinha < quantLinha:
            if (matriz[contLinha][coluna] != 0):
                InverteLinhas(linha, contLinha)
            if (matriz[linha][coluna] != 0):
                break
            contLinha += 1
    
    ## Pivor for igual maior que 1 ou menor, Dividir multiplicar pivor por (1/pivor) para transformar em 1
    if ((matriz[linha][coluna] < 1 or matriz[linha][coluna] > 1) and matriz[linha][coluna] != 0):
        MultLinha(linha, 1/matriz[linha][coluna])
        
    ## Pivor for igual a 1 ou -1, converter -1 para 1 e zerar colunas acima e abaixo
    if ((matriz[linha][coluna] == 1 or matriz[linha][coluna] == -1)):
        if (matriz[linha][coluna] == -1):
            MultLinha(linha, -1)
        contLinha = 0
        while contLinha < quantLinha:
            if (contLinha != coluna):
                if (matriz[contLinha][coluna] != 0):
                    MultLinhaSoma(linha, contLinha, (-1 * matriz[contLinha][coluna]))
            contLinha += 1
    
# Organizar linhas por quantidade de zeros ate o primeiro não nulo da linha
def OrganizarLinhas():
    quantZero = 0
    for m in matriz:
        for n in m:
            if (n == 0):
                quantZero += 1
        if (quantZero == quantColunas):
            InverteLinhas(matriz.index(m), quantZero)
            quantZero = 0
           
# Escalonar matriz:
def EscalonarLinha():
    ## Verificar se 1º Coluna é vazia
    for i in matriz:
        if (i[0] != 0):
            colunaNula = False
        else:
            colunaNula = True

    ## Efetuar o escalonamento por pivor
    OrganizarLinhas()
    for contLinha in range(quantLinha):
        if (colunaNula):
            if (contLinha < quantLinha):
                CalculoEscala(contLinha, contLinha)
            else:
                CalculoEscala(contLinha, contLinha + 1)
        else:
            if (contLinha < quantColunas):
                CalculoEscala(contLinha, contLinha)
    
# Para criação desse programa foi usado o metodo Eliminação de Gauss para criar a versao escada da matriz

# Começo do codigo:
matriz = []
quantLinha = int(input("Digite a quantidade de linhas da matriz:"))
quantColunas = int(input("Digite a quantidade de colunas da matriz:"))

CriarMatriz()
print("\n----- Matriz Normal ----")
PrintarMatriz()
EscalonarLinha()
print("\n---- Matriz Escada ----")
PrintarMatriz()