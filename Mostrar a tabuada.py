'''Crie um programa que peça dois números ao usuário – o primeiro será o numerador e o segundo, o expoente.
A saída do programa deve ser o resultado da operação: numerador elevado ao expoente.
Observação: não use a função própria do Python que calcula automaticamente potência.'''

numero=0

numerador=int(input("Escreva um número: "))
expoente=int(input("Escreva um segundo número: "))

multiplicaçao=numerador
for i in range (1,expoente,1):

    multiplicaçao*=numerador

print("Resultado= ",multiplicaçao)


