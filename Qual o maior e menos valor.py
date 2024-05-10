'''Exercício de fixação 3: Crie um programa que receba um texto digitado pelo usuário e o imprima apenas com consoantes,
removendo as vogais. Observação: desconsiderar letras maiúsculas e acentos.'''

texto=str(input("Escreva um texto qualquer: "))
frase=""
for vogal in texto:
    if vogal.lower() not in "aeiou":
        frase=frase+vogal
print(frase)