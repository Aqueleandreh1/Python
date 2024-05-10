"""Crie um programa que calcule, a partir de uma função, o fatorial de um número.
Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Observação: por propriedade, 0! = 1."""

def fatorial(numero):
    """
    Se o número for 0, o resultado será 1. Senão, ele calculará o fatorial:

    :param numero: Número digitado pelo usuário.
    :return:
    """

    if numero == 0:
        return 1
    else:
        fat=1
        for i in range(numero,0,-1):
            fat *= i
            print(fat)
        return fat

numero=int(input("Digite o número fatorial: "))
fat = fatorial(numero)
print(f"O numero fatorial é {numero} e o fatorial dele é {fat}")