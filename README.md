# Escalonamento Matriz

# Sobre:
Esse projeto foi feito para aual 

# Processo de escalonamento de Matrizes:
O escalonamento de matrizes é uma técnica matemática que consiste em transformar uma matriz em uma forma escalonada, isto é, uma matriz em que os elementos abaixo da diagonal principal são iguais a zero. Essa técnica é frequentemente utilizada em diversas áreas da matemática, como álgebra linear e cálculo.

### O que é uma matriz
Uma matriz é uma estrutura de dados composta por elementos dispostos em linhas e colunas. Matrizes são amplamente utilizadas na matemática para representar sistemas de equações lineares, transformações lineares, entre outras aplicações.

Uma matriz pode ser representada por uma letra maiúscula, como A, B, C, etc., e seus elementos podem ser denotados por um índice duplo, como A[i,j], que representa o elemento da linha i e coluna j.

Por exemplo, a matriz A a seguir possui 3 linhas e 3 colunas:
```
| 2  3 -1 |
| 1  2  1 |
|-1  1  2 |
```

### O que é escalonar uma matriz
Escalonar uma matriz significa transformá-la em uma forma escalonada, isto é, uma matriz em que os elementos abaixo da diagonal principal são iguais a zero. Para isso, são realizadas operações elementares nas linhas da matriz, como adição, subtração e multiplicação.

Dessa maneira, para reduzir uma matriz para a forma escada de ser seguido os seguites pirincipios:
- O primeiro elemento não nulo de uma linha não nula é igual a 1
- Cada coluna contem o primeiro elemento não nulo e o resto abaixo deve ser igual a zero
- Toda linha nula deve estar abaixo de todas as linhas não nulas

Dessa forma conseguimos um exemplo de uma escalonamento 
```
| 2  3 -1 |
| 1  2  1 |
|-1  1  2 |
```
--->
```
| 1  0  0 |
| 0  1  0 |
| 0  0  1 |
```
### Como escalonar uma matriz
Existem três operações elementares que podem ser realizadas nas linhas de uma matriz sem alterar o seu conjunto de soluções de sistemas de equações lineares. Essas operações são:

Multiplicação de uma linha por uma constante não nula;
- Troca de posição de duas linhas;
- Adição de uma múltipla de uma linha em outra linha.

Para escalonar uma matriz, é necessário realizar essas operações elementares nas linhas da matriz, de modo a transformá-la na forma escalonada. O processo pode ser resumido em quatro etapas:

Identifique a primeira coluna da matriz que contém um elemento não nulo (chamado de pivô).
Utilize operações elementares para transformar os elementos abaixo e acima do pivô em zero.
Repita o processo nas colunas restantes.
