"""
Анализ лояльности пользователей к 1 бренду
"""

import pandas as pd

df = pd.read_csv("analytic_example_2.csv")
user_df = df[['Дата оплаты', 'Наименование товара, услуги']]
user_df = user_df.rename(columns={'Дата оплаты': 'user_id',
                                  'Наименование товара, услуги': 'brand_info'
                                  })

user_df["brand_name"] = user_df.brand_info.apply(lambda x: x.split(' ')[-1])
user_df["user_id"] = user_df.user_id.apply(lambda x: x.split('/')[1])

# пользователи совершают покупки _ users_purchases
# Общее число покупок для пользователей у которых число покупок больше 33
users_purchases = user_df \
    .groupby('user_id', as_index=False) \
    .agg({'brand_name': 'count'}) \
    .rename(columns={'brand_name': 'purchases'}) \
    # .query('purchases > 33')  # сначала считаем .describe() без .query и берём 75% = 33.5 и
# подставляем purchases > 33

print(users_purchases, '\n')
# print(users_purchases.purchases.describe())

# Уникальные бренды пользователей - users_unique_brands
# Сколько уникальных брендов купил каждый пользователь
users_unique_brands = user_df \
    .groupby('user_id', as_index=False) \
    .agg({'brand_name': pd.Series.nunique}) \
    .rename(columns={'brand_name': 'unique_brands_name'})
print(users_unique_brands, '\n')

# Покупки любимого бренда - favorite_brand_purchases
# Пользователи совершившие максимальное количество покупок одного бреда (это и есть любимый бренд)
favorite_brand_purchases_df = user_df \
    .groupby(['user_id', 'brand_name'], as_index=False) \
    .agg({'brand_info': 'count'}) \
    .sort_values(['user_id', 'brand_info'], ascending=[False, False]) \
    .groupby('user_id') \
    .head(1) \
    .rename(columns={'brand_name': 'favorite_brand_name', 'brand_info': 'favorite_brand_purchases'})
print(favorite_brand_purchases_df, '\n')
