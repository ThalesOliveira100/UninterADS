print('Bem vindo a Loja do THALES OLIVEIRA - 4675362')

while True:
    try:
        valor_unitario = float(input('Entre com o valor unitário do produto: R$ '))

        while True:
            try:
                quantidade = float(input('Entre com a quantidade do produto: '))
                break
            except ValueError:
                print('\nA quantidade do produto deve ser númerica! Preencha o campo novamente.\n')
                continue

        valor_total_compra = (valor_unitario * quantidade)

        # Define a porcentagem inicial como 0, a porcentagem é a variável responsável pelo calculo do valor com o
        # desconto e pela exibição da porcentagem calculada no segundo print, por isso, foi utilizada como valor
        # inteiro.
        porcentagem = 0

        if 2500 > valor_total_compra:
            porcentagem = 0
        elif 2500 <= valor_total_compra < 6000:
            porcentagem = 4
        elif 6000 <= valor_total_compra < 10000:
            porcentagem = 7
        else:
            porcentagem = 11

        valor_com_desconto = valor_total_compra - (valor_total_compra * porcentagem / 100)

        # A formatação :.2f tem a finalidade de exibir apenas duas casas decimais nos valores exibidos,
        # não foi solicitado, mas é essencial em négocios reais.
        print('O valor sem desconto foi R$ {:.2f}'.format(valor_total_compra))
        print('O valor com desconto foi R$ {:.2f} (desconto {}%)'.format(valor_com_desconto, porcentagem))
    except ValueError:
        print('\nO valor unitário deve ser informado de forma númerica! Informe o campo novamente.\n')
        continue
    finally:
        continua = input('Deseja sair? S/N\n>> ')
        if continua.lower() == 's':
            break
        else:
            pass
