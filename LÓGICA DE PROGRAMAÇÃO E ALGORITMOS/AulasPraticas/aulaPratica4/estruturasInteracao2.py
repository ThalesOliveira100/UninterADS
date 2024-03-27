# Calculadora básica
# Escreva um algoritmo que leia dois valores númericos, e que pergunte ao usuário qual operação ele deseja realizar:
# Adição (+), Subtração (-), Multiplicação (*) ou Divisão (/)
# Exiba na tela o resultado da operação desejada.

while True:
    print('='*33)
    print('='*10, 'CALCULADORA', '='*10)
    print('='*33)

    try:
        valor1 = int(input('\nInforme o primeiro valor: \n>> '))
        valor2 = int(input('Informe o segundo valor: \n>> '))
        total = 0

        operacao = input('Informe a operação a ser realizada:'
                         '\n( + ) Adição'
                         '\n( - ) Subtração'
                         '\n( * ) Multiplicação'
                         '\n( / ) Divisão\n>> ')

        if operacao == '+':
            total = valor1 + valor2

        elif operacao == '-':
            total = valor1 - valor2

        elif operacao == '*':
            total = valor1 * valor2

        elif operacao == '/':
            total = valor1 / valor2

        print(f'O resultado entre {valor1} {operacao} {valor2} é {total} !\n')

    except ValueError:
        print('O valor deve ser númerico! Informe os valores novamente.')
    finally:
        continua = input('Deseja sair? S/N\n>> ')
        if continua.lower() == 's':
            break
        else:
            pass
