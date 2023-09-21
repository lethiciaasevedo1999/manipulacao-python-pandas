import pandas as pd 



# importar a base de dados 
tabela_vendas = pd.read_excel ('Vendas.xlsx')


# visualizar a base de dados 
pd.set_option('display.max_columns', None) #faz com que o terminal mostre todas as colunas sem cortes

print(tabela_vendas)


# faturamento por loja 
faturamento = tabela_vendas [['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)

print('-' *50)

# quantidade de produtos vendidos por loja 
quantidade = tabela_vendas [['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(quantidade)

print('-' *50)

# ticket médio por produto em cada loja 
ticket_medio = (faturamento['Valor Final'] / quantidade [ 'Quantidade']).to_frame()

print(ticket_medio)

# enviar um e-mail com relatório 