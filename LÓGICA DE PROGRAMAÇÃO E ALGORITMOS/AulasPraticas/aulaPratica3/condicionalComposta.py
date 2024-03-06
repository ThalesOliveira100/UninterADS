# Exercício de escrita de condicionais compostas em Python

# A) Se ano é divisível por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente não é um
# ano bissexto"

ano = int(input('Qual o ano a ser analisado? '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bisexto')

# B) Se ambas as variáveis booleanas cima e baixo forem True, escreva: "Decida-se", caso contrário, escreva: "Agora você
# escolheu o seu caminho"

cima = False
baixo = True
if all([cima, baixo]):
    print('Decida-se')
else:
    print('Agora você escolheu o seu caminho.')
