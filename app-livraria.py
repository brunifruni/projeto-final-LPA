print("\nBEM VINDO A NOSSA LIVRARIA")
lista_livro = []
id_global = 0

#cadastro de livros
def cadastrar_livro(id):
    print('\n ------ MENU CADASTRAR LIVRO ------')
    print(f'ID do livro: {id}')
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o autor do livro: ")
    editora = input("Digite a editora do livro: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)


#função para consultar livro
def consultar_livro():
    while True:
        print("\n------ MENU CONSULTAR LIVRO ------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por id")
        print("3 - Consultar Livro(s) por autor")
        print("4 - Retornar")
        print("----------------------------------")
        opcao = input(">> ")

        if opcao == "1":
            if not lista_livro:
                print("Nenhum livro cadastrado.")
            else:
                print("\n------ CONSULTA TODOS OS LIVROS CADASTRADOS ------")
                for livro in lista_livro:
                    print(f"id: {livro['id']}")
                    print(f"nome: {livro['nome']}")
                    print(f"autor: {livro['autor']}")
                    print(f"editora: {livro['editora']}")
                    print("----------------------------------")
        elif opcao == "2":
            id = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id:
                    print("\nid:", livro['id'])
                    print("nome:", livro['nome'])
                    print("autor:", livro['autor'])
                    print("editora:", livro['editora'])
                    print("----------------------------------")
                    encontrado = True
                    break
            if not encontrado:
                print("Livro não encontrado.")
        elif opcao == "3":
            autor = input("Digite o autor: ")
            encontrado = False
            for livro in lista_livro:
                if livro["autor"] == autor:
                    print("\nid:", livro['id'])
                    print("nome:", livro['nome'])
                    print("autor:", livro['autor'])
                    print("editora:", livro['editora'])
                    print("----------------------------------")
                    encontrado = True
            if not encontrado:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida")


#remover livro
def remover_livro():
    while True:
        id = int(input("\nDigite o ID do livro a ser removido: "))
        for livro in lista_livro:
            if livro["id"] == id:
                lista_livro.remove(livro)
                print("Livro removido com sucesso.")
                return
        print("Id inválido")


#executa o menu
while True:
    print("\n------ MENU PRINCIPAL ------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    print("---------------------------")
    opcao = input(">> ")

    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida")
