print('Bem-Vindo a Loja de Gelados do Thales Gabriel Moreira de Oliveira 4675362')
print('-------------------------------- Cardápio --------------------------------')
print('------------------| Tamanho | Cupuaçu (CP) | Açaí (AC) | -----------------')
print('------------------|    P    |   R$ 10,00   | R$ 12,00  | -----------------')
print('------------------|    M    |   R$ 15,00   | R$ 17,00  | -----------------')
print('------------------|    G    |   R$ 17,00   | R$ 21,00  | -----------------')
print('--------------------------------------------------------------------------')

# Variáveis importantes ao longo do programa que são inicializadas antes pois para não ter problemas no escopo.
sabor = ''
tamanho = ''
valor_total = 0

while True:
    sabor = str(input('\nEntre com o sabor desejado (CP/AC): '))

    # Se o sabor selecionda for CP, executará este bloco, onde verificará o tamanho, e em seguida calculará o preço.
    if sabor.upper() == 'CP':
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

        if tamanho == 'P':
            valor_total += 10
        elif tamanho == 'M':
            valor_total += 15
        elif tamanho == 'G':
            valor_total += 17
        else:
            print('Tamanho Inválido. Tente novamente!')
            continue

    # Se o sabor selecionda for AC, executará este bloco, onde verificará o tamanho, e em seguida calculará o preço.
    elif sabor.upper() == 'AC':
        tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()

        if tamanho == 'P':
            valor_total += 12
        elif tamanho == 'M':
            valor_total += 17
        elif tamanho == 'G':
            valor_total += 21
        else:
            print('Tamanho Inválido. Tente novamente!')
            continue
    else:
        print('Sabor Inválido. Tente novamente!')
        continue

    # Pergunta se o usuário deseja comprar algo a mais, se sim o laço se repete, se não o laço é encerrado.
    mais_pedidos = input('Deseja mais alguma coisa? (S/ digite outra tecla) ').upper()
    if mais_pedidos == 'S':
        continue
    else:
        break

# A notação ":.2f" serve para limitar as casas decimais exibidas ao usuário.
print('\nO valor total a ser pago: R$ {:.2f}'.format(valor_total))
