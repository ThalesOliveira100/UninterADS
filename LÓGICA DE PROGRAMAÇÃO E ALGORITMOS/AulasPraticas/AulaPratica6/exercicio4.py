# Programa que lê o nome, ano de nascimento e sexo de diferentes pessoas
# Dados armazenados em um dicionário com listas
# Ao encerrar o cadastro, apresenta:
# * O total de cadastros efetuados
# * A média das idades das pessoas
# * Uma lista de mulheres com menos de 30 anos
# * Uma lista de homens com idade acima da média
import datetime

# VARIAVEIS GLOBAIS
cadastros = {'nome': [],
             'ano': [],
             'sexo': []}

# Menu Principal
print('SISTEMA CADASTRO DE PESSOAS - THALES OLIVEIRA\n')


def iniciar_cadastro():
    global cadastros
    while True:
        try:
            nome = input('Informe o nome:  ')
            ano_nascimento = int(input('Informe o ano de nascimento:  '))
            sexo = input('Informe o sexo (F - M):  ')
            while sexo.lower() not in 'fm':
                sexo = input('Sexo informado de forma incorreta. Informe novamente:  ')

            cadastros['nome'].append(nome)
            cadastros['ano'].append(ano_nascimento)
            cadastros['sexo'].append(sexo)
            print(cadastros)

        except ValueError:
            print('O ano deve ser informado em formato númerico!')
        finally:
            prosseguir = input('Pressione ENTER para continuar, ou digite N para retornar ao menu principal.\n')
            if prosseguir.lower() == 'n':
                break
            while prosseguir.lower() not in ['s', '']:
                prosseguir = input('Pressione ENTER para continuar, ou digite N para retornar ao menu principal.\n')


def consultar_cadastro():
    lista_idades = []
    for ano in cadastros['ano']:
        idade = ano - int(str(datetime.date.today())[0:4])
        lista_idades.append(idade)

    soma_idades = sum(lista_idades) * -1
    print(soma_idades)

    print(f'TOTAL DE CADASTROS:  {len(cadastros["nome"])}')
    print(f'MÉDIA DAS IDADES:    {soma_idades / len(cadastros["nome"])}')


def exibir_resultados():
    pass


while True:
    print('1 - Iniciar cadastros\n'
          '2 - Consultar cadastro\n'
          '3 - Exibir resultados\n'
          '0 - Encerrar sistema\n'
          '\nInforme a opção desejada')
    operacao = int(input('>>  '))

    if operacao == 0:
        exit('Encerrando sistema')

    elif operacao == 1:
        iniciar_cadastro()

    elif operacao == 2:
        consultar_cadastro()

    elif operacao == 3:
        exibir_resultados()

    else:
        print('Operação inválida! Tente novamente.\n')
