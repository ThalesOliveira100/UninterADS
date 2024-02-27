# Solicitar ao usuário o preço de um produto e o percentual de desconto a ser aplicado
preco_normal = float(input('Qual o preço do produto? R$'))
percentual = float(input('Qual o percentual a ser aplicado? %'))

# Calcular e exibir o valor do desconto e o preço final do produto.
preco_desconto = (preco_normal * percentual) / 100
novo_preco = preco_normal - preco_desconto

print('O preço do produto normal R${}, com o percentual de {}% é igual à R${}'
      .format(preco_normal, percentual, novo_preco))

