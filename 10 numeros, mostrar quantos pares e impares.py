'''Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos são ímpares e informando ao final essas informações.'''
par=impar=0

for i in range (0,10):
    valor=int(input("Digite o "+str(i+1)+" número: "))
    resultado=valor%2

    if resultado==0:
        par+=1
    else:
        impar+=1
print(f"Você digitou {par:.0f} valores pares")
print(f"Você digitou {impar:.0f} valores impares")
