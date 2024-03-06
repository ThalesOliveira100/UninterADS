# Exercício de leitura e denominação de triângulos
import sys

# 1. Triângulo equilátero:
# Todos os lados são congruentes.

# 2. Triângulo isósceles:
# Dois lados são congruentes.

# 3. Triângulo escaleno:
# Todos os lados são diferentes.

A = int(input('Informa o lado A do triângulo: '))
B = int(input('Informa o lado B do triângulo: '))
C = int(input('Informa o lado C do triângulo: '))


if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A == B and B == C:
            print('O triângulo é equilátero!')

        elif ((A == B and A != C)
              or (A == C and A != B)
              or (B == C and B != A)):
            print('O triângulo é isósceles!')

        else:
            print('O triângulo é escaleno!')
    else:
        print('\nO triângulo não pode ser formado!\n'
              'Algum dos valores indicados é maior que a soma dos outros dois!')
else:
    print('\nO triângulo não pode ser formado!\n'
          'Algum dos valores indicados é igual à zero! ')
