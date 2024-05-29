# Apresentação do projeto
As seguintes análises foram feitas pelo script `main.py`, no qual utilizei a biblioteca `pandas` para ler e tratar os dados do banco de dados e a biblioteca `matplotlib` para gerar os gráficos com base nos dados tratados.

# Roteiro de análise
1. Quais os produtos mais vendidos considerando os últimos 3 anos?
2. Qual o produto mais caro e o mais barato?
4. Qual a categoria de produto mais vendida e menos vendida? Qual a categoria mais e menos cara?
5. Qual o produto com melhor e pior NPS?

- ## Quais os produtos mais vendidos considerando os últimos 3 anos?
  Os produtos mais vendidos nos últimos 3 anos foram as roupas, totalizando 168593 vendas. Logo em seguida temos: livros, com 166998 vendas; produtos eletrônicos, com 112091 vendas; produtos para casa, com 111223 vendas.

  ![vendas_por_categoria_ultimos_3_anos](https://github.com/docafavarato/itau-dados/assets/98183878/2c415eff-9e12-4e11-95ce-89b704933c98)
  *Vendas por categoria nos últimos 3 anos*

- ## Qual o produto mais caro e o mais barato?
  Todas as categorias possuem um valor mínimo de 10 e um valor máximo de 500.
  
  ![maiscaroemaisbarato](https://github.com/docafavarato/itau-dados/assets/98183878/6ccb294e-dc7e-49dc-adc1-27960a434fde)
  *Valor mais alto e mais baixo para cada categoria*
  
- ## Qual a categoria de produto mais vendida e menos vendida? Qual a categoria mais e menos cara?
  A categoria de produto mais vendida é a de roupas, com um total de 225322 vendas. A menos vendida é a de produtos para casa, com 149698 vendas.

  ![qtd_produtos_vendidos_por_categoria](https://github.com/docafavarato/itau-dados/assets/98183878/6b51b6c6-0b75-43fc-bc4a-a244acaacc4c)
  *Quantidade de produtos vendidos em cada categoria*

  A categoria mais cara é a de produtos para casa, com um preço médio de 254.84. A mais barata é a de roupas, com um preço médio de 254.45.

  ![preco_medio_por_categoria](https://github.com/docafavarato/itau-dados/assets/98183878/2746c4d3-aca9-495c-a1ad-a3498745ddb4)
  *Preço médio dos produtos vendidos em cada categoria*

- ## Qual o produto com melhor e pior NPS?
  Todas as categorias possuem produtos com o NPS máximo (10) e mínimo (0). Entretanto, a categoria com o melhor NPS médio é a de produtos para casa, com 5.01, e a pior é a de produtos eletrônicos, com 4.97.
  
  ![nps_maior_e_menor_por_categoria](https://github.com/docafavarato/itau-dados/assets/98183878/c9c318cf-867d-4393-8f67-a186a84a5cf0)
  *Maior e menor NPS por categoria*

  ![nps_medio_por_categoria](https://github.com/docafavarato/itau-dados/assets/98183878/5ee0f0bd-28e3-4d65-86de-c1692dfe3b22)
  *NPS médio por categoria*

# Análises
## Eletrônicos
### Análise de canais
Para produtos eletrônicos, o canal que mais resultou em vendas foi o "Instagram Campaign", sendo responsável por ~28% das mesmas. O "FaceBook Campaign" e o "SEM" demonstraram desempenho semelhante, sendo juntos responsáveis por ~53%. O "Organic Search" apresentou desempenho inferior, sendo responsável por ~19% das vendas.

Portanto, o canal ideal de vendas é o "Instagram Campaign".

![source_electronics](https://github.com/docafavarato/itau-dados/assets/98183878/d0ee2b19-24f5-4074-b2c9-c1855d3eb4de)
*Vendas de produtos eletrônicos por canais*

### Análise de público
As vendas de produtos eletrônicos tiveram maior concentração na faixa dos 26 aos 65 anos, sendo esta responsável por ~74% das mesmas. Não houve discrepância significativa no NPS médio e na quantidade de vendas de cada gênero, portanto, o público ideal de vendas são homens e mulheres de 26 a 65 anos.

![age_electronics](https://github.com/docafavarato/itau-dados/assets/98183878/246be1d4-c355-4019-a257-635b79ead6e6)
*Vendas de produtos eletrônicos por faixa etária*

![gender_electronics](https://github.com/docafavarato/itau-dados/assets/98183878/d8bc1484-910b-430d-8fea-6c7539bbf425)
*Vendas de produtos eletrônicos por gênero*

![nps_electronics](https://github.com/docafavarato/itau-dados/assets/98183878/7a63f2f7-7f09-48f4-a11d-b0694b1cfbbf)
*NPS médio de produtos eletrônicos por gênero*

## Livros
### Análise de canais
Para livros, o canal que mais captou vendas foi o "Instagram Campaign" (~28%), seguido pelo "SEM" (~27%), "FaceBook Campaign" (~25%) e "Organic Search" (~20%).

O canal ideal de vendas é o "Instagram Campaign".

![source](https://github.com/docafavarato/itau-dados/assets/98183878/c3a08258-ba3c-4e23-95e3-f12b334608b8)
*Vendas de livros por canais*

### Análise de público
As vendas de livros se concentraram na faixa dos 26 aos 65 anos, sendo esta responsável por ~75% das mesmas, e não havendo grande variação em suas subfaixas. Não houve grande discrepância na quantidade de vendas e no NPS médio de cada gênero, logo, o público ideal de vendas são homens e mulheres de 26 a 65 anos.

![age](https://github.com/docafavarato/itau-dados/assets/98183878/bad8f1f0-80c3-4bba-b8cc-96d2debd5f70)
*Vendas de livros por faixa etária*

![gender](https://github.com/docafavarato/itau-dados/assets/98183878/7e9def9d-0ea4-4463-bd04-635a82bd3646)
*Vendas de livros por gênero*

![nps](https://github.com/docafavarato/itau-dados/assets/98183878/abd3388b-b004-4d0e-94a4-a2fab43faf42)
*NPS médio de livros por gênero*

## Roupas
### Análise de canais
Para roupas, o canal mais eficiente também foi o "Instagram Campaign", responsável por ~27% das vendas.

![source](https://github.com/docafavarato/itau-dados/assets/98183878/44ec83f8-9bf5-46fb-b9e1-8c665ba5da45)
*Vendas de roupas por canais*

### Análise de público
As vendas de roupas foram ligeiramente maiores na faixa dos 26 aos 35 anos, exibindo valores semelhantes até a faixa dos 65 anos. A quantidade de vendas e o NPS médio de cada gênero também se mostraram próximos, portanto, o público ideal de vendas são homens e mulheres de 26 a 65 anos.

![age](https://github.com/docafavarato/itau-dados/assets/98183878/252cdf36-7c17-465e-a5bf-782ced59225b)
*Vendas de roupas por faixa etária*

![gender](https://github.com/docafavarato/itau-dados/assets/98183878/e6d4d73d-b040-4fa1-920d-a7830733af9b)
*Vendas de roupas por gênero*

![nps](https://github.com/docafavarato/itau-dados/assets/98183878/2203a370-04ea-403d-a7a0-e762c76c03a8)
*NPS médio de roupas por gênero*

## Produtos para casa
### Análise de canais
Para produtos para casas, o "Instagram Campaign" se mostrou o canal mais eficaz na captação de vendas, ocasionando em ~30% das mesmas.

![source](https://github.com/docafavarato/itau-dados/assets/98183878/033bd94c-c212-490f-a7ee-b77fde05a08d)
*Vendas de produtos para casas por canais*

### Análise de público
As vendas de produtos para casas tiveram seu ápice na faixa etária dos 26 aos 35 anos, com números próximos até a faixa dos 65 anos. A quantidade de vendas e o NPS médio pra cada gênero também foram semelhantes, então, o público ideal de vendas são homens e mulheres de 26 a 65 anos.

![age](https://github.com/docafavarato/itau-dados/assets/98183878/100acf6b-e711-4696-b5f1-1255b394aefd)
*Vendas de produtos para casas por faixa etária*

![gender](https://github.com/docafavarato/itau-dados/assets/98183878/7a7e41cf-759c-4504-907d-8ab9871d17fa)
*Vendas de produtos para casas por gênero*

![nps](https://github.com/docafavarato/itau-dados/assets/98183878/46ec2af4-a0ef-4675-b2d2-e65a81cb36aa)
*NPS médio de produtos para casas por gênero*
