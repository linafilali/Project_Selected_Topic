import pandas as pd

# Load original dataset
df = pd.read_csv("data/sales_data.csv", encoding="latin1")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Filter only 2017
df_2017 = df[df["Order Date"].dt.year == 2017]

# Save new dataset
df_2017.to_csv("sales_data_2017.csv", index=False)

print("Filtered dataset saved as sales_data_2017.csv")
print("Rows:", len(df_2017))