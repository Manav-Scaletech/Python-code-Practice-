import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS COMPLETE DEMO")
print("=" * 60)

# ------------------------------------------------------------------
# Create DataFrame
# ------------------------------------------------------------------
data = {
    "ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [24, 30, 28, np.nan, 35],
    "City": ["New York", "London", "Paris", "London", "Paris"],
    "Salary": [50000, 60000, 70000, 80000, np.nan]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame")
print(df)

# ------------------------------------------------------------------
# Basic Information
# ------------------------------------------------------------------
print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nIndex")
print(df.index)

print("\nData Types")
print(df.dtypes)

print("\nInformation")
print(df.info())

print("\nStatistics")
print(df.describe())

# ------------------------------------------------------------------
# Selecting Data
# ------------------------------------------------------------------
print("\nSingle Column")
print(df["Name"])

print("\nMultiple Columns")
print(df[["Name", "Salary"]])

print("\nFirst Row using iloc")
print(df.iloc[0])

print("\nRows 1 to 3")
print(df.iloc[1:4])

print("\nUsing loc")
print(df.loc[2])

# ------------------------------------------------------------------
# Filtering
# ------------------------------------------------------------------
print("\nAge > 25")
print(df[df["Age"] > 25])

print("\nCity == London")
print(df[df["City"] == "London"])

print("\nSalary > 60000")
print(df[df["Salary"] > 60000])

# ------------------------------------------------------------------
# Sorting
# ------------------------------------------------------------------
print("\nSort by Age")
print(df.sort_values("Age"))

print("\nSort by Salary Descending")
print(df.sort_values("Salary", ascending=False))

# ------------------------------------------------------------------
# Missing Values
# ------------------------------------------------------------------
print("\nMissing Values")
print(df.isnull())

print("\nMissing Count")
print(df.isnull().sum())

print("\nFill Missing Values")
filled = df.fillna(0)
print(filled)

print("\nDrop Missing Values")
print(df.dropna())

# ------------------------------------------------------------------
# Add Column
# ------------------------------------------------------------------
df["Bonus"] = 5000

print("\nAfter Adding Bonus")
print(df)

# ------------------------------------------------------------------
# Update Column
# ------------------------------------------------------------------
df["Salary"] = df["Salary"].fillna(50000)

print("\nUpdated Salary")
print(df)

# ------------------------------------------------------------------
# Delete Column
# ------------------------------------------------------------------
temp = df.drop("Bonus", axis=1)

print("\nAfter Removing Bonus")
print(temp)

# ------------------------------------------------------------------
# Rename Column
# ------------------------------------------------------------------
renamed = df.rename(columns={"Salary": "Monthly Salary"})

print("\nRenamed Column")
print(renamed)

# ------------------------------------------------------------------
# Unique Values
# ------------------------------------------------------------------
print("\nUnique Cities")
print(df["City"].unique())

print("\nNumber of Unique Cities")
print(df["City"].nunique())

print("\nValue Counts")
print(df["City"].value_counts())

# ------------------------------------------------------------------
# Mathematical Operations
# ------------------------------------------------------------------
print("\nAverage Salary")
print(df["Salary"].mean())

print("\nMaximum Salary")
print(df["Salary"].max())

print("\nMinimum Salary")
print(df["Salary"].min())

print("\nTotal Salary")
print(df["Salary"].sum())

print("\nMedian Salary")
print(df["Salary"].median())

# ------------------------------------------------------------------
# Group By
# ------------------------------------------------------------------
print("\nGroup By City")
print(df.groupby("City")["Salary"].mean())

# ------------------------------------------------------------------
# Apply Function
# ------------------------------------------------------------------
df["Age + 5"] = df["Age"].apply(lambda x: x + 5 if pd.notnull(x) else x)

print("\nUsing Apply")
print(df)

# ------------------------------------------------------------------
# Insert Column
# ------------------------------------------------------------------
df.insert(1, "Country", ["USA", "UK", "France", "UK", "France"])

print("\nAfter Insert")
print(df)

# ------------------------------------------------------------------
# Duplicate Rows
# ------------------------------------------------------------------
print("\nDuplicate Rows")
print(df.duplicated())

# ------------------------------------------------------------------
# Drop Duplicates
# ------------------------------------------------------------------
print("\nDrop Duplicates")
print(df.drop_duplicates())

# ------------------------------------------------------------------
# Sample
# ------------------------------------------------------------------
print("\nRandom Sample")
print(df.sample(2))

# ------------------------------------------------------------------
# Copy
# ------------------------------------------------------------------
copy_df = df.copy()

print("\nCopied DataFrame")
print(copy_df)

# ------------------------------------------------------------------
# Merge
# ------------------------------------------------------------------
department = pd.DataFrame({
    "ID": [101, 102, 103, 104, 105],
    "Department": ["HR", "IT", "Finance", "Sales", "Marketing"]
})

merged = pd.merge(df, department, on="ID")

print("\nMerged DataFrame")
print(merged)

# ------------------------------------------------------------------
# Concatenate
# ------------------------------------------------------------------
extra = pd.DataFrame({
    "ID": [106],
    "Country": ["India"],
    "Name": ["John"],
    "Age": [27],
    "City": ["Delhi"],
    "Salary": [55000],
    "Bonus": [5000],
    "Age + 5": [32]
})

combined = pd.concat([df, extra], ignore_index=True)

print("\nConcatenated DataFrame")
print(combined)

# ------------------------------------------------------------------
# Export Files
# ------------------------------------------------------------------
combined.to_csv("employees.csv", index=False)
combined.to_excel("employees.xlsx", index=False)

print("\nCSV and Excel files created.")

# ------------------------------------------------------------------
# Reading Files
# ------------------------------------------------------------------
csv_data = pd.read_csv("employees.csv")
excel_data = pd.read_excel("employees.xlsx")

print("\nRead CSV")
print(csv_data.head())

print("\nRead Excel")
print(excel_data.head())

# ------------------------------------------------------------------
# Convert to Dictionary
# ------------------------------------------------------------------
print("\nDictionary")
print(df.to_dict())

# ------------------------------------------------------------------
# Convert to List
# ------------------------------------------------------------------
print("\nList")
print(df.values.tolist())

# ------------------------------------------------------------------
# Transpose
# ------------------------------------------------------------------
print("\nTranspose")
print(df.T)

# ------------------------------------------------------------------
# DataFrame Size
# ------------------------------------------------------------------
print("\nSize")
print(df.size)

# ------------------------------------------------------------------
# Memory Usage
# ------------------------------------------------------------------
print("\nMemory Usage")
print(df.memory_usage())

print("\nFinished Pandas Demonstration Successfully!")