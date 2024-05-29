# Analisando a base de dados, qual o tipo de ´publico (considerando gênero e idade)´ e o canal ideal para vender determinado tipo de produto?

## Roteiro de análise

### Quais são os produtos mais vendidos nos últimos 3 anos?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/0fbbfb77-6312-4b9b-8289-7e6d669cff16)

Nos últimos 3 anos, as categorias de produtos vestuário (164.688 unidades) e livros (163.000 unidades) apresentaram o melhor resultado em termos de quantidade vendida.

### Qual é o produto mais caro e mais barato?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/c75a1b8b-29f0-4fe3-b135-3726f4dcb888)

O gráfico revela que todas as categorias partilham um preço mínimo de 10 dólares e máximo de 500 dólares. Portanto, não podemos concluir quais são os produtos mais caros e quais são os mais baratos.

### Qual é a categoria de produto mais vendida e menos vendida? Qual é a categoria mais e menos cara?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/d39bffce-ea45-4034-829c-b7d1b752d6cf)

Com base no gráfico 'Volume de Vendas por Categoria de Produto' verifica-se que as categorias vestuário (225.322) e livros (223.876) foram as mais vendidas.

### Qual produto tem o melhor e o pior NPS?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/adc46d95-1bce-4f4c-8612-4aca042fab5d)

Com base no gráfico 'NPS médio por categoria de produto', em média, a categoria doméstica tem ligeiramente o melhor fator de satisfação do cliente (NPS). 
Portanto, não podemos concluir qual categoria de produto possui o melhor NPS apenas pela média.

## Outras análises

### Qual é o produto mais vendido e menos vendido por origem?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/7723d71a-bc60-4748-a844-6c99514a18b2)

Com base no gráfico 'Volume de vendas por origem', os canais com melhor desempenho foram Instagram Campaign (210.473 unidades vendidas)
e Organic Search (138.999 unidades vendidas), enquanto o canal com pior desempenho foi Organic Search.

### Quantos produtos foram vendidos por gênero?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/b221b8af-0ef6-41d1-8c39-607fab99dae8)

### Teste t independente de duas amostras para receita com base no gênero

- Hipótese nula: Não há associação entre gênero e quantidade.

- Hipótese alternativa: Existe uma associação entre gênero e quantidade.

```
T-statistic: [1.14845231]
P-value: [0.25078299]
There is no statistically significant difference between genders.
```

Com base no gráfico 'Volume de Vendas por Gênero', a quantidade de produto vendido por gênero é quase a mesma. O 'Teste t independente 
de duas amostras para receitas com base no gênero' confirma que não há associação de quantidade por gênero.

### Quantos produtos foram vendidos por categoria de produto e faixa etária?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/43a3f391-004b-436d-a170-7a4dcdbdaa26)

Com base no gráfico 'Vendas por categoria de produto e faixa etária', a quantidade de produto vendido por categoria de produto e gênero é 
maior entre aqueles entre 18 e 29 anos, relativamente semelhante nas faixas etárias de 30 a 69 anos e diminui significativamente na
faixa etária com mais de 70 anos.

### Quantos produtos foram vendidos por origem e faixa etária?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/1721e163-0858-4478-91df-2a96fe38bba0)

Com base no gráfico 'Vendas por origem e faixa etária', a quantidade de produto vendido por origem e gênero é maior entre aqueles entre 18 e 29 anos, 
relativamente semelhante nos grupos etários dos 30 aos 69 anos e diminui significativamente no grupo etário com mais de 70 anos.

### Quantos produtos foram vendidos por origem e categoria de produto?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/b517cbcf-0af0-4561-89d7-9d86ddaaeab8)

Com base no gráfico 'Vendas por origem e categoria de produto', a quantidade de produto vendido por origem e categoria de produto é relativamente 
semelhante para a categoria de roupas e livros e para casa e eletrônicos em todas as fontes.

### Quanta receita foi gerada por fonte e categoria de produto?

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/f5c560c4-422d-4010-b1cf-c66718acd95e)

Com base no gráfico 'Receita por origem e categoria de produto', a receita por origem e categoria de produto é relativamente semelhante para roupas
e categoria de livros e para casa e eletrônicos em todas as fontes.

### Teste qui-quadrado para receita com base na origem e na categoria do produto

