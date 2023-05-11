"""
1)	Faça um programa para ler e imprimir uma matriz 2 × 4 de números inteiros.
"""
matriz = []

# Leitura da matriz
for i in range(2):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha += [valor]
    matriz += [linha]

# Impressão da matriz
for i in range(2):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()
