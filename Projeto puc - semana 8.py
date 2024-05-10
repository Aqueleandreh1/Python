import json

estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []
data = []

def menu_principal():
    print("--MENU PRINCIPAL--")
    print("Digite um número do menu:\n1.Estudante\n2.Disciplina\n3.Professor\n4.Turma\n5.Matrícula\n9.Sair\n")

def menu_operacoes():
    print("--MENU DE OPERAÇÕES--")
    print("Digite um número do menu:\n1.Incluir\n2.Listar\n3.Atualizar\n4.Excluir\n5.Menu principal\n")

def incluir_estudante():
    print("\n---- INCLUIR ESTUDANTE----")
    print("Código do aluno:")
    codigo = apenas_numero()
    nome_do_aluno = str(input("\nInsira o nome do aluno: "))
    cpf_do_aluno = str(input("\nInsira o cpf do aluno: "))
    novo_estudante = {
        "Código": codigo,
        "Nome": nome_do_aluno,
        "Cpf": cpf_do_aluno
    }
    print("\nEstudante inserido com sucesso!")
    carregar_arquivos()
    estudantes.append(novo_estudante)
    salvar_arquivos()
def listar_estudante():
    carregar_arquivos()
    print("\n---- LISTAR ----")
    if len(estudantes) > 0:
        for estudante in estudantes:
            print(f"Dados do estudante: {estudante}")
    else:
        print("\nNenhum estudante cadastrado.")

def atualizar_estudante():
    carregar_arquivos()
    print("\n---- ATUALIZAR ----")
    if len(estudantes) > 0:
        print(estudantes)
        print("Código do aluno:")
        atualizar = int(apenas_numero())
        for estudante in estudantes:
            if estudante["Código"] == atualizar:
                estudante["Nome"] = input("Digite o novo nome: ")
                estudante["Cpf"] = input("Digite o novo CPF: ")
                salvar_arquivos()
                print("Estudante atualizado com sucesso!")
                break
        else:
            print("\nEstudante não encontrado.")
    else:
        print("\nNenhum estudante cadastrado para atualizar.")
def excluir_estudante():
    carregar_arquivos()
    print("\n---- EXCLUIR ----")
    if estudantes:
        print("Código do aluno:")
        excluir = apenas_numero()
        estudante_encontrado = False
        for estudante in estudantes:
            if estudante['Código'] == excluir:
                estudantes.remove(estudante)
                print("\nEstudante excluído com sucesso!")
                estudante_encontrado = True
                salvar_arquivos()
                break
        if not estudante_encontrado:
            print("\nEstudante não encontrado.")
    else:
        print("\nNenhum estudante cadastrado para excluir.")

def incluir_disciplina():
    print("\n---- INCLUIR DISCIPLINA---")
    print("Código da disciplina:")
    codigo = apenas_numero()
    nome_da_disciplina = str(input("\nInsira o nome da disciplina: "))
    nova_disciplina = {
        "Código": codigo,
        "Nome": nome_da_disciplina,
    }
    print("\nDisciplina inserida com sucesso!")
    carregar_arquivos()
    disciplinas.append(nova_disciplina)
    salvar_arquivos()

def listar_disciplina():
    carregar_arquivos()
    print("\n---- LISTAR ----")
    if len(disciplinas) > 0:
        for disciplina in disciplinas:
            print(f"Dados da disciplina: {disciplina}")
            salvar_arquivos()
    else:
        print("\nNenhuma disciplina cadastrada.")

def atualizar_disciplina():
    carregar_arquivos()
    print("\n---- ATUALIZAR ----")
    if len(disciplinas) > 0:
        print(disciplinas)
        print("Código da disciplina:")
        atualizar = apenas_numero()
        for disciplina in disciplinas:
            if disciplina["Código"] == atualizar:
                disciplina["Nome"] = input("Digite o novo nome da disciplina: ")
                salvar_arquivos()
                print("Disciplina atualizada com sucesso!")
                break
        else:
            print("\nDisciplina não encontrada.")
    else:
        print("\nNenhuma disciplina cadastrada para atualizar.")

def excluir_disciplina():
    carregar_arquivos()
    print("\n---- EXCLUIR ----")
    if disciplinas:
        print("Código da disciplina:")
        excluir = apenas_numero()
        disciplina_encontrada = False
        for disciplina in disciplinas:
            if disciplina['Código'] == excluir:
                disciplinas.remove(disciplina)
                print("\nEstudante excluído com sucesso!")
                disciplina_encontrada = True
                salvar_arquivos()
                break
        if not disciplina_encontrada:
            print("\nEstudante não encontrado.")
    else:
        print("\nNenhum estudante cadastrado para excluir.")
