"""
2) Ler uma matriz A de duas dimensões com 7 linhas e 7 colunas. Ao final apresentar o
total de elementos pares existentes dentro da matriz.
"""
matriz = [[0] * 7 for _ in range(7)]  # Cria uma matriz 7x7 preenchida com zeros
total_pares = 0

for linha in range(7):
    for coluna in range(7):
        digitado = int(input(f'Digite o LIN {linha+1} COL {coluna+1}: '))
        matriz[linha][coluna] = digitado
        if digitado % 2 == 0:  # Verifica se o valor digitado é par
            total_pares += 1

print("Matriz:")
for linha in matriz:
    print(linha)

print(f'Total de pares: {total_pares}')
