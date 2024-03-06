print('Bem vindo à copiadora do Thales Gabriel Moreira de Oliveira')


def printa_servicos():
    print('DIG - Digitalização'
          '\nICO - Impressão Colorida'
          '\nIPB - Impressão Preto e Branco'
          '\nFOT - Fotocópia')


def escolhe_servico():
    try:
        print('Entre com o serviço desejado: ')
        printa_servicos()
        servico = input()

        if servico == 'DIG':
            pass
        elif servico == 'ICO':
            pass
        elif servico == 'IPB':
            pass
        elif servico == 'FOT':
            pass
    except:
        print('Escolha Inválida!\n Entre com o serviço desejado novamente:')
        printa_servicos()


def num_paginas(servico):
    pass


escolhe_servico()