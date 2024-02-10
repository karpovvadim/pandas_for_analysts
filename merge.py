from main import users_purchases, users_unique_brands, favorite_brand_purchases_df

loyalty_df = users_purchases \
    .merge(users_unique_brands, on='user_id') \
    .merge(favorite_brand_purchases_df, on='user_id')

outer_join = users_purchases \
    .merge(users_unique_brands, on='user_id', how="outer") \
    .merge(favorite_brand_purchases_df, on='user_id', how="outer")

print("inner_join\n", loyalty_df, "\n")
# print("outer_join\n", outer_join)

loyalty_users = loyalty_df[loyalty_df.unique_brands_name == 1]
print(loyalty_users)

loyalty_df['loyalty_score'] = loyalty_df.favorite_brand_purchases / loyalty_df.purchases
loyalty_df = loyalty_df.sort_values("loyalty_score", ascending=[False])
print(loyalty_df)
