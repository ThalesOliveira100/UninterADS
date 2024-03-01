import sys

print('Bem-Vindo a Loja do Thales Gabriel Moreira de Oliveira 4675362')

try:
    valor_unitario = float(input('Entre com o valor unitário do produto: R$ '))
    quantidade = float(input("Entre com a quantidade do produto: "))
except ValueError as e:
    print('Um valor não esperado foi informado, certifique-se de que os valores sejam escritos de forma numérica.')
    sys.exit()

valor_total_compra = (valor_unitario * quantidade)

# Define a porcentagem inicial como 0, a porcentagem é a variável responsável pelo calculo do valor com o desconto e
# pela exibição da porcentagem calculada no segundo print, por isso, foi utilizada como valor inteiro.
porcentagem = 0

if 2500 > valor_total_compra:
    porcentagem = 0
elif 2500 <= valor_total_compra < 6000:
    porcentagem = 4
elif 6000 <= valor_total_compra < 10000:
    porcentagem = 7
else:
    porcentagem = 11

valor_com_desconto = valor_total_compra - (valor_total_compra * porcentagem / 100)

# A formatação :.2f tem a finalidade de exibir apenas duas casas decimais nos valores exibidos, não foi solicitado, mas
# é essencial em négocios reais.
print('O valor sem desconto foi R$ {:.2f}'.format(valor_total_compra))
print('O valor com desconto foi R$ {:.2f} (desconto {}%)'.format(valor_com_desconto, porcentagem))
