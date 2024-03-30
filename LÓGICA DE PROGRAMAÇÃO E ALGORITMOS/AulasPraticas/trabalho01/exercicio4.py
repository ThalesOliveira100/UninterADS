# Variáveis globais utilizadas ao longo do sistema
lista_livro = []
id_global = 0


# Função básica de cadastro, puxa um id para cadastrar o livro, não realiza nenhuma verificação por não ser necessário,
# visto que só é utilizada ao invocar a função passando o id_global que é auto incrementado.
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
    # Primeiramente valida se a lista_livros está nula, se estiver ele avisará que o usuário ainda não cadastrou nenhum
    # livro no sistema, e o impede de acessar o menu.
    if len(lista_livro):
        print('-' * 23, 'MENU CONSULTAR LIVRO', '-' * 24)
        opcao_consulta = int(input('Escolha a opção desejada: '
                                   '\n1 - Consultar todos'
                                   '\n2 - Consultar por ID'
                                   '\n3 - Consultar por Autor'
                                   '\n4 - Voltar ao menu\n>> '))

        while True:
            # Primeira opção da consulta de livros, realiza um loop na lista_livro e retorna todos os livros encontrados
            if opcao_consulta == 1:
                for livro in lista_livro:
                    print(f"** ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-------------------------")

            # Segunda opção da consulta de livros, localiza o livro pelo ID
            elif opcao_consulta == 2:
                id_livro = int(input("Digite o ID do livro: "))
                livro_encontrado = False

                # Valida se o ID informado é maior que o Id global e localiza o primeiro livro cadastrado com o ID
                # informado.
                if id_global >= id_livro:
                    for livro in lista_livro:
                        if livro['id'] == id_livro:
                            print(f"** ID: {livro['id']}")
                            print(f"Nome: {livro['nome']}")
                            print(f"Autor: {livro['autor']}")
                            print(f"Editora: {livro['editora']}")
                            livro_encontrado = True

                    if not livro_encontrado:
                        print('Este livro não está mais disponível!')
                else:
                    print('Não há um livro cadastrado com este ID')

            # Terceira opção da consulta de livros, localiza o livro pelo nome do autor, o nome não pode ter partes
            # ocultas, mas não é capsensive. A função cria uma nova lista para exibir por meio de uma laço futuro, todos
            # os livros encontrados.
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

                if not livros_encontrados:
                    print(f'Nenhum livro encontrado para o autor: "{autor_livro}"')

            # Quarta opção da consulta de livros, como o laço é quebrado ao final do loop, foi utilizado apenas um pass
            # para passar a vez.
            elif opcao_consulta == 4:
                pass

            else:
                print('Opção inválida!')
            break
    else:
        print('Você ainda não cadastrou nenhum livro!')


# Função para remover um livro da lista_livros através do ID
def remover_livro():
    try:
        id_livro = int(input('Digite o ID do livro que deseja remover: '))
        livro_encontrado = False

        # Verifica se o id_global é maior que o ID informado. Se for, prosegue para a busca por meio de um laço. Também
        # utiliza o livro_encontrado, mas para definir melhor qual mensagem será impressa ao final da execução.
        if id_global >= id_livro:
            for livro in lista_livro:
                if livro['id'] == id_livro:
                    print(f'Livro {livro["nome"]} deletado com sucesso!')
                    del lista_livro[id_livro - 1]

                    livro_encontrado = True

            if not livro_encontrado:
                print('Não foi possível localizar o livro pelo ID informado.')
        else:
            print("Não há um livro cadastrado com este ID")

    except IndexError:
        print('O ID informado é invalido!')
    except ValueError:
        print('O ID informado deve ser numérico!')


# Segmento principal do sistema: o menu principal.
print('Bem vindo ao Controle de Livros do Thales Gabriel Moreira de Oliveira')
while True:
    try:
        print('*' * 69)
        print('-' * 26, 'MENU PRINCIPAL', '-' * 27)
        opcao = int(input('Escolha a opção desejada: '
                          '\n1 - Cadastrar Livro'
                          '\n2 - Consultar Livro(s)'
                          '\n3 - Remover Livro'
                          '\n4 - Sair\n>> '))

        # Caso a primeira opção seja seleciona, o id_global é implementado, e depois, passado para a função de cadastro.
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
    except ValueError:
        print('Opção inválida. A opção deve ser numérica!')
