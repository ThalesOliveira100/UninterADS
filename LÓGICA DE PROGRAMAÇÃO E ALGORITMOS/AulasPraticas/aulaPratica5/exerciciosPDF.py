def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print('{} '.format(i), end='')
    print('')


def retorna_valores_de_listas(lista):
    texto = ''
    for i in lista:
        texto += '{} '.format(i)

    return texto


def maior_2_menor(valor1, valor2, valor3):
    lista = [valor1, valor2, valor3]
    lista.sort()

    print('Ordem crescente: {}'.format(retorna_valores_de_listas(lista)), end='')
    print('')


def maior_2_menor_main():
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    valor3 = int(input('Digite o terceiro valor: '))
    maior_2_menor(valor1, valor2, valor3)


def valida_inteiro(numero):
    try:
        numero = int(numero)
        if numero > -1:
            if isinstance(numero, int):
                return numero
            else:
                print('O valor informado é décimal, não inteiro!')
                return -1
        else:
            print('O número não pode ser negativo!')
            return -1

    except ValueError:
        print('O valor informado deve ser um número inteiro!')
        return -1


def calcula_fatorial(numero):
    valor = valida_inteiro(numero)
    fatorial = 1
    if valor == -1:
        print('Ocorreram erros durante o cálculo...')
    else:
        if valor > 0:
            for i in range(valor, 1, -1):
                fatorial *= valor
                valor -= 1

        return fatorial


def calcula_valores_inteiros_positivos_entre(inicio, fim):
    soma = 0
    i = inicio

    while i <= fim:
        soma += i
        i = i + 1
    print(soma)


contador(5, 40, 1)
print(calcula_fatorial(0))
calcula_valores_inteiros_positivos_entre(5, 10)


