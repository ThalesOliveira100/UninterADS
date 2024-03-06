# Exercicios de condicinais simples em Python
# Traduza as afirmações a seguir para condicionais em Python

# A) Se a idade é maior que 60, excreva:"Voce tem direitos aos beneficios"

idade = int(input('Qual a sua idade? '))
if idade > 60:
    print('Você tem direitos aos benefícios')

# B) Se dano é maior do que 10 e escudo é igual a 0, escreva "Você está morto"

dano = int(input('Qual o valor do dano recebido? '))
escudo = int(input('Qual o valor atual do escudo? '))
if dano > 10 and escudo == 0:
    print('Você está morto :(')

# C) Se pelo menos umas das váriáveis booleanas: norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
norte = False
sul = True
leste = False
oeste = False

if any([norte, sul, leste, oeste]):
    print('Você escapou!')
