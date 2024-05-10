'''Exercício de fixação 7: Crie um programa que solicite ao usuário vários números e, ao digitar 0, calcule a média dos números informados.'''
contador=0
soma=0
media=0

while True:
    contador+=1
    numero=int(input("Digite um numero: "))
    soma+=numero
    if numero==0:
        break
media=soma/contador
print("A média é: ",media)