# Escreva um algoritmo que crie uma tupla com 10 palavras.
# Encontre dentro dessa tupla as vogais de cada palavra.
# Faça um print na tela com o nome da palavra e sua respectivas vogais.

palavras = input('Digite as palavras separadas por espaço.\n>>  ')
tupla = tuple(palavras.split(' '))

vogais_encontradas = []

for palavra in tupla:
    for letra in palavra:
        if letra.lower() in 'aiueo':
            if letra not in vogais_encontradas:
                vogais_encontradas.append(letra)
    print('\nPalavra: {}\nVogais encontradas: {}'.format(palavra, vogais_encontradas))
    vogais_encontradas.clear()
