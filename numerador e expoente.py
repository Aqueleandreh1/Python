'''CExercício de fixação 6: Crie um programa que peça para o usuário inserir um login e uma senha.
Caso os valores sejam iguais, informar que os dados são inválidos e pedir novamente as informações.
Caso contrário, exibir a mensagem "Bem-vindo ao sistema!".'''


while True:
    usuario = str(input("Escreva seu usuário para login: "))
    senha = str(input("Escreva sua senha para login: "))
    if usuario == senha:
        print("Valor invalido")
    else:
        break
print("\nBem-vindo ao sistema!")