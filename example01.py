import pandas as pd


def read_n_agg(path):
    df = pd.read_csv(path, sep=';')
    print("dtypes:\n",df.dtypes, '\n\nshape:\n', df.shape, '\ncolumns:', df.columns, '\n\ndf.head():\n', df.head(), "\n")
    df['name_company'] = df.company

    # считает средний заработок (income) по каждой компании (company)
    pg_agg = df \
        .groupby('name_company', as_index=False) \
        .agg({'company': 'count', 'income': 'mean'})

    # считает средний заработок (income) по компаниям > 1 (company),
    pg_agg_2 = df \
        .groupby('name_company', as_index=False) \
        .agg({'company': 'count', 'income': 'mean'}) \
        .query('company > 1') \
        .sort_values("income", ascending=False)

    # запрос по компаниям > 1 ("ГК Мега-Авто","Международный центр", "Шубин Инк")
    pg_GK = df.query('company == ["ГК Мега-Авто","Международный центр", "Шубин Инк"]')

    print(pg_agg.head(), '\n\n', pg_agg_2, '\n\n', pg_GK)
    return


read_n_agg("companies.csv")
