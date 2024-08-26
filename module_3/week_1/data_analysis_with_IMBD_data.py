import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATA_PATH = "module_3/week_1/data/IMDB-Movie-Data.csv"

# 1. Read data from IMBD data
data = pd.read_csv(DATA_PATH)

# Read data with specified explicit index
data_indexed = pd.read_csv(DATA_PATH, index_col="Title")

# 2. View data
# Preview top 5 rows using head()
top_5_rows = data.head()
print(f"==== Top 5 rows: ==== \n {top_5_rows}\n")

# 3. Understand some basic information about the data
# Let's first understand some basic information about this data using info()
print(f"==== Basic information about data: =====")
data.info()
# Statical overview from data
statical_overview = data.describe()
print(f"\n==== Statical Overview ====\n {statical_overview}")

# 4. Data selection - Indexing and Slicing data
# Extract data as series
genre_series = data['Genre']
print(f"Genre_series: \n{genre_series}")
print(f"Datatype of genre_series = {type(genre_series)}")

# Extract data as dataframe
genre_df = data[["Genre"]]
print(f"Genre_series: \n{genre_df}")
print(f"Datatype of genre_df = {type(genre_df)}")

# We can select and split multiple columns at once, creating a new DataFrame.
some_cols = data[["Title", "Genre", "Actors", "Director", "Rating"]]
print("New dataframe\n", some_cols)

# Extract rows
print(data.iloc[10:15][['Title', 'Rating', 'Revenue (Millions)']])

# 5. Data selection - Based on conditional filltering
conditonal_data = data[((data["Year"] >= 2010) & (data["Year"] <= 2015))
                       & (data["Rating"] < 6.0) & (data["Revenue (Millions)"] < data["Revenue (Millions)"].quantile(0.95))]
print(conditonal_data)

# 6. Group by operations
director_data = data.groupby('Director')[['Rating']].mean().head()
print(director_data)

# 7. Sorting operations
sort_director_data = data.groupby('Director')[['Rating']].mean().sort_values('Rating', ascending=False).head()
print(sort_director_data)

# 8. View missing value 
missing_value = data.isnull().sum()
print("Missing value: \n", missing_value)

# 9. Deal with missing value - Deleting
# Use drop function to drop columns
drop_metascore_cols = data.drop("Metascore", axis=1).head()
print(drop_metascore_cols)
# Use dropna function to drop missing rows
drop_missing_data = data.dropna()
print(drop_missing_data)

# 10. Dealing with missing values - Filling
revenue_mean = data['Revenue (Millions)'].mean()
print('The mean revenue is ', revenue_mean)
data['Revenue (Millions)'].fillna(revenue_mean, inplace=True)

# 11. Apply functions
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'
    
data['Rating_Category'] = data['Rating'].apply(rating_group)
print(data[['Title', 'Director', 'Rating', 'Rating_Category']].head(5))





