import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('books.csv', sep=",", on_bad_lines="skip")

# Limpa os espaços em branco de todos os nomes das colunas de uma vez
df.columns = df.columns.str.strip()

# %% PARTE 1: Visualização inicial
df.head()
df.sample(5)
df.info()

# %% PARTE 2: Limpeza e Checagem
df.isnull().sum()  # valores nulos
df.describe()  # descrição da base
df[df.duplicated()]  # checa linhas duplicadas
df[df.duplicated('isbn')]  # checa isbn duplicado
df[df.duplicated('isbn13')]  # checa isbn13 duplicado
df[df.duplicated('bookID')]  # checa bookID duplicado
# dados que possuem mais comentários do que número de reviews
df[df.ratings_count < df.text_reviews_count]
df[df.ratings_count == 0].shape  # qt. dados que não possuem reviews
df[df['num_pages'] < 30].shape  # qt. dados com número depáginas menor que 30
df[df.duplicated(["title", "language_code"], keep=False)]
df.sort_values('title')  # dados que têm título e língua duplicados

# %% PARTE 3: Resolução
df.drop(['isbn', 'isbn13', 'bookID'], axis=1, inplace=True)
df.rename(columns={' num_pages': 'num_pages'}, inplace=True)
df.drop(df[(df.ratings_count == 0) | (
    df['num_pages'] < 30)].index, inplace=True)
df.reset_index(drop=True, inplace=True)
invalid_dates = []
for idx, date_str in enumerate(df['publication_date']):
    try:
        pd.to_datetime(date_str, format='%m/%d/%Y')
    except ValueError:
        invalid_dates.append((idx, date_str))
df.drop(index=[idx for idx, _ in invalid_dates], inplace=True)
df['publication_date'] = pd.to_datetime(
    df['publication_date'], format='%m/%d/%Y')
aggregated_df = df.groupby(['title', 'language_code']).agg({
    'authors': lambda x: '/'.join(set(x)),
    'average_rating': 'mean',
    'num_pages': 'max',
    'ratings_count': 'sum',
    'text_reviews_count': 'sum',
    'publication_date': 'min',
    'publisher': lambda x: '/'.join(set(x))
}).reset_index()
df = aggregated_df

# %% PARTE 4: Análise Exploratória dos Dados

# Quais os 10 livros com mais avaliações e qual a sua média de avaliação?
most_rated = df.sort_values(
    'ratings_count', ascending=False).head(10).set_index('title')
sns.barplot(x=most_rated['ratings_count'], y=most_rated.
            index)
most_rated.describe()

# Qual a média de avaliação dos autores com mais livros?
# df com autores como uma lista
df2 = df.copy()
df2['authors'] = df2['authors'].apply(lambda x: set(x.
                                                    split('/')))
df2 = df2.explode('authors')
# Agrupando por 'authors' para contar o número de livros e calcular a média de avaliação
author_book_count = df2.groupby('authors').size().reset_index(name='num_books')
author_rating_mean = df2.groupby(
    'authors')['average_rating'].mean().reset_index()
# Juntando as duas informações em um único DataFrame
pd.merge(author_book_count, author_rating_mean,
         on='authors').sort_values('num_books', ascending=False)

# Qual a média de avaliação de livros por autor e por ano?
plt.figure(figsize=(15, 5))
plt.grid()
author_df = df[df.authors.str.contains('Stephen King', case=False, na=False)]
sns.barplot(x=author_df.publication_date.dt.year, y=author_df.average_rating)
