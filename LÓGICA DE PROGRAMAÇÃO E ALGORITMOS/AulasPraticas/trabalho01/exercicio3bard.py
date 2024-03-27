def escolha_servico():
    # Pergunta o serviço desejado e retorna o valor do serviço.
    while True:
        servico = input("Entre com o tipo de serviço desejado: "
                        "\nDIG - Digitalização"
                        "\nICO - Impressão Colorida"
                        "\nIPB - Impressão Preto e Branco"
                        "\nFOT - Fotocópia\n>> ").lower()
        if servico in ("dig", "ico", "ibo", "fot"):
            return servico_valor[servico]
        else:
            print("Escolha inválida. \nEntre com o tipo de serviço desejado novamente.>> ")


def num_pagina():
    # Pergunta o número de páginas e retorna o número de páginas com desconto.
    while True:
        try:
            num_paginas = int(input("Entre com o número de páginas: "))
            if num_paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez.")
            elif num_paginas >= 2000:
                return num_paginas * 0.75
            elif num_paginas >= 200:
                return num_paginas * 0.8
            elif num_paginas >= 20:
                return num_paginas * 0.85
            else:
                return num_paginas
        except ValueError:
            print("Número de páginas inválido. Digite novamente.")


def servico_extra():
    # Pergunta pelo serviço adicional e retorna a opção escolhida.
    while True:
        extra = input("Deseja adicionar mais algum serviço? "
                      "\n1 - Encadernação Simples - R$ 10,00"
                      "\n2 - Encadernação Capa Dura - R$ 25,00"
                      "\n0 - Não desejo mais nada\n")

        if extra in ("1", "2", "0"):
            return extra
        else:
            print("Escolha Inválida!\n Entre com o serviço desejado novamente:")


# Dicionário com os valores dos serviços
servico_valor = {
    "dig": 1.10,
    "ico": 1.00,
    "ibo": 0.40,
    "fot": 0.20
}

# Dicionário com os valores dos serviços extras
servico_extra_valor = {
    "1": 15.00,
    "2": 40.00,
    "0": 0.00
}


print('Bem vindo à copiadora do Thales Gabriel Moreira de Oliveira')

# Chamada das funções para obter as informações do pedido
servico = escolha_servico()
num_paginas = num_pagina()
extra = servico_extra()

# Cálculo do total a pagar
total = servico * num_paginas + servico_extra_valor[extra]

# Exibição do total a pagar
print(f"Total (R$): {total:.2f} (servico: {str(servico).replace('.',',')} * paginas: {num_paginas:.2f} + extra(s): {servico_extra_valor[extra]})")
