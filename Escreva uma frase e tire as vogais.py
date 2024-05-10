'''Exercício de fixação 4: Crie um programa que solicite um número ao usuário e exiba a tabuada dele de 1 a 10, no formato:
Tabuada do n
n x 1 = n'''

numero=int(input("Digite um número: "))
for i in range(1,11):
    resultado=i*numero
    print(f"{i} * {numero} = {resultado}\n")