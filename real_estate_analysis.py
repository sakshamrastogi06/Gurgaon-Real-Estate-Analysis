import pandas as pd

# Load Dataset
df = pd.read_csv("data of gurugram real Estate.csv")

# First 5 Rows
print(df.head())

# Dataset Shape
print("\nDataset Shape:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate Rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# Convert Numeric Columns
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Area"] = pd.to_numeric(df["Area"], errors="coerce")

df["Rate per sqft"] = (
    df["Rate per sqft"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Rate per sqft"] = pd.to_numeric(
    df["Rate per sqft"],
    errors="coerce"
)

# Remove invalid rows
df = df.dropna(subset=["Price", "Area", "Rate per sqft"])

print("\nDataset Shape After Numeric Conversion:")
print(df.shape)

# Question 1
print("\nMost Expensive Property:")
print(df.loc[df["Price"].idxmax()])

# Question 2
print("\nTop 10 Localities by Average Price:")
avg_price_locality = (
    df.groupby("Locality")["Price"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_price_locality.head(10))

# Question 3
print("\nTop 10 Localities by Rate Per Sqft:")

rate_locality = (
    df.groupby("Locality")["Rate per sqft"]
    .mean()
    .sort_values(ascending=False)
)

print(rate_locality.head(10))

# Question 4

print("\nReady To Move vs Under Construction:")

status_price = df.groupby("Status")["Price"].mean()

print(status_price)

# Question 5

print("\nRERA Approval Impact:")

rera_price = df.groupby("RERA Approval")["Price"].mean()

print(rera_price)

# Question 6

import matplotlib.pyplot as plt

print("\nCreating Area vs Price Graph...")

plt.figure(figsize=(10,6))

plt.scatter(df["Area"], df["Price"])

plt.title("Area vs Price")

plt.xlabel("Area (sqft)")

plt.ylabel("Price")

#plt.show()

# Question 7

print("\nAverage Price by BHK:")

bhk_price = df.groupby("BHK_Count")["Price"].mean().sort_values(ascending=False)

print(bhk_price)

# Question 8

print("\nAverage Price by Property Type:")

property_type_price = df.groupby("Flat Type")["Price"].mean().sort_values(ascending=False)

print(property_type_price)

# Question 9

print("\nTop 10 Builders / Companies by Average Price:")

builder_price = df.groupby("Company Name")["Price"].mean().sort_values(ascending=False)

print(builder_price.head(10))

# Question 10

print("\nTop 10 Areas with Maximum Properties:")

top_localities = df["Locality"].value_counts()

print(top_localities.head(10))