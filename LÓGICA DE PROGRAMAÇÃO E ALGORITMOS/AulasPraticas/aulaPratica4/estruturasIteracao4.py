# Cobrança de preçs no cinema de acordo com a idade
# idade > 3: gratuito
# idade entre 3 e 12 anos: R$ 15
# idade maior que 12 anos: R$ 30
# teste

total_visitantes = 0
total_dinheiro_arrecadado = 0

while True:
    opcao = input('Quantos anos você tem?\n>> ')

    if opcao.lower() == 's':
        try:
            media = total_dinheiro_arrecadado / total_visitantes
        except ZeroDivisionError as e:
            media = 0

        print('\nVocê escolheu sair!'
              '\nHoje tivemos o total de {} visitantes, e {} de reais acumulados!'
              '\nA média de lucrativadade do dia foi de R$ {:.2}!'
              .format(total_visitantes, total_dinheiro_arrecadado, media))
        break

    try:
        idade = int(opcao)

        if idade < 3:
            precoEntrada = 'gratuito!'

        elif 3 <= idade <= 12:
            precoEntrada = 'R$ 15,00'
            total_dinheiro_arrecadado += 15

        elif idade > 12:
            precoEntrada = 'R$ 30,00'
            total_dinheiro_arrecadado += 30

        total_visitantes += 1
        print('O ingresso será {}\n'.format(precoEntrada))

    except ValueError as e:
        print('O valor informado não é uma idade, ou não é o comando para sair!')
        continue
