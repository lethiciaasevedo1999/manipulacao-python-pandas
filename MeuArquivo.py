import pandas as pd 



# importar a base de dados 
tabela_vendas = pd.read_excel ('Vendas.xlsx')


# visualizar a base de dados 
pd.set_option('display.max_columns', None) #faz com que o terminal mostre todas as colunas sem cortes

print(tabela_vendas)


# faturamento por loja 
faturamento = tabela_vendas [['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

print(faturamento)


# quantidade de produtos vendidos por loja 
quantidade = tabela_vendas [['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

print(quantidade)

# ticket médio por produto em cada loja 
ticket_medio = 

# enviar um e-mail com relatório 