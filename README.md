# ANÁLISE EXPLORATÓRIA DOS DADOS

## Referente à vaga de Estágio em Dados - ITAÚ

. **Nome:** Gabriel Ribeiro dos Santos

. **CPF:** 538.719.308 - 65

Este README detalha a análise exploratória realizada nos dados de um e-commerce para o processo seletivo de estágio em dados no Itaú. A análise cobre diversos aspectos dos dados, respondendo a perguntas específicas sobre vendas, categorias de produtos, fontes de tráfego e características dos clientes.

### PERGUNTAS PARA ANÁLISE
#### 1. QUAIS PRODUTOS MAIS VENDIDOS CONSIDERANDO OS ÚLTIMOS 3 ANOS?

**Nos últimos três anos, os produtos mais vendidos foram:**

1. **Clothing** com 139438 vendas (cerca de 30%)

2. **Books** com 138448 vendas (cerca de 29%) 

3. **Eletronics** com 92389 vendas (20%)

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/42607248-02d6-4de6-a910-6ea85eea9719)

#### 2. QUAL O PRODUTO MAIS CARO E O MAIS BARATO?

Analisando a faixa de preços dos produtos disponíveis foi possível notar que todas categorias de produtos possuem um **valor mínimo de 10** e um **valor máximo de 500.**
![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/6b971d6a-f25b-4989-9205-9b66b0831bb5)

#### 3. QUAL A CATEGORIA DE PRODUTO MAIS VENDIDA E MENOS VENDIDA? QUAL A CATEGORIA MAIS E MENOS CARA?
A categoria de produto **mais vendida é Clothing** **com uma porcentagem de vendas totais de 30.1%**. Em contrapartida, a categoria **menos vendida é Home com uma porcentagem de vendas totais de 20%**, o que pode indicar uma necessidade de revisão de estratégias nesta categoria.
![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/91eb0eaf-fba2-43da-a164-be65c2e3042d)

Em termos de preços, **a categoria mais cara é Home, com um preço médio de 254.84, A categoria menos cara é Clothing, com um preço médio de 254.44.**
![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/bc037351-f37f-4ede-ad49-52d98e556d33)

#### 4. QUAL O PRODUTO COM MELHOR E PIOR NPS?
**Todas** categorias possuem produtos com **NPS mínimo de 0 e máximo de 10**
![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/dcd3512e-c264-44da-b048-91c5560f3fcd)

O produto com o **melhor NPS** (Net Promoter Score) **médio é Home**, indicando um alto nível de satisfação. Por outro lado, o produto com o **pior NPS é Eletronics**, sugerindo que há áreas que necessitam de melhorias para atender melhor às expectativas dos clientes.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/a3a897bd-e4a9-4c1f-b951-b77dcfec9e03)

## PERGUNTA NORTEADORA PARA DEMAIS ANÁLISES FEITAS
### **Analisando a base de dados, qual o tipo de público (considerando gênero e idade) e o canal ideal para vender determinado tipo de produto?**
## ANÁLISE DETALHADA DE CADA PRODUTO
### ELETRONICS
#### RELAÇÃO DE ELETRONICS E SOURCE

Para produtos eletrônicos, o canal que **mais resultou em vendas foi** o **Instagram Campign**, sendo responsável por aproximadamente **28%** das vendas. Os canais **SEM** e **FaceBook campaign** demonstraram desempenhos semelhantes, sendo juntos responsáveis por aproximadamente **52%**. O canal **Organic Search** apresentou desempenho inferior, sendo responsável por cerca de **18%** das vendas.

Portanto, o canal ideal de vendas para produtos eletrônicos é o **Instagram Campign**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/851546b0-5513-46df-8521-49e619256b68)


#### RELAÇÃO DE ELETRONICS E CUSTOMER AGE

Ao analisar as vendas de produtos eletrônicos por faixa etária, observamos que a maior parte das vendas ocorreu entre os clientes com idades entre **18 - 23**, representando cerca de **10%** do total de vendas. As faixas etárias **23-27** e **38-42** também demonstraram um volume significativo de vendas, juntas contribuindo com aproximadamente 18%. Em contraste, a faixa etária **68-72** teve a menor participação, correspondendo a **5%** das vendas.

Assim, a faixa etária ideal para direcionar os esforços de marketing de produtos eletrônicos é a de **18 - 23**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/9809aeeb-87ca-4b43-96b0-a0447618b84d)


#### RELAÇÃO DE ELETRONICS E GENDER

Em termos de gênero, as vendas de produtos eletrônicos foram predominantemente realizadas pelo gênero **Feminino**, que representou aproximadamente **51%** do total de vendas. Gênero Masculino foi responsável por cerca de **49%** das vendas, mostrando um envolvimento pouco menor, mas ainda muito significativo.

Portanto, o público ideal para campanhas de marketing de produtos eletrônicos é composto majoritariamente pelo **Gênero Feminino**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/a6ba63b7-bfb6-4edc-b12b-8ee58bccdabc)


### HOME
#### RELAÇÃO DE HOME E SOURCE

Para produtos de casa, o canal que **mais resultou em vendas foi** o **Instagram Campign**, sendo responsável por aproximadamente **28%** das vendas. Os canais **SEM** e **FaceBook campaign** demonstraram desempenhos semelhantes, sendo juntos responsáveis por aproximadamente **52%**. O canal **Organic Search** apresentou desempenho inferior, sendo responsável por cerca de **18%** das vendas.

Portanto, o canal ideal de vendas de Prodtos de Casa é o **Instagram Campign**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/9df7944a-f7ea-4c14-8617-8cce76d1797a)

#### RELAÇÃO DE HOME E CUSTOMER AGE

Ao analisar as vendas de **produtos de casa** por faixa etária, observamos que a maior parte das vendas ocorreu entre os clientes com idades entre **18 - 23**, representando cerca de **10%** do total de vendas. As faixas etárias **23-27** e **48-52** também demonstraram um volume significativo de vendas, juntas contribuindo com aproximadamente **18%**. Em contraste, a faixa etária **68-72** teve a menor participação, correspondendo a **5%** das vendas.

Assim, a faixa etária ideal para direcionar é a de **18 - 23**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/74d02cfd-1dde-446b-8f44-839d6d760c2a)

#### RELAÇÃO DE HOME E GENDER

Em termos de gênero, as vendas de produtos para Casa foram predominantemente realizadas pelo gênero **Feminino**, que representou aproximadamente **51%** do total de vendas. Gênero Masculino foi responsável por cerca de **49%** das vendas, mostrando um envolvimento pouco menor, mas ainda muito significativo.

Portanto, o público ideal para campanhas de marketing de produtos para Casa é composto majoritariamente pelo **Gênero Feminino**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/676bf081-b411-4856-aa35-ac848ee6c9e8)

### CLOTHING
#### RELAÇÃO DE CLOTHING E SOURCE

Para Roupas, o canal que **mais resultou em vendas foi** o **Instagram Campign**, sendo responsável por aproximadamente **28%** das vendas. Os canais **SEM** e **FaceBook campaign** demonstraram desempenhos semelhantes, sendo juntos responsáveis por aproximadamente **52%**. O canal **Organic Search** apresentou desempenho inferior, sendo responsável por cerca de **18%** das vendas.

Portanto, o canal ideal de vendas de Roupas é o **Instagram Campign**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/8079023f-a574-44d1-bb45-ccea03e42db9)

#### RELAÇÃO DE CLOTHING E CUSTOMER AGE

Ao analisar as vendas de **Roupas** por faixa etária, observamos que a maior parte das vendas ocorreu entre os clientes com idades entre **18 - 23**, representando cerca de **10%** do total de vendas. As faixas etárias **23-27** e **38-42** também demonstraram um volume significativo de vendas, juntas contribuindo com aproximadamente **18%**. Em contraste, a faixa etária **68-72** teve a menor participação, correspondendo a **5%** das vendas.

Assim, a faixa etária ideal para direcionar é a de **18 - 23.**

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/a34535c2-9a9f-40b3-ba3d-d21f5a465f89)

#### RELAÇÃO DE CLOTHING E GENDER

