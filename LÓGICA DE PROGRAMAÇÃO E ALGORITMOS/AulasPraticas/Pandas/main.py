import pandas as pd

#
# Acesso aos dados
#
df = pd.read_csv('pokemon_data.csv')  # Data Frame

# visualiza colunas.
print(df.columns)

# visualiza primeiros e ultimos registros com base no valor indicado.
print(df.head(3))
print(df.tail(2))

# Acessar colunas especificas
print(df['Nome'])
print(df[['Nome', 'Tipo 1']][0:151])

# Acessar linhas especificas
print(df.iloc[:4])
print(df.iloc[2, 1])  # linha, coluna
print(df.loc[df['Tipo 1'] == 'Fogo'])

