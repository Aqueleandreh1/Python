"""Crie um programa que cadastre locais históricos do mundo com suas coordenadas,
fazendo uso de tuplas com parâmetros nomeados. Dica: use a função namedtuple()."""

from collections import namedtuple

monumentos=[]

while True:
    coordenada=namedtuple("monumento",["nome","pais","continente"])
    nome=input("Escreva o nome do local histórico: ")
    pais=input("Escreva em qual pais fica: ")
    continente=input("Escreva em qual continente fica este pais: ")

    monumento = coordenada(nome=nome,pais=pais,continente=continente)
    monumentos.append(monumento)

    if input("Gostaria de cadastrar mais um monumento? (s/n) ") == "n":
            break
for monumento in monumentos:
    print(f"Local Historico: {monumento.nome}")
    print(f"Local macro: ({monumento.pais}, {monumento.continente})")