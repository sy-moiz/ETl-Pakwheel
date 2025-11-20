# pakwheels_data_analysis_fixed.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick

# ================================
# LOAD JSON
# ================================
df = pd.read_json("pakwheels_10_pages.json", lines=True)
print("Initial rows:", len(df))
print(df.head(), "\n")

# ================================
# PRICE CLEANING
# ================================
def price_to_numeric(price):
    try:
        if pd.isnull(price):
            return None
        
        txt = str(price).replace("PKR", "").strip().lower()

        # Convert crore / lacs
        if "crore" in txt:
            return float(txt.replace("crore", "").strip()) * 1e7
        if "lacs" in txt:
            return float(txt.replace("lacs", "").strip()) * 1e5

        # Normal PKR like "2,500,000"
        return float(txt.replace(",", ""))
    except:
        return None

df["price"] = df["price"].apply(price_to_numeric)

# ================================
# MILEAGE CLEANING (UL BASED)
# ================================
df["mileage"] = (
    df["mileage"]
    .str.replace("km", "", regex=False)
    .str.replace(",", "", regex=False)
    .astype(float)
)

# ================================
# ENGINE CLEANING (UL BASED)
# ================================
df["engine"] = df["engine"].str.extract(r"([0-9\.]+)").astype(float)

# ================================
# YEAR CLEANING (UL BASED)
# ================================
df["year"] = pd.to_numeric(df["year"], errors="coerce")

# ================================
# REMOVE ROWS ONLY IF ESSENTIAL NUMBERS MISSING
# ================================
df = df.dropna(subset=["price", "mileage", "engine", "year"])
print("Rows after cleaning:", len(df), "\n")

# ================================
# SAVE CLEANED CSV
# ================================
df.to_csv("cleaned_car_data.csv", index=False)
print("Saved: cleaned_car_data.csv\n")

# ================================
# BASIC INFO
# ================================
print(df.info(), "\n")
print(df.describe(), "\n")

# ================================
# HISTOGRAMS
# ================================
numeric_cols = ["price", "mileage", "engine", "year"]
df[numeric_cols].hist(bins=20, figsize=(12, 8))
plt.suptitle("Distribution of Numeric Columns", fontsize=14)
plt.show()

# ================================
# PRICE VS MILEAGE SCATTER
# ================================
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="mileage", y="price")
plt.title("Price vs Mileage")
plt.xlabel("Mileage (km)")
plt.ylabel("Price (PKR)")
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
plt.show()

# ================================
# PRICE VS ENGINE SCATTER
# ================================
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="engine", y="price")
plt.title("Price vs Engine Capacity")
plt.xlabel("Engine (cc or kWh)")
plt.ylabel("Price (PKR)")
plt.gca().yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
plt.show()

# ================================
# YEAR DISTRIBUTION
# ================================
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="year", palette="viridis")
plt.title("Number of Cars by Year")
plt.xticks(rotation=45)
plt.show()

# ================================
# TOP 10 BRANDS
# ================================
df["brand"] = df["title"].str.split().str[0]
top_brands = df["brand"].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_brands.index, y=top_brands.values, palette="magma")
plt.title("Top 10 Car Brands on PakWheels")
plt.ylabel("Count")
plt.show()

# ================================
# CORRELATION HEATMAP
# ================================
plt.figure(figsize=(8, 6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Between Numeric Features")
plt.show()
