"""Crie um programa que receba uma lista de números e retorne a média."""

numeros=[]

def media(numeros):
    """
    Faz a média dos números digitados pelo usuário.
    :param numeros: Lista que esta recebendo o número digitado.
    :return:
    """

    soma=0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)

while True:
    if input("Deseja adicinaor um número? (s/n) ") == "n":
        break
    else:
        numero=int(input("Digite um numero: "))
        numeros.append(numero)

resultado = media(numeros)
print(f"A media é {resultado} e os numeros são {numeros}")

