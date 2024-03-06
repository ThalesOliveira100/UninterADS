# Cálculo do consumo de energia elétrica
# Escreva um algoritmo que calcule o preço a pagar pelo fornecimento de energia elétrica.
# Pergunte a quantidade de kWh consumida e o tipo de instalação, sendo:
# R para residências, I para indústrias e C para comércios.

while True:
    print('=' * 46)
    print('=' * 10, 'CÁLCULO ENERGIA ELÉTRICA', '=' * 10)
    print('=' * 46)

    try:
        kwh_consumidos = float(input('\nInforme a quantidade de kWh consumidas: \n>> '))
        tipo_instalacao = input('Informe o tipo de instalação:'
                                '\nR -> Residências'
                                '\nI -> Indústrias'
                                '\nC -> Comércios\n>> ').lower()

        if tipo_instalacao in ('r', 'i', 'c'):

            total = 0

            # R é o tipo residencial, e possui duas bases de cálculo, para kWh até 500 e para Kwh acima de 500
            # C é o tipo comercial, e possui duas bases de cálculo, para kWh até 100 e para Kwh acima de 1000
            # I é o tipo industrial, e possui duas bases de cálculo, para kWh até 5000 e para Kwh acima de 5000

            tipos = {
                'r500': 0.4,
                'r>500': 0.65,
                'c1000': 0.55,
                'c>1000': 0.6,
                'i5000': 0.55,
                'i>5000': 0.6
            }

            if tipo_instalacao == 'r':
                if kwh_consumidos > 500:
                    total = kwh_consumidos * tipos['r>500']
                else:
                    total = kwh_consumidos * tipos['r500']

            elif tipo_instalacao == 'i':
                if kwh_consumidos > 5000:
                    total = kwh_consumidos * tipos['i>5000']
                else:
                    total = kwh_consumidos * tipos['i5000']

            elif tipo_instalacao == 'c':
                if kwh_consumidos > 1000:
                    total = kwh_consumidos * tipos['c>1000']
                else:
                    total = kwh_consumidos * tipos['c1000']

            print('Deve ser pago R${:.2f} para o tipo de instalação informado!\n'.format(total))
        else:
            print('Tipo de Instalação não reconhecido. Verifique os campos e tente novamente.')

    except ValueError as e:
        print('A quantidade deve ser numérica! Verifique os campos e tente novamente.')
    finally:
        continua = input('Deseja sair? S/N\n>> ')
        if continua.lower() == 's':
            break
        else:
            pass
