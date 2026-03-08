import pandas as pd
import os

print("ANALYTICS LAYER STARTED")

df = pd.read_csv("data/raw/ecommerce_raw.csv")

# total revenue
total_revenue = df["price"].sum()
pd.DataFrame({"total_revenue":[total_revenue]}).to_csv("data/serving/total_revenue.csv",index=False)

# top products
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False).head(10)
top_products.to_csv("data/serving/top_products.csv")

# revenue per category
category_revenue = df.groupby("category")["price"].sum()
category_revenue.to_csv("data/serving/category_revenue.csv")

print("ANALYTICS COMPLETED")
