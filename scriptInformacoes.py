import pandas as pd

# Carregar o arquivo CSV
data = pd.read_csv('./Ecommerce_DBS.csv')


####################  TIPO DE PRODUTO MAIS VENDIDO EM 3 ANOS  #################

# Converter a coluna 'Purchase Date' para o tipo datetime
data['Purchase Date'] = pd.to_datetime(data['Purchase Date'], format='%d/%m/%Y')
# Filtrar os dados dos últimos 3 anos
data_recent = data[data['Purchase Date'] > pd.to_datetime('today') - pd.DateOffset(years=3)]
# Obter o tipo de produto mais vendido
tipo_mais_vendido = data_recent['Product Category'].mode()[0]
print("O tipo de produto mais vendido nos últimos 3 anos é:", tipo_mais_vendido)

####################  COMPRA MAIS BARATA E MAIS CARA  #################

# Encontrar a linha da compra mais cara
linha_mais_cara = data.loc[data['Product Price'].idxmax()]
# Encontrar a linha da compra mais barata
linha_mais_barata = data.loc[data['Product Price'].idxmin()]
print("Compra mais cara:")
print(linha_mais_cara)
print("\nCompra mais barata:")
print(linha_mais_barata)


####################  CATEGORIAS COM MAIS E MENOS VENDAS  #################


# Contar o número de vendas em cada categoria de produtos
vendas_por_categoria = data['Product Category'].value_counts()

# Encontrar a categoria com mais vendas
categoria_mais_vendida = vendas_por_categoria.idxmax()
vendas_mais_vendida = vendas_por_categoria.max()

# Encontrar a categoria com menos vendas
categoria_menos_vendida = vendas_por_categoria.idxmin()
vendas_menos_vendida = vendas_por_categoria.min()

print("Vendas por categoria:")
print(vendas_por_categoria)

print("\nCategoria com mais vendas:", categoria_mais_vendida)
print("Número de vendas:", vendas_mais_vendida)

print("\nCategoria com menos vendas:", categoria_menos_vendida)
print("Número de vendas:", vendas_menos_vendida)



#################### CATEGORIA DE PRODUTOS MAIS BARATA E MAIS CARA CONSIDERANDO MEDIA DE PREÇO POR CATEGORIA  #################

# Calcular a média dos preços de produtos em cada categoria
media_por_categoria = data.groupby('Product Category')['Product Price'].mean()

# Encontrar a categoria mais cara
categoria_mais_cara = media_por_categoria.idxmax()
preco_mais_caro = media_por_categoria.max()

# Encontrar a categoria mais barata
categoria_mais_barata = media_por_categoria.idxmin()
preco_mais_barato = media_por_categoria.min()

print("\n\n\n##################\nCategoria mais cara:", categoria_mais_cara)
print("Preço médio mais caro:", preco_mais_caro)

print("\nCategoria mais barata:", categoria_mais_barata)
print("Preço médio mais barato:", preco_mais_barato)


#################### NPS  #################

# Calcular a média de NPS para cada categoria de produto
media_nps_por_categoria = data.groupby('Product Category')['NPS'].mean()

# Encontrar a categoria com o maior NPS
categoria_maior_nps = media_nps_por_categoria.idxmax()
maior_nps = media_nps_por_categoria.max()

# Encontrar a categoria com o menor NPS
categoria_menor_nps = media_nps_por_categoria.idxmin()
menor_nps = media_nps_por_categoria.min()

# Calcular a média geral de NPS
media_nps_geral = data['NPS'].mean()

print("\n\n\n##################\nCategoria com maior NPS:", categoria_maior_nps)
print("Media da categora",categoria_maior_nps,":", maior_nps)

print("\nCategoria com menor NPS:", categoria_menor_nps)
print("Media da categora",categoria_menor_nps,":", menor_nps)

print("\nMédia geral de NPS:", media_nps_geral)