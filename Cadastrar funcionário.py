"""Crie um programa que cadastre os funcionários de uma empresa e seus dependentes. O funcionário deve ser cadastrado com matrícula,
nome e dependentes. Os dependentes devem ser inseridos dinamicamente em uma tupla. Dica: use o operador “+=”."""

cadastro=[]

while True:
    nome=input("Digite o nome do funcionário: ")
    matricula=input("Digite o numero de matricula: ")
    dependentes=tuple()
    while True:
        dependente=input("Digite o nome do dependente (Digite 0 para sair): ")
        if dependente == "0":
            break
        else:
            dependentes += (dependente,)
    funcionario=(nome,matricula,dependentes)
    cadastro.append(funcionario)
    if input("Gostaria de cadastrar mais um funcionário (Digite 0 para sair): ") == "0":
        break
print(cadastro)
