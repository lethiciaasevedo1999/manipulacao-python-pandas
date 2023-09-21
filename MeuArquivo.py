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

# ticket médio por produto em cada loja 

# enviar um e-mail com relatório 