- Hipótese nula: Não há associação entre categoria de produto e origem.

- Hipótese alternativa: Existe associação entre categoria de produto e origem.

```
Chi-squared statistic: 13.825465648217591
P-value: 0.12867060967583924
There is no statistically significant association between product category and source.
```

O Teste de Independência Qui-Quadrado mostra que não há associação estatisticamente significativa entre a categoria do produto e a fonte de receita.


### Análise de Box-plot de idade por categoria de produto e fonte

![image](https://github.com/mathewsrc/matheus-ribeiro-cerqueira/assets/94936606/54f8b55e-f743-48e9-b16c-5ab753b71c0c)

A análise do box plot revela uma média de idades semelhante em todas as combinações de categoria de produto e fonte para ambos os sexos. Esta consistência sugere
que a idade pode não ser um fator de diferenciação significativo no comportamento do consumidor em várias categorias e fontes de produtos para ambos os gêneros.

### Teste ANOVA bidirecional para receita com base na categoria e origem do produto

```
Two-way ANOVA results for Revenue based on Product Category and Source:
                                     sum_sq        df         F    PR(>F)
C(product_category)            1.142100e+06       3.0  1.087692  0.352817
C(source)                      1.897568e+06       3.0  1.807171  0.143412
C(product_category):C(source)  4.477103e+06       9.0  1.421273  0.172279
Residual                       8.749621e+10  249984.0       NaN       NaN
```

Com base nos resultados do teste ANOVA bidirecional para o efeito da categoria do produto e da fonte na receita:

O valor p é 0,352817, que é maior que o nível de significância de 0,05. Isto sugere que o efeito principal da 'Categoria de Produto' não é estatisticamente
significativo sobre a 'Receita'.

O valor p associado a 'Fonte' é 0,143412, que é maior que 0,05. Assim, o efeito principal da ´Fonte` não é estatisticamente significativo sobre a 'Receita'.

O valor p para o efeito de interação é 0,172279, que é maior que 0,05. Assim, o efeito da interação entre 'Categoria de Produto' e 'Fonte' 
não é estatisticamente significativo na 'Receita'.


### Conclusão

- Em média a categoria casa apresenta ligeiramente o melhor fator de satisfação do cliente (NPS). Portanto, não podemos concluir qual categoria de
  produto possui o melhor NPS apenas pela média.
- Alguns gráficos mostram que o volume de produtos vendidos (quantidade) são muito semelhantes quando agrupamos a quantidade de vendas por gênero.
- Mesmo que a fonte com melhor desempenho tenha sido o Instagram para ambos os sexos, não há associação estatisticamente significativa entre sexo e fonte.
- Em termos de categoria de produto, as categorias de vestuário e livros tiveram o melhor desempenho para ambos os sexos, mas não há associação
  estatisticamente significativa entre o gênero e a categoria de produto.
- A análise da origem e da faixa etária mostra que temos um volume maior entre aqueles entre 18 e 29 anos, relativamente semelhante nas faixas
  etárias de 30 a 69 anos e uma diminuição significativa na faixa etária de 70+ anos tanto para receita quanto para quantidade de produto vendido.
- O Teste de Independência Qui-Quadrado confirmou que existe uma associação estatisticamente significativa entre fonte e faixa etária para receita,
  mas não para categoria de produto e faixa etária.
- A análise do produto vendido (quantidade) e receita por fonte e categoria de produto revela que Instagram e SEM foram as fontes com melhor desempenho,
  mas o Teste de Independência Qui-Quadrado elucida que não há associação estatisticamente significativa entre categoria de produto e fonte de receita .
- Com base na análise do box-plot para ambos os gêneros, podemos concluir que a idade pode não ser um fator de diferenciação significativo no
  comportamento do consumidor em várias categorias e fontes de produtos.
- Também podemos concluir, com base na ANOVA bidirecional, que tanto a categoria do produto quanto a fonte não foram estatisticamente significativas na receita.
- Portanto, assumindo as limitações do conjunto de dados e das informações que temos sobre os clientes, devemos tentar encontrar novas
  características que possam revelar o comportamento do nosso cliente e, assim, tomar melhores decisões sobre a recomendação de fontes e
  categorias de produtos com base no sexo e faixa etária dos clientes.
