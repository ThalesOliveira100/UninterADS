# Perguntar a quantidade de km percorridos, e a quantidade de dias com o carro alugado
quantidade_km_percorridos = float(input('Qual foi a quantidade de KM percorridos? '))
quantidade_dias_alugados = int(input('Qual foi a quantidade de dias com o carro alugado? '))

# Calcular o preço a pagar, tendo que o carro custa R$60 ao dia e R$0,15 por km rodados
valor_ao_dia = int(60)
valor_por_KM = float(0.15)

valor_a_pagar = quantidade_km_percorridos * valor_por_KM + quantidade_dias_alugados + valor_ao_dia
print('O valor total a pagar será de R${}'
      .format(valor_a_pagar))
