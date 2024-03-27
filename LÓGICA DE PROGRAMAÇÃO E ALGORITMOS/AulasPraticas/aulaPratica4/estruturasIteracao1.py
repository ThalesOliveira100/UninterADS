# Realize a sequência de print com for e while:
# a) Inteiros de 3 até 12, com 12 incluso
# b) Inteiros de 0 até 9, excluindo 9, com passo de 2

def a_com_while():
    i = 3
    while i <= 12:
        print(i)
        i += 1


def a_com_for():
    for i in range(3, 13, 0):
        print(i)


def b_com_while():
    i = 0
    while i <= 9:
        if i % 2 == 0:
            print(i)
        i += 1


def b_com_for():
    for i in range(0, 9, 2):
        print(i)


b_com_while()