def incluir_professor():
    print("\n---- INCLUIR PROFESSOR---")
    print("Código do professor:")
    codigo = apenas_numero()
    nome_do_professor = str(input("\nInsira o nome do professor: "))
    cpf_do_professor = str(input("\nInsira o cpf do professor: "))
    novo_professor = {
        "Código": codigo,
        "Nome": nome_do_professor,
        "Cpf": cpf_do_professor
    }
    print("\nProfessor inserido com sucesso!")
    carregar_arquivos()
    professores.append(novo_professor)
    salvar_arquivos()

def listar_professor():
    carregar_arquivos()
    print("\n---- LISTAR ----")
    if len(professores) > 0:
        for professor in professores:
            print(f"Dados do estudante: {professor}")
            salvar_arquivos()
    else:
        print("\nNenhum professor cadastrado.")

def atualizar_professor():
    carregar_arquivos()
    print("\n---- ATUALIZAR ----")
    if len(professores) > 0:
        print(professores)
        print("Código do professor:")
        atualizar = apenas_numero()
        for professor in professores:
            if professor["Código"] == atualizar:
                professor["Nome"] = input("Digite o novo nome: ")
                professor["Cpf"] = input("Digite o novo CPF: ")

                salvar_arquivos()
                print("Professor atualizado com sucesso!")
                return
        else:
            print("\nProfessor não encontrado.")
    else:
        print("\nNenhum Professor cadastrado para atualizar.")

def excluir_professor():
    carregar_arquivos()
    print("\n---- EXCLUIR ----")
    if professores:
        print("Código do professor:")
        excluir = apenas_numero()
        professor_encontrado = False
        for professor in professores:
            if professor['Código'] == excluir:
                professores.remove(professor)
                print("\nProfessor excluído com sucesso!")
                professor_encontrado = True
                salvar_arquivos()
                break
        if not professor_encontrado:
            print("\nProfessor não encontrado.")
    else:
        print("\nNenhum professor cadastrado para excluir.")

def incluir_turma():
    print("\n---- INCLUIR TURMA---")
    print("Código da turma:")
    codigo = apenas_numero()
    if codigo in turmas:
        print("Código de turma já existente.")
    else:
        codigo_do_professor = int(input("\nInsira o código do professor: "))
        codigo_da_disciplina = int(input("\nInsira o código da disciplina: "))
        nova_turma = {
            "Código da turma": codigo,
            "Código do professor": codigo_do_professor,
            "Código da disciplina": codigo_da_disciplina
        }
        print("\nTurma inserida com sucesso!")
        carregar_arquivos()
        turmas.append(nova_turma)
        salvar_arquivos()

def listar_turma():
    carregar_arquivos()
    print("\n---- LISTAR ----")
    if len(turmas) > 0:
        for turma in turmas:
            print(f"Dados da turma: {turma}")
            salvar_arquivos()
    else:
        print("\nNenhuma turma cadastrada.")

def atualizar_turma():
    carregar_arquivos()
    print("\n---- ATUALIZAR ----")
    if len(turmas) > 0:
        print(turmas)
        print("Código da turma:")
        atualizar = apenas_numero()
        for turma in turmas:
            if turma["Código da turma"] == atualizar:
                turma["Código do professor"] = input("Digite o novo código do professor: ")
                turma["Código da disciplina"] = input("Digite o novo código da disciplina: ")

                salvar_arquivos()
                print("Turma atualizada com sucesso!")
                break
        else:
            print("\nTurma não encontrada.")
    else:
        print("\nNenhuma turma cadastrada para atualizar.")

def excluir_turma():
    carregar_arquivos()
    print("\n---- EXCLUIR ----")
    if turmas:
        print("Código da turma:")
        excluir = apenas_numero()
        turma_encontrada = False
        for turma in turmas:
            if turma['Código'] == excluir:
                turmas.remove(turma)
                print("\nEstudante excluído com sucesso!")
                turma_encontrada = True
                salvar_arquivos()
                break
        if not turma_encontrada:
            print("\nTurma não encontrado.")
    else:
        print("\nNenhuma turma cadastrada para excluir.")

def incluir_matricula():
    print("\n---- INCLUIR MATRICULA---")
    print("Código da turma:")
    codigo = apenas_numero()
    codigo_do_estudante = int(input("\nInsira o código do estudante: "))
    nova_matricula = {
        "Código da turma": codigo,
        "Código do estudante": codigo_do_estudante
    }
    if nova_matricula in matriculas:
        print("O aluno já esta matriculado nessa turma.")
    else:
        print("\nMatricula inserida com sucesso!")
        carregar_arquivos()
        matriculas.append(nova_matricula)
        salvar_arquivos()

