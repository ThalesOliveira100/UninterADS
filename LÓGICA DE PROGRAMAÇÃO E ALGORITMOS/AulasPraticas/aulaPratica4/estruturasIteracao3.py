# Algoritmo que lê valores e imprime a quantidade de cédulas necessárias para pagar esse mesmo valor.
# Devem ser utilizados apenas valores inteiros e com cédulas de R$200, R$100, R$50, R$10, R$5 e R$1.

valor = int(input('Qual o valor a ser impresso?\n>> '))

# contadores
cedulas200 = 0
cedulas100 = 0
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas5 = 0
cedulas1 = 0

while valor >= 0:
    if valor >= 200:
        cedulas200 += 1
        valor -= 200
        continue

    if valor >= 100:
        cedulas100 += 1
        valor -= 100
        continue

    if valor >= 50:
        cedulas50 += 1
        valor -= 50
        continue

    if valor >= 20:
        cedulas20 += 1
        valor -= 20
        continue

    if valor >= 10:
        cedulas10 += 1
        valor -= 10
        continue

    if valor >= 5:
        cedulas5 += 1
        valor -= 5
        continue

    if valor >= 1:
        cedulas1 += 1
        valor -= 1
        continue

    if valor == 0:
        print('Cédulas de R$ 200,00: {}\n'
              'Cédulas de R$ 100,00: {}\n'
              'Cédulas de R$ 50,00: {}\n'
              'Cédulas de R$ 20,00: {}\n'
              'Cédulas de R$ 10,00: {}\n'
              'Cédulas de R$ 5,00: {}\n'
              'Cédulas de R$ 1,00: {}'.format(cedulas200, cedulas100, cedulas50, cedulas20, cedulas10, cedulas5, cedulas1))
        break
