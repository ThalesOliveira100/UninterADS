# VARIÁVEIS GLOBAIS
_estabelecimento_id_global = 1
_estabelecimentos_lista = [{
    'nome': 'ESTABELECIMENTO 1 - EXEMPLO',
    'endereco': 'Av. Teste, Num: 123',
    'responsavel': 'Thales Oliveira',
    'ativo': True
}]
_cliente_id_global = 1
_clientes_lista = [{
    'id': 0,
    'nome': 'CONSUMIDOR FINAL',
    'numero': None,
    'email': None,
    'endereco': _estabelecimentos_lista[0]['endereco'],
    'desconto': 0,
    'ativo': True
}]
_funcionario_id_global = 0
_funcionarios_lista = []
_produto_id_global = 0
_produtos_lista = []


def cadastrar_estabelecimento(id_estabelecimento):
    nome = input('Informe o nome do estabelecimento: ')
    endereco = input('Informe o endereco do estabelecimento: ')
    responsavel = input('Informe o nome do responsável pelo estabelecimento: ')

    print('O estabelecimento {}, {}, foi cadastrado com sucesso!\n'
          .format(id_estabelecimento, nome))

    _estabelecimentos_lista.append({
        'id': id_estabelecimento,
        'nome': nome,
        'endereco': endereco,
        'responsavel': responsavel,
        'ativo': True
    })


def cadastrar_cliente(id_cliente):
    nome = input('Informe o nome do cliente: ')
    numero = input('Informe o número do cliente: ')
    email = input('Informe o e-mail do cliente: ')

    informa_endereco = bool(input('Deseja informar o endereco do cliente? 0 - Não | 1 - Sim:  '))
    if informa_endereco:
        endereco = input('Informe o endereço do cliente: ')
    else:
        endereco = ''

    tem_desconto = bool('O cliente terá desconto fixo nas compras? 0 - Não | 1 - Sim:  ')
    if tem_desconto:
        porcentagem_desconto = float(input('Informe a porcentagem do desconto: % '))
    else:
        porcentagem_desconto = 0

    print('O cliente {}, {}, foi cadastrado com sucesso!\n'
          .format(_cliente_id_global, nome))

    _clientes_lista.append({
        'id': id_cliente,
        'nome': nome,
        'numero': numero,
        'email': email,
        'endereco': endereco,
        'desconto': porcentagem_desconto,
        'ativo': True
    })


def cadastrar_funcionario(id_funcionario):
    nome = input('Informe o nome do funcionario: ')
    email = input('Informe o e-mail do funcionario: ')
    cargo = input('Informe o cargo do funcionário: ')

    tem_comissao = bool(input('O funcionário trabalha com comissão? 0 - Não | 1 - Sim:  '))
    if tem_comissao:
        porcentagem_comissao = float(input('Informe o percentual de comissão do funcionário: '))
    else:
        porcentagem_comissao = 0

    print('O funcionario {}, {}, foi cadastrado com sucesso!\n'
          .format(_funcionario_id_global, nome))

    _funcionarios_lista.append({
        'id': id_funcionario,
        'nome': nome,
        'email': email,
        'cargo': cargo,
        'comissao': porcentagem_comissao,
        'ativo': True
    })


def cadastrar_produto(id_produto):
    nome = input('Informe o nome do produto: ')
    preco = input('Informe o preço do produto: ')

    definir_saldo = bool(input('Deseja definir o saldo inicial do produto? 0 - Não | 1 - Sim:  '))
    if definir_saldo:
        saldo = float(input('Informe o saldo inicial do produto: '))
    else:
        saldo = 0

    print('O produto {}, {}, foi cadastrado com sucesso!\n'
          .format(_produto_id_global, nome))

    _produtos_lista.append({
        'id': id_produto,
        'nome': nome,
        'preco': preco,
        'saldo': saldo,
        'ativo': True
    })


