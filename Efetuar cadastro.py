"""Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas,
adicionando-as a uma lista e imprimindo essa lista no fim do programa."""

cadastro=[]

nome=str(input("Digite o seu nome: "))
rg=input("Digite o seu RG (apenas os numeros): ")
cpf=input("Digite o seu CPF (apenas os numeros): ")
pessoa=(nome,rg,cpf)
cadastro.append(pessoa)

print(cadastro)