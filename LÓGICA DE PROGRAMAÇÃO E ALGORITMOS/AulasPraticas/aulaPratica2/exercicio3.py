# String que recebera uma frase qualquer
frase = input('Digite uma frase qualquer: ')

# Criar uma segunda variável com metade da string digitada
meia_quantidade = int(len(frase)/2)
meia_frase = frase[:meia_quantidade]

# Imprimir os dois ultimos caracteres da segunda variável
print(meia_frase[-2:])
