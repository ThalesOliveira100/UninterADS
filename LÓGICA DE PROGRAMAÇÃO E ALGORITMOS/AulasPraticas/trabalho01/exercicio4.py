lista_livro = []
id_global = 0


def cadastrar_livro(id):
    print('*' * 69)
    print('-' * 23, 'MENU CADASTRAR LIVRO', '-' * 23)
    print(f'ID do livro: {id}')

    nome = input('Por favor entre com o nome: ')
    autor = input('Por favor entre com o autor: ')
    editora = input('Por favor entre com a editora: ')

    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livro.append(livro)


def consultar_livro():
    print('*' * 69)
    print('-' * 23, 'MENU CONSULTAR LIVRO', '-' * 24)
    opcao_consulta = int(input('Escolha a opção desejada: '
                               '\n1 - Consultar todos'
                               '\n2 - Consultar por ID'
                               '\n3 - Consultar por Autor'
                               '\n4 - Voltar ao menu\n>> '))

    while True:
        if opcao_consulta == 1:
            for livro in lista_livro:
                print(f"** ID: {livro['id']}")
                print(f"Nome: {livro['nome']}")
                print(f"Autor: {livro['autor']}")
                print(f"Editora: {livro['editora']}")
                print("-------------------------")
            break

        elif opcao_consulta == 2:
            id_livro = int(input("Digite o ID do livro: "))
            livro_encontrado = False

            for livro in lista_livro:
                if livro['id'] == id_livro:
                    print(f"** ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")

                    livro_encontrado = True
                break
            if not livro_encontrado:
                print('Livro não encontrado!')
            break

        elif opcao_consulta == 3:
            autor_livro = input('Digite o nome do autor: ')
            livros_encontrados = False
            livros_do_autor = []

            for livro in lista_livro:
                if autor_livro.lower() in livro['autor'].lower():
                    livros_do_autor.append(livro)
                    livros_encontrados = True

            if livros_encontrados:
                for livro in livros_do_autor:
                    print(f"** ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-------------------------")
                break

            if not livros_encontrados:
                print(f'Nenhum livro encontrado para o autor: "{autor_livro}"')
                break

        elif opcao_consulta == 4:
            break

        else:
            print('Opção inválida!')


def remover_livro():
    id_livro = int(input('Digite o ID do livro que deseja remover: '))
    livro_encontrado = False

    for indice, livro in enumerate(lista_livro):
        if livro['id'] == id_livro:
            del lista_livro[indice]
            livro_encontrado = True
            break

        if livro_encontrado:
            print(f"Livro com ID {id_livro} removido com sucesso!")
        else:
            print(f"Livro com ID {id_livro} não encontrado!")


print('Bem vindo ao Controle de Livros do Thales Gabriel Moreira de Oliveira')
while True:

    print('*' * 69)
    print('-' * 26, 'MENU PRINCIPAL', '-' * 27)
    opcao = int(input('Escolha a opção desejada: '
                      '\n1 - Cadastrar Livro'
                      '\n2 - Consultar Livro(s)'
                      '\n3 - Remover Livro'
                      '\n4 - Sair\n>> '))

    if opcao == 1:
        id_global += 1
        cadastrar_livro(id_global)

    elif opcao == 2:
        consultar_livro()

    elif opcao == 3:
        remover_livro()

    elif opcao == 4:
        print('Programa encerrado!')
        break
    else:
        print('Opção inválida! Escolha a opção desejada novamente.')