def listar_matricula():
    carregar_arquivos()
    print("\n---- LISTAR ----")
    if len(matriculas) > 0:
        for matricula in matriculas:
            print(f"Dados da matricula: {matricula}")
            salvar_arquivos()
    else:
        print("\nNenhuma matricula cadastrada.")

def atualizar_matricula():
    carregar_arquivos()
    print("\n---- ATUALIZAR ----")
    if len(matriculas) > 0:
        print(matriculas)
        print("Código da turma:")
        atualizar = apenas_numero()
        for matricula in matriculas:
            if matricula["Código da turma"] == atualizar:
                matricula["Código do estudante"] = input("Digite o novo código do estudante: ")
                salvar_arquivos()
                print("Matricula atualizada com sucesso!")
                return
        else:
            print("\nMatricula não encontrada.")
    else:
        print("\nNenhuma Matricula cadastrada para atualizar.")

def excluir_matricula():
        carregar_arquivos()
        print("\n---- EXCLUIR ----")
        if matriculas:
            print("Código da turma:")
            excluir = apenas_numero()
            matricula_encontrada = False
            for matricula in matriculas:
                if matricula['Código'] == excluir:
                    matriculas.remove(matricula)
                    print("\nEstudante excluído com sucesso!")
                    matricula_encontrada = True
                    salvar_arquivos()
                    break
            if not matricula_encontrada:
                print("\nMatricula não encontrada.")
        else:
            print("\nNenhuma matricula cadastrada para excluir.")

def get_data():
    return{
        'estudantes': estudantes,
        'disciplinas': disciplinas,
        'professores': professores,
        'turmas': turmas,
        'matricula': matriculas
         }

def salvar_arquivos():
    with open("teste123.json", "w", encoding="utf-8") as arquivo:
        json.dump(get_data(), arquivo, ensure_ascii=False)

def carregar_arquivos():
    try:
        with open("teste123.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return None

def apenas_numero():
    while True:
        try:
            codigo = int(input("\nInsira o código deste campo: "))
            return codigo
        except ValueError:
            print("Este campo aceita apenas números.")

#Início do código_______________

while True:
    data = carregar_arquivos()

    if data is not None:
        estudantes = data.get('estudantes', [])
        disciplinas = data.get('disciplinas', [])
        professores = data.get('professores', [])
        turmas = data.get('turmas', [])
        matriculas = data.get('matriculas', [])
    else:
        estudantes = []
        disciplinas = []
        professores = []
        turmas = []
        matriculas = []

    menu_principal()
    menu_principal1 = int(input("Digite o número da opção desejada: "))

    if menu_principal1 == 1:
        while True:
            print("--MENU ESTUDANTES--")
            menu_operacoes()
            menu = int(input("Digite o número da opção desejada: "))
            if menu == 1:
                incluir_estudante()
            elif menu == 2:
                listar_estudante()
            elif menu == 3:
                atualizar_estudante()
            elif menu == 4:
                excluir_estudante()
            elif menu == 5:
                break
    if menu_principal1 == 2:
        while True:
            print("--MENU DISCIPLINA--")
            menu_operacoes()
            menu = int(input("Digite o número da opção desejada: "))
            if menu == 1:
                incluir_disciplina()
            elif menu == 2:
                listar_disciplina()
            elif menu == 3:
                atualizar_disciplina()
            elif menu == 4:
                excluir_disciplina()
            elif menu == 5:
                break
    if menu_principal1 == 3:
        while True:
            print ("--MENU PROFESSOR--")
            menu_operacoes()
            menu = int(input("Digite o número da opção desejada: "))
            if menu == 1:
                incluir_professor()
            elif menu == 2:
                listar_professor()
            elif menu == 3:
                atualizar_professor()
            elif menu == 4:
                excluir_professor()
            elif menu == 5:
                break
    if menu_principal1 == 4:
        while True:
            print("--MENU TURMA--")
            menu_operacoes()
            menu = int(input("Digite o número da opção desejada: "))
            if menu == 1:
                incluir_turma()
            elif menu == 2:
                listar_turma()
            elif menu == 3:
                atualizar_turma()
            elif menu == 4:
                excluir_turma()
            elif menu == 5:
                break
    if menu_principal1 == 5:
        while True:
            print("--MENU MATRÍCULA--")
            menu_operacoes()
            menu = int(input("Digite o número da opção desejada: "))
            if menu == 1:
                incluir_matricula()
            elif menu == 2:
                listar_matricula()
            elif menu == 3:
                atualizar_matricula()
            elif menu == 4:
                excluir_matricula()
            elif menu == 5:
                break
    if menu_principal1 == 9:
        break
print("Programa finalizado!")