Em termos de gênero, as vendas de Roupas foram predominantemente realizadas pelo gênero **Feminino**, que representou aproximadamente **51%** do total de vendas. Gênero Masculino foi responsável por cerca de **49%** das vendas, mostrando um envolvimento pouco menor, mas ainda muito significativo.

Portanto, o público ideal para campanhas de marketing de Roupas é composto majoritariamente pelo **Gênero Feminino**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/db2c6075-f244-467b-afa3-575b6744596d)

### BOOKS

#### RELAÇÃO DE BOOKS E SOURCE

Para Livros, o canal que **mais resultou em vendas foi** o **Instagram Campign**, sendo responsável por aproximadamente **28%** das vendas. Os canais **SEM** e **FaceBook campaign** demonstraram desempenhos semelhantes, sendo juntos responsáveis por aproximadamente **52%**. O canal **Organic Search** apresentou desempenho inferior, sendo responsável por cerca de **18%** das vendas.

Portanto, o canal ideal de vendas de Livros é o **Instagram Campign**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/e0bb727e-e59f-4b92-a973-9df3a1e0a829)

#### RELAÇÃO DE BOOKS E CUSTOMER AGE

Ao analisar as vendas de **Livros** por faixa etária, observamos que a maior parte das vendas ocorreu entre os clientes com idades entre **18 - 23**, representando cerca de **10%** do total de vendas. As faixas etárias **38-42** e **28-32** também demonstraram um volume significativo de vendas, juntas contribuindo com aproximadamente **18%**. Em contraste, a faixa etária 68-72 teve a menor participação, correspondendo a **5%** das vendas.

Assim, a faixa etária ideal para direcionar é a de **18 - 23.**

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/8ac3241b-cdda-4486-ba25-319c87ed47be)

#### RELAÇÃO DE BOOKS E GENDER

Em termos de gênero, as vendas de **Livros** foram predominantemente realizadas pelo gênero **Feminino**, que representou aproximadamente **51%** do total de vendas. Gênero Masculino foi responsável por cerca de **49%** das vendas, mostrando um envolvimento pouco menor, mas ainda muito significativo.

Portanto, o público ideal para campanhas de marketing de **Livros** é composto majoritariamente pelo **Gênero Feminino**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/b559375a-67c5-4f95-812f-e53541073978)

### ANÁLISE DAS VENDAS
#### VENDAS PELO TIPO DE FONTES

Analisando as vendas pelo tipo de fontes ou canais, é possivel notar que o canal **Instagram Campign** **lidera com cerca de 28% de vendas totais**.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/47df1cb4-dd39-46fc-9f08-c57c7cdfd7db)

#### VENDAS POR GÊNERO

Analisando as Vendas por Gênero, é observável, que o **gênero Feminino é o que obtém maior porcentagem de vendas com cerca de 51%.**

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/02f09a09-7374-4fa4-9221-48ea186a5b5c)

#### VENDAS POR FAIXA ETÁRIA

Analisando as Vendas por Faixa Etária, é observável, que a **Faixa de 18 - 23 anos é a que possui a maior porcentagem, cerca de 10%.**

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/7192fb0c-265a-4dfd-b008-d6b6f9a52e9e)

### DEMAIS ANÁLISES
#### DISTRIBUIÇÃO DE GÊNERO

Pode se observar como os Gêneros estão distribuidos na base de dados.

Notável que o gênero Feminino está em maior quantidade, porem não é uma grande diferença. 

Feminino - cerca de 50.2%

Masculino - cerca de 49.8%

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/2db3a69f-27e6-4c46-a6a9-bec7fbfd4614)


#### DISTRIBUIÇÃO DE IDADE

Neste gráfico de densidade pode se observar que a idade mais frequenteente relatada, está entre os 20 a 25 anos.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/8f4ab5ff-880c-4f4b-9de0-bb876e522d66)

#### DISTRIBUIÇÃO DE CANAIS

Na distribuiçào dos canais notável que o **Instagram Campign** é o canal mais utilizado com cerca de 28% do total.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/b22a5d86-c87b-4e80-9295-628ed79bdb93)

#### DISTRIBUIÇÃO DE PRODUTOS

A distribuição dos produtos apresentou uma diferença após sua análise, por mais que todas análises os elementyos apresentaram números bem próximos, bem balanceados, a distribuição dos produtos apresentou um empate na porcentagem de duas categorias de produtos sendo elas, **Clothing** e **Books**, ambas com 30% de distribuição total.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/3d9b9918-dbd0-40a8-8680-933136048685)

#### RELAÇÃO - GÊNERO E CATEGORIA DE PRODUTOS

Como já visulizado o gênero Feminino se mostra superior ao Masculino na análise, nesta relação não é diferente, todas as categorias de produtos possuem mais o gênero Feminino.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/6ef88c55-78f9-415a-ae42-7325f7b063c0)

#### RELAÇÃO - GÊNERO E CANAIS

Como já visulizado o gênero Feminino se mostra superior ao Masculino na análise, nesta relação não é diferente, todos os canais possuem mais o gênero Feminino. Sendo preferível então a venda para mulheres principalmente pelo Instagram Campign. 


![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/0fbb73bc-0cf5-4f7a-b249-11bbc25d56dd)

#### RELAÇÃO - IDADE E CATEGORIA DE PRODUTOS

Não há diferenças significativas na distribuição das idades pelas categorias de produtos.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/d1bc7c40-f2a8-4523-ac40-c681bbf4b1fd)

####  RELAÇÃO - IDADE E CANAIS

Não há diferença significativa na distribuição das idades pelos canais de venda.

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/55561c67-d9ec-4e66-83e0-8adefeea760b)

#### RELAÇÃO - CANAIS E CATEGORIA DE PRODUTOS

Possível notar que todas categorias de produtos performam melhor pelo canal, Intagram Campign e pior pelo canal Organic Search. 

![image](https://github.com/GabrielRibeiro5402/Gabriel-Ribeiro-dos-Santos/assets/164082848/7f93f64b-7d62-4150-bc16-f62f5192df89)


## Conclusão

**Após a análise detalhada dos dados do e-commerce, foi retirado as seguintes conclusões sobre o tipo de público ideal e o canal de venda mais eficaz para os diferentes tipos de produtos:**

### Canal de Vendas Ideal:

O canal que se destacou como o mais eficaz para todas as categorias de produtos foi o Instagram Campaign, responsável por aproximadamente 28% das vendas totais. Este canal superou outros como SEM, Facebook Campaign e Organic Search, mostrando-se a melhor opção para direcionar esforços de marketing e vendas.

### Público-alvo por Gênero:

As vendas foram predominantemente realizadas pelo gênero feminino, que representou cerca de 51% do total de vendas. O gênero masculino, embora significativo, ficou ligeiramente atrás com 49%. Portanto, campanhas de marketing focadas no público feminino tendem a ser mais eficazes.

### Público-alvo por Faixa Etária:

A faixa etária que mais se destacou foi a de 18 a 23 anos, responsável por cerca de 10% das vendas em todas as categorias de produtos. No entanto, outras faixas etárias como 23-27 e 38-42 também mostraram volumes significativos de vendas. Isso indica que, embora a faixa de 18 a 23 anos seja a mais importante, as estratégias de marketing devem ser inclusivas e abrangentes para outras idades.

### Desempenho por Categoria de Produto:

Todas as categorias de produtos (Eletronics, Home, Clothing e Books) tiveram melhor desempenho no canal Instagram Campaign e apresentaram resultados semelhantes em termos de distribuição de vendas por gênero e idade.
A categoria de Clothing foi a mais vendida, enquanto a Home teve o menor desempenho em termos de quantidade de vendas.

## Resumo

-----

A análise dos dados do e-commerce revela que o canal Instagram Campaign é o mais eficaz para alcançar o público-alvo, com o gênero feminino e a faixa etária de 18 a 23 anos sendo os segmentos mais receptivos às campanhas de marketing. Entretanto, a distribuição de vendas é relativamente uniforme entre os gêneros e levemente variada entre diferentes faixas etárias, indicando a necessidade de uma abordagem inclusiva. As estratégias de marketing devem ser amplamente focadas no Instagram Campaign e no público feminino jovem, mas sem deixar de lado outros segmentos importantes que também contribuem significativamente para as vendas.
