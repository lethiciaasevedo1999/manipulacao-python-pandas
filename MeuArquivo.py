import pandas as pd 
import win32com.client as win32



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


outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'lethiciaasevedo@hotmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados, </p>

<p>Segue o relatório analisado pela equipe, analisando os dados descritos em tabelas da loja, de forma resumida:</p>

<p>Faturamento: </p>
{faturamento.to_html}


<p>Quantidade vendida: </p>
{quantidade.to_html}


<p>Ticket Médio dos produtos em cada loja: </p>
{ticket_medio.to_html}

<p>Qualquer dúvida estou á disposição.</p>

<p>Atenciosamente.</p>


'''

mail.Send()

print('Email enviado com sucesso')