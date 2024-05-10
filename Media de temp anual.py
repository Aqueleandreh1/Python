'''Crie um programa que efetue a soma de duas matrizes 3x3, sabendo que a soma desse tipo de matriz é uma nova matriz 3x3,
sendo cada elemento resultado da soma dos elementos das matrizes na mesma posição. Exemplo:

#ParaTodosVerem Abre colchetes linha com 1 2 3, linha abaixo com 4 5 6, linha abaixo com 7 8 9, fecha colchetes.
# Sinal de adição e abre novo colchetes. Linha com 3 2 3, linha abaixo com 1 3 3, linha abaixo com 0 2 2,
# fecha colchetes.  Sinal de igual e abre novo colchetes com linha  com 4 4 6, linha abaixo com  5 8 9, linha abaixo com 7 10 11, fecha colchetes.'''

matriz1 = []
matriz2 = []
matrizSoma = []

matriz1 = []
matriz2 = []
matrizSoma = []

# Preenchendo a primeira matriz
print("Preencha a primeira matriz")
for i in range(3):
    matriz1.append([])
    print("Na matriz número", i + 1, "insira abaixo")
    for n in range(3):
        num = int(input(f"Insira o elemento {n + 1} da linha {i + 1}: "))
        matriz1[i].append(num)
    print("\nMatriz atual:")
    for linha in matriz1:
        print(linha)

# Preenchendo a segunda matriz
print("\nPreencha a segunda matriz:")
for i in range(3):
    matriz2.append([])
    print("Na matriz número", i + 1, "insira abaixo:")
    for n in range(3):
        num = int(input(f"Insira o elemento {n + 1} da linha {i + 1}: "))
        matriz2[i].append(num)
    print("\nMatriz atual:")
    for linha in matriz2:
        print(linha)

# Somando as matrizes
for i in range(3):
    matrizSoma.append([])
    for j in range(3):
        soma = matriz1[i][j] + matriz2[i][j]
        matrizSoma[i].append(soma)

# Imprimindo a matriz resultante
print("\nMatriz resultante da soma:")
for linha in matrizSoma:
    print(linha)