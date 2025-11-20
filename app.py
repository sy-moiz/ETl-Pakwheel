import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

st.set_page_config(page_title="PakWheels Car Dashboard", layout="wide")

# ------------------------
# Load Data
# ------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_car_data.csv")
    df["brand"] = df["title"].str.split().str[0]
    return df

df = load_data()

st.title("🚗 PakWheels Car Market Dashboard")
st.write("Live Data Analysis from PakWheels Karachi (Scraped & Cleaned)")

st.markdown("---")

# ------------------------
# Filters
# ------------------------
col1, col2, col3, col4 = st.columns(4)

brand_filter = col1.selectbox("Brand", ["All"] + sorted(df["brand"].unique()))
fuel_filter = col2.selectbox("Fuel Type", ["All"] + sorted(df["fuel"].unique()))
year_filter = col3.selectbox("Year", ["All"] + sorted(df["year"].unique()))
trans_filter = col4.selectbox("Transmission", ["All"] + sorted(df["transmission"].unique()))

filtered_df = df.copy()

if brand_filter != "All":
    filtered_df = filtered_df[filtered_df["brand"] == brand_filter]

if fuel_filter != "All":
    filtered_df = filtered_df[filtered_df["fuel"] == fuel_filter]

if year_filter != "All":
    filtered_df = filtered_df[filtered_df["year"] == year_filter]

if trans_filter != "All":
    filtered_df = filtered_df[filtered_df["transmission"] == trans_filter]

st.markdown(f"### 📊 Showing {len(filtered_df)} Cars")
st.dataframe(filtered_df)

st.markdown("---")

# ------------------------
# Price Distribution
# ------------------------
st.subheader("💰 Price Distribution")

fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(filtered_df["price"], bins=30, kde=True, ax=ax)
ax.set_xlabel("Price (PKR)")
ax.set_ylabel("Count")
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
st.pyplot(fig)

# ------------------------
# Scatter Plot: Price vs Mileage
# ------------------------
st.subheader("📉 Price vs Mileage")

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x="mileage", y="price", hue="brand", ax=ax)
ax.set_ylabel("Price (PKR)")
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
st.pyplot(fig)

# ------------------------
# Scatter: Price vs Engine
# ------------------------
st.subheader("⚙️ Price vs Engine Capacity")

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x="engine", y="price", hue="fuel", ax=ax)
ax.set_ylabel("Price (PKR)")
ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
st.pyplot(fig)

# ------------------------
# Top Brands
# ------------------------
st.subheader("🏆 Top 10 Brands")

top_brands = df["brand"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_brands.index, y=top_brands.values, palette="viridis", ax=ax)
ax.set_ylabel("Number of Cars")
st.pyplot(fig)

# ------------------------
# Correlation Heatmap
# ------------------------
st.subheader("📈 Correlation Matrix")

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(df[["price", "mileage", "engine", "year"]].corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
