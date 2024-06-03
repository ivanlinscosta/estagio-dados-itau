#Autor: Ricard Veiga Coelho
#email: rvcoelho0@gmail.com
#CPF: 449.152.598-62

#Imports que usarei
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns

db = pd.read_csv('Ecommerce_DBS.csv')

#Visualizando colunas para remover as desnecessárias
db.info()

#checando categorias da base de dados
db['Product Category'].unique()

# Limpeza de dados

#Removendo colunas desnecessárias
db.drop(columns=['Purchase Date', 'Country', 'State', 'Latitude', 'Longituide'], axis=1, inplace=True)

#Removendo linhas com missing values
db.dropna(inplace=True)

db = db.drop_duplicates()

#Renomeação de colunas

db.columns = db.columns.str.lower().str.replace(' ', '_').str.rstrip('_')
db.info()

#Criação de faixas etárias

bins = [18, 28, 39, 49, 59, 69, 100]
labels = ['18-28', '29-39', '39-49', '49-59', '59-69', '70+']

db['age_group'] = pd.cut(db['customer_age'], bins=bins, labels=labels, right=False)

# Criação de bases de dados separados por categorias para uso de análises futuras

home = db[db['product_category'] == 'Home']
electronics = db[db['product_category'] == 'Electronics']
books = db[db['product_category'] == 'Books']
clothing = db[db['product_category'] == 'Clothing']

# 1) Quais os produtos mais vendidos considerando os últimos 3 anos?

#Achando produtos mais vendidos dos últimos 3 anos (2020 à 2022)
#Como não temos código do produto nem nome do produto, a minha estratégia será pegar produtos de mesma categoria e preço e assumir que são iguais quando essas duas colunas forem iguais.
#No entanto é importante ressaltar que é possível que diferentes produtos de mesma categoria tenham o mesmo preço, o que pode gerar resultados incorretos em análise de outras colunas, como por exemplo, NPS de um suposto produto, pois se ocorrer esse caso, podem ser produtos diferentes de mesmo preço com NPS médio bem diferentes

top_products = db.groupby(["product_category", "product_price"]).count()
top10_products = top_products.sort_values(by="total_purchase_amount", ascending=False).head(10).filter(items=["product_category", "product_price", "total_purchase_amount"]).reset_index()
top10_products.style.set_caption("10 produtos mais vendidos")

top10_products['position'] = range(1, len(top10_products) + 1)

plt.figure(figsize=(5,3))
sns.barplot(data=top10_products, y='position', x='total_purchase_amount', orient='h')
plt.title('10 produtos mais vendidos da plataforma')
plt.xlabel('Quantidades vendidas')
plt.ylabel('Ranking de cada produto')
plt.xlim(170, None)
plt.grid(True)
plt.show()

#Interpretação de linhas: o livro de preço 48 vendeu 192 unidades, e assim por diante.

#Também poderiam ser simplesmente as linhas com maiores valores de "Total Purchase Amount", mas creio que isso indique a quantidade total de compras por Customer ID, e não quantidade total de mesmo produto vendido, portanto ignorarei essa possibilidade
#db.sort_values(by="Total Purchase Amount", ascending=False).head(10)

# 2) Qual o produto mais caro e o mais barato?

#Produto mais caro:
idx = db["product_price"].idxmax()
db_maior_preco = db.loc[idx]
print(db_maior_preco)

#Conversão pra Series, pegando apenas o que identifica o produto: categoria e preço
serie = pd.Series(db_maior_preco)
produto_mais_caro = serie[['product_category', 'product_price']]
print(produto_mais_caro)

#Produto mais caro: eletrônico de valor 500.

#Produto mais barato
idx = db["product_price"].idxmin()
db_menor_preco = db.loc[idx]
print(db_menor_preco)

#Conversão pra Series, pegando apenas o que identifica o produto: categoria e preço
serie = pd.Series(db_menor_preco)
produto_mais_barato = serie[['product_category', 'product_price']]
print(produto_mais_barato)

#Produto mais barato: eletrônico de valor 10.

# 3) Qual a categoria de produto mais vendida e menos vendida? Qual a categoria mais e menos cara?

