import pandas as pd

# Load the Netflix dataset
df = pd.read_csv("netflix_titles.csv")

print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Records:", df.duplicated().sum())

# Fill missing values
columns_to_fill = ["director", "cast", "country"]

for col in columns_to_fill:
    df[col] = df[col].fillna("Unknown")

# Remove rows missing rating or duration
df = df.dropna(subset=["rating", "duration"])

# Remove duplicate records
df = df.drop_duplicates()

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"].str.strip(),
    errors="coerce"
)

print("\nData Cleaning Completed!")
print("Cleaned Dataset Shape:", df.shape)

# Export cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("Cleaned dataset saved as netflix_cleaned.csv")