
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Headphones", "Tablet", "Monitor", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Electronics", "Accessories"],
    "Price": [60000, 30000, 1500, 25000, 8000, 1200],
    "Stock": [10, 35, 15, 60, 40, 10]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

filtered_df = df[(df["Price"] > 500) & (df["Stock"] < 50)]

print("\nProducts with Price > 500 and Stock < 50:")
print(filtered_df)

df["Restock_Needed"] = df["Stock"] < 20

print("\nDataFrame with Restock_Needed:")
print(df)

df = df.sort_values(by="Price", ascending=False)

print("\nFinal DataFrame sorted by Price:")
print(df)