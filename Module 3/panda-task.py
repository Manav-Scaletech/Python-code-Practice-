import pandas as pd

# 1. Create local data (No internet required!)
data = {
    'name': ['Mumbai', 'Delhi', 'Bangalore', 'Ahmedabad', 'New York', 'Los Angeles', 'Chicago'],
    'country': ['India', 'India', 'India', 'India', 'United States', 'United States', 'United States'],
    'subcountry': ['Maharashtra', 'Delhi', 'Karnataka', 'Gujarat', 'New York', 'California', 'Illinois'],
    'population': [12442373, 11034555, 8443675, 5577940, 8175133, 3792621, 2695598]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

print("--- 1. Dataset Loaded Successfully (Offline) ---")
print(f"Total rows in dataset: {len(df)}\n")


# 2. View the first 5 rows
print("--- 2. First 5 Rows ---")
print(df.head())
print("\n")


# 3. Filter Data: Find all cities located in 'India'
print("--- 3. Filtering Cities in India ---")
india_cities = df[df['country'] == 'India']
print(india_cities[['name', 'subcountry', 'population']])
print("\n")


# 4. Value Counts: See which countries have the most cities listed
print("--- 4. City Count by Country ---")
top_countries = df['country'].value_counts()
print(top_countries)
print("\n")


# 5. Aggregation: Find the highest population in India
print("--- 5. Max Population in India ---")
max_pop = india_cities['population'].max()
print(f"The largest city population is: {max_pop:,}")
