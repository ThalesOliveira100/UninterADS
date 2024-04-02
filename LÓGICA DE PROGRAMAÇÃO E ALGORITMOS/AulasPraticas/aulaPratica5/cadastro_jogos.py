# Algoritmo para cadastrar jogos informando o nome e a qual videgame ele pertence.
# Criar um menu de opções contendo: cadastrar novo item, listar tudo que foi cadastrado e sair.


def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'at')
        a.close()
    except Exception as e:
        print('Erro na criação do arquivo', e)
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nome_arquivo))


def cadastrar_jogo(nome_arquivo):
    nome = input('Digite o nome do jogo: ')
    plataforma = input('Digite a plataforma do jogo: ')
    print('\nJogo cadastrado com sucesso!')

    try:
        a = open(nome_arquivo, 'at')
    except Exception as e:
        print('Erro ao abrir o arquivo', e)
    else:
        a.write(f'{id};{nome};{plataforma}\n')
    finally:
        a.close()


def consultar_jogos(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except Exception as e:
        print('Erro ao ler o arquivo: ', e)
    else:
        print(a.read())
    finally:
        a.close()


# Programa principal
arquivo = 'games.txt'

if existe_arquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    criar_arquivo(arquivo)

while True:
    try:
        print('')
        print('-=-' * 17 + '\n Bem vindo ao cadastro de jogos do Thales Oliveira\n' + '-=-' * 17)
        print('Entre com a opção desejada: \n')
        print('1 - Cadastrar novo Jogo')
        print('2 - Consultar todos os jogos')
        print('3 - Sair')
        operacao = int(input('>>  '))

        if operacao == 1:
            cadastrar_jogo(arquivo)

        elif operacao == 2:
            consultar_jogos(arquivo)

        elif operacao == 3:
            exit('Encerrando o programa...')

        else:
            print('Operação inválida. Tente novamente.')
            continue

    except ValueError:
        print('O valor deve ser númerico!')
