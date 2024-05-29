import pandas as pd
import matplotlib.pyplot as plt

class Analyzer():
    def __init__(self, file_path: str) -> None:
        '''Lê o arquivo e higieniza os dados'''
        
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)
        ignore = ['Customer ID', 'Total Purchase Amount', 'Latitude', 'Longituide', 'Country', 'State']
        self.df.drop(columns=ignore, inplace=True)
        self.df.dropna(inplace=True)
    
    def plot_total_sales_by_source(self, category: str) -> None:
        '''Constrói um gráfico da quantidade de vendas por canal'''
        
        df_category = self.df[self.df['Product Category'] == category]
    
        source_sales = df_category['Source'].value_counts()
        plt.figure(figsize=(10, 6))
        ax = source_sales.plot(kind='bar')
        plt.title(f'Vendas de {category} por canais')
        plt.xlabel('Canal')
        plt.ylabel('Número de Vendas')
        for i in ax.patches:
            ax.annotate(str(i.get_height()), (i.get_x() + i.get_width() / 2, i.get_height()), 
                        ha='center', va='bottom')
        plt.tight_layout()
        plt.show()
        
    def plot_sales_by_gender(self, category: str) -> None:
        '''Constrói um gráfico da porcentagem de vendas por gênero'''
        
        df_category = self.df[self.df['Product Category'] == category]
        
        gender_counts = df_category['Gender'].value_counts()
        gender_percentages = gender_counts / gender_counts.sum() * 100

        plt.figure(figsize=(10, 6))
        ax = gender_percentages.plot(kind='bar')
        plt.title(f'Porcentagem de Vendas de {category} por gênero')
        plt.xlabel('Gênero')
        plt.ylabel('Porcentagem de Vendas')

        for i in ax.patches:
            ax.annotate(f'{i.get_height():.2f}%', (i.get_x() + i.get_width() / 2, i.get_height()), 
                        ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

    def plot_sales_by_age(self, category: str) -> None:
        '''Constrói um gráfico da quantidade de vendas por faixa etária'''
        
        df_category = self.df[self.df['Product Category'] == category]
        
        ages = [0, 18, 25, 35, 45, 55, 65, 100]
        labels = ['0-18', '19-25', '26-35', '36-45', '46-55', '56-65', '65+']
        df_category['Age Group'] = pd.cut(df_category['Customer Age '], bins=ages, labels=labels, right=False)

        age_group_sales = df_category['Age Group'].value_counts().sort_index()

        plt.figure(figsize=(10, 6))
        ax = age_group_sales.plot(kind='bar')
        plt.title(f'Vendas de {category} por faixa etária')
        plt.xlabel('Faixa Etária')
        plt.ylabel('Número de Vendas')

        for i in ax.patches:
            ax.annotate(str(i.get_height()), (i.get_x() + i.get_width() / 2, i.get_height()), 
                        ha='center', va='bottom')

        plt.tight_layout()
        plt.show()
        
    def plot_highest_and_lowest_price_by_source(self) -> None:
        '''Constrói um gráfico com o valor do produto mais caro e barato por categoria'''
        category_prices = self.df.groupby('Product Category')['Product Price'].agg(['min', 'max'])

        fig, ax = plt.subplots(figsize=(14, 8))

        colors = ['#1f77b4', '#ff7f0e']
        bar_width = 0.4
        index = range(len(category_prices))
        bars1 = ax.bar([i - bar_width / 2 for i in index], category_prices['min'], bar_width, color=colors[0], label='Produto mais barato')
        bars2 = ax.bar([i + bar_width / 2 for i in index], category_prices['max'], bar_width, color=colors[1], label='Produto mais caro')
        for bar in bars1:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12, color=colors[0])

        for bar in bars2:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12, color=colors[1])

        plt.title('Valor do produto mais caro e mais barato por categoria', fontsize=16)
        ax.set_xlabel('Categoria do Produto', fontsize=14)
        ax.set_ylabel('Valor do Produto', fontsize=14)
        ax.set_xticks(index)
        ax.set_xticklabels(category_prices.index, rotation=45, ha='right', fontsize=12)
        ax.legend()

        plt.tight_layout()
        plt.show()

    def plot_total_sales_by_category(self):
        '''Constrói um gráfico da quantidade de produtos vendidos por categoria'''
        colors = plt.cm.tab20.colors
        category_counts = self.df.groupby('Product Category')['Quantity'].sum()

        fig, ax = plt.subplots(figsize=(14, 8))
        bars = ax.bar(category_counts.index, category_counts, color=colors[:len(category_counts)]) ##2ca02c

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12, color='black')

        plt.title('Quantidade de produtos vendidos por Categoria', fontsize=16)
        ax.set_xlabel('Categoria do produto', fontsize=14)
        ax.set_ylabel('Quantidade vendida', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)

        plt.tight_layout()
        plt.show()

    def plot_mean_price_by_category(self):
        '''Constrói um gráfico com o preço médio dos produtos por categoria'''
        category_avg_price = self.df.groupby('Product Category')['Product Price'].mean()
        fig, ax = plt.subplots(figsize=(14, 8))
        colors = plt.cm.tab20.colors
        bars = ax.bar(category_avg_price.index, category_avg_price, color=colors[:len(category_avg_price)])
        
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12)

        plt.title('Preço médio dos produtos por categoria', fontsize=16)
        ax.set_xlabel('Categoria do produto', fontsize=14)
        ax.set_ylabel('Preço médio', fontsize=14)
        ax.set_xticklabels(category_avg_price.index, rotation=45, ha='right', fontsize=12)

        plt.tight_layout()
        plt.show()
        
    def plot_highest_and_lowest_NPS_by_category(self):
        '''Constrói um gráfico com o maior e menor NPS por categoria'''
        category_nps = self.df.groupby('Product Category')['NPS'].agg(['min', 'max'])
        fig, ax = plt.subplots(figsize=(14, 8))
        colors = ['#1f77b4', '#ff7f0e'] 
        bar_width = 0.4
        spacing = 0.2 
        index = list(range(len(category_nps)))
        positions_min = [i - bar_width / 2 for i in index]
        positions_max = [i + bar_width / 2 for i in index]
        bars_min = ax.bar(positions_min, category_nps['min'], width=bar_width, color=colors[0], label='Menor NPS')
        bars_max = ax.bar(positions_max, category_nps['max'], width=bar_width, color=colors[1], label='Maior NPS')

        for bar in bars_min:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3), 
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12)
        for bar in bars_max:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}', 
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=12)

        plt.title('Maior e menor NPS por categoria de produto', fontsize=16)
        ax.set_xlabel('Categoria do produto', fontsize=14)
        ax.set_ylabel('NPS', fontsize=14)
        ax.set_xticks(index)
        ax.set_xticklabels(category_nps.index, rotation=45, ha='right', fontsize=12)
        ax.legend()
        plt.tight_layout()
        plt.show()

    def plot_mean_NPS_by_category(self):
        '''Constrói um gráfico com o NPS médio por categoria'''
        category_nps_mean = self.df.groupby('Product Category')['NPS'].mean()

        plt.figure(figsize=(12, 6))
        colors = plt.cm.tab10.colors
        
        bars = category_nps_mean.plot(kind='bar', color=colors)
        for bar in bars.patches:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', 
             ha='center', va='bottom', fontsize=10, color='black')
    
        plt.title('NPS médio por categoria de produto', fontsize=16)
        plt.xlabel('Categoria do produto', fontsize=14)
        plt.ylabel('NPS médio', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)

        plt.tight_layout()
        plt.show()
        
    def plot_last_three_years_sales_by_category(self):
        '''Constrói um gráfico com o total de vendas nos últimos 3 anos por categoria'''
        self.df['Purchase Date'] = pd.to_datetime(self.df['Purchase Date'])

        last_3_years = self.df[self.df['Purchase Date'] >= self.df['Purchase Date'].max() - pd.DateOffset(years=3)]

        category_counts = last_3_years.groupby('Product Category')['Quantity'].sum()
        plt.figure(figsize=(12, 6))
        bars = category_counts.plot(kind='bar', color='skyblue')
        for bar in bars.patches:
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height()}', 
                    ha='center', va='bottom', fontsize=10)

        plt.title('Vendas de produtos por categoria nos últimos 3 anos', fontsize=16)
        plt.xlabel('Categoria do produto', fontsize=14)
        plt.ylabel('Quantidade vendida', fontsize=14)
        plt.xticks(rotation=45, ha='right', fontsize=12)

        plt.tight_layout()
        plt.show()

an = Analyzer(file_path="Ecommerce_DBS.csv")

an.analyze_prices()