#Categorias mais e menos vendida
categories_ranked_by_sold_volume = db.groupby("product_category").count().sort_values(by="total_purchase_amount", ascending=False).filter(items=["product_category", "total_purchase_amount"])
categories_ranked_by_sold_volume

plt.figure(figsize=(5,3))
sns.barplot(data=categories_ranked_by_sold_volume, x='product_category', y='total_purchase_amount', orient='v')
plt.title('Volume de vendas por categoria')
plt.xlabel('Categorias')
plt.ylabel('Volume vendido')
plt.show()

#Categorias mais e menos caras
categories_ranked_by_average_price = db.groupby("product_category")["product_price"].mean().round(3).reset_index().sort_values(by="product_price", ascending=False)
categories_ranked_by_average_price

#Categoria mais vendida: roupas, porém praticamente empatado com livros

#Categoria menos vendida: casa, porém praticamente empatado com eletrônicos

percentiles = [0.25, 0.50, 0.75, 0.90, 0.95, 0.99]

home['product_price'].quantile(percentiles)

electronics['product_price'].quantile(percentiles)

books['product_price'].quantile(percentiles)

clothing['product_price'].quantile(percentiles)

#Como as distribuições de preços são extremamente semelhantes, não é possível determinar uma categoria mais cara e mais barata, pois são todas praticamente iguais ao todo.

# 4) Qual o produto com melhor e pior NPS?

db.groupby(["product_category", "product_price"])["nps"].mean().round(3).reset_index().sort_values(by="nps", ascending=False).filter(items=["product_category", "product_price", "nps"])

#Produto com melhor NPS: produto da categoria casa de valor 64 com NPS médio de 6,157

#Produto com pior NPS: produto da categoria de eletrônicos de valor 64 com NPS médio de 4,065

# Analisando a base de dados, qual o tipo de público (considerando gênero e idade) e o canal ideal para vender determinado tipo de produto?

#Primeiramente irei verificar o tipo de distribuição de faxas etárias para checar se há faixas etárias mais prevalecentes. 

plt.figure(figsize=(10,6))
plot = sns.histplot(data=db, x='age_group', hue='gender', multiple='dodge', palette={'Male': '#2a3bd4', 'Female': '#d63a85'})
plt.title('Distribuição de idades dos clientes por gênero')
plt.xlabel('Faixas etárias')
plt.ylabel('Frequência')
plt.grid(True)
for i in plot.containers:
    plot.bar_label(i)
plt.show()

#Não é possível determinar um público alvo geral pois a distribuição é muito uniforme entre ambos gêneros e faixas etárias.




# E o canal ideal para vender cada produto?

plt.figure(figsize=(10,6))
plot = sns.histplot(data=db, x='source', hue='product_category', multiple='dodge', palette='viridis')
plt.title('Vendas por fonte e categoria')
plt.xlabel('Fontes')
plt.ylabel('Vendas')
plt.grid(True)
for i in plot.containers:
    plot.bar_label(i, rotation=45)
plt.show()

#Podemos ver que apenas pesquisa ôrganica fica abaixo das outras fontes, que tem, entre si, desempenho bastante similar para cada categoria. 
#Portanto também não é possível determinar um canal ideal 

plt.figure(figsize=(10,6))
plot = sns.histplot(data=db, x='product_category', hue='source', multiple='dodge', palette='viridis')
plt.title('Vendas por fonte e categoria')
plt.xlabel('Fontes')
plt.ylabel('Vendas')
plt.grid(True)
for i in plot.containers:
    plot.bar_label(i, rotation=45)
plt.show()

#Fazendo o gráfico trocando fonte por categoria de produto, podemos ver mais claramente 
#que também não há muita diferença de desempenho entre as 3 melhores fontes para cada categoria,
#mas que o instagram tem um desempenho levemente superior que as outras duas.

# Conclusões

#A distribuição não permite que determinemos público alvo considerando gênero e idade devido à uniformidade da distribuição,
#e nem canal ideal, devido ao desempenho muito semelhante entre instagram, SEM e facebook.

#O único insight verdadeiramente útil que conseguimos extrair dessa análise é que o gráfico de volume de vendas por categoria mostra claramente
#que as categorias de livros e roupas são as que tem maior sucesso.