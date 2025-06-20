import pandas as pd

# Load the datasets you'll need for Day 3
# Make sure these CSVs are in the same directory as this script!
movies = pd.read_csv('movies.csv')
credits = pd.read_csv('credits.csv')

# Task 1: Merge datasets
print("--- Task 1: Merging datasets ---")

# Step 1: Rename the 'movie_id' column in the 'credits' DataFrame to 'id'
# This ensures both DataFrames have a common column name for merging.
credits = credits.rename(columns={'movie_id': 'id'})

# Step 2: Merge the 'movies' and 'credits' DataFrames
# We're merging 'on' the 'id' column, which is now common to both.
df = movies.merge(credits, on='id')

# Step 3: Print the shape of the new merged DataFrame (df)
# This helps you verify if the merge resulted in the expected number of rows and columns.
print("Shape after merging movies and credits:", df.shape)

print("\n")


# Task 2: Check for missing data in the merged DataFrame
print("--- Task 2: Checking for missing data in merged DataFrame ---")

# Use isna().sum() to count missing values across all columns of your new 'df'
print(df.isna().sum())

print("\n")


# Task 3: Handle missing 'overview' data
print("--- Task 3: Handling missing 'overview' ---")

# Fill any NaN values in the 'overview' column with an empty string ('')
df['overview'] = df['overview'].fillna('')

# Verify that there are no more NaNs in the 'overview' column
print("Missing values in 'overview' after fillna:", df['overview'].isna().sum()) # Should be 0

print("\n")


# Task 4: Save the cleaned DataFrame
print("--- Task 4: Saving cleaned_movies.csv ---")

# Save the DataFrame 'df' to a new CSV file
# index=False prevents Pandas from writing the DataFrame index as a column in the CSV
df.to_csv('cleaned_movies.csv', index=False)

print("Cleaned movie data saved to 'cleaned_movies.csv'")
print("\n")

print("--- Project Day 3: Data Preparation & Merging Complete! ---")