def consultar_estabelecimento(filtro=None, campo=''):
    estabelecimentos_encontrados = []
    try:
        if filtro is None:
            for estabelecimento in _estabelecimentos_lista:
                estabelecimentos_encontrados.append(estabelecimento)

        elif filtro.lower() in _estabelecimentos_lista:
            for estabelecimento in _estabelecimentos_lista:
                if estabelecimento[campo].find(filtro):
                    estabelecimentos_encontrados.append(estabelecimento)
        # else:
        #     for estabelecimento in _estabelecimentos_lista:
        #         for item in estabelecimento.values():
        #             resultado = item
        #             if resultado.find(filtro):
        #                 estabelecimentos_encontrados.append(resultado)
    except AttributeError:
        pass
    finally:
        print(estabelecimentos_encontrados)


def menu_cadastros(estabelecimento_id_global, funcionario_id_global, cliente_id_global, produto_id_global):
    while True:
        print('-' * 17 + '\n| MENU CADASTROS|\n' + '-' * 17)
        print('Entre com a operacao desejada: \n')
        print('1 - CADASTRAR ESTABELECIMENTO')
        print('2 - CADASTRAR FUNCIONARIOS')
        print('3 - CADASTRAR CLIENTES')
        print('4 - CADASTRAR PRODUTOS')
        print('5 - VOLTAR')
        operacao_cadastro = int(input('>> '))

        if operacao_cadastro == 1:
            estabelecimento_id_global += 1
            cadastrar_estabelecimento(estabelecimento_id_global)

        elif operacao_cadastro == 2:
            funcionario_id_global += 1
            cadastrar_funcionario(funcionario_id_global)

        elif operacao_cadastro == 3:
            cliente_id_global += 1
            cadastrar_cliente(cliente_id_global)

        elif operacao_cadastro == 4:
            produto_id_global += 1
            cadastrar_produto(produto_id_global)

        elif operacao_cadastro == 5:
            break
        else:
            print('Opção Inválida, tente novamente!\n')


def menu_consulta_estabelecimentos():
    while True:
        print('1 - Consultar por nome')
        print('2 - Consultar por endereço')
        print('3 - Consultar por responsável')
        print('4 - Consultar todos')
        print('5 - Voltar')
        operacao_consulta_estabelecimento = int(input('>> '))

        if operacao_consulta_estabelecimento == 1:
            nome_consulta = input('>> ')

        elif operacao_consulta_estabelecimento == 2:
            endereco_consulta = input('>> ')

        elif operacao_consulta_estabelecimento == 3:
            responsavel_consulta = input('>> ')

        elif operacao_consulta_estabelecimento == 4:
            consultar_estabelecimento()

        elif operacao_consulta_estabelecimento == 5:
            break
        else:
            print('Opção Inválida, tente novamente!\n')



def menu_consultas(estabelecimento_lista, funcionario_lista, cliente_lista, produto_lista):
    while True:
        print('-' * 17 + '\n| MENU CONSULTAS|\n' + '-' * 17)
        print('Entre com a operacao de consulta desejada: \n')
        print('1 - Estabelecimento')
        print('2 - Funcionário')
        print('3 - Cliente')
        print('4 - Produto')
        print('5 - Voltar')
        operacao_consulta = int(input('>> '))

        if operacao_consulta == 1:
            pass

        elif operacao_consulta == 2:
            pass

        elif operacao_consulta == 3:
            pass

        elif operacao_consulta == 4:
            pass

        elif operacao_consulta == 5:
            break
        else:
            print('Opção Inválida, tente novamente!\n')


# PROGRAMA PRINCIPAL
while True:
    print('-' * 32 + '\n| SISTEMA DE GESTÃO DE ESTOQUE |\n' + '-' * 32)
    print('Entre com a operacao desejada: \n')
    print('1 - CADASTROS')
    print('2 - CONSULTAS')
    print('3 - ESTOQUE')
    print('4 - FATURAMENTO')
    print('5 - SAIR')
    operacao = int(input('>> '))

    if operacao == 1:
        menu_cadastros(_estabelecimento_id_global, _funcionario_id_global, _cliente_id_global, _produto_id_global)
    elif operacao == 2:
        menu_consultas(_estabelecimentos_lista, _funcionarios_lista, _clientes_lista, _produtos_lista)
    elif operacao == 3:
        pass
    elif operacao == 4:
        pass
    elif operacao == 5:
        exit('Execução finalizada...')
    else:
        print('Opção Inválida, tente novamente!\n')
