import pandas as pd
import numpy as np

# Load the cleaned Netflix dataset
df = pd.read_csv("netflix_cleaned.csv")

# STEP 1: Split duration into value and unit
df["duration_value"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)", expand=False),
    errors="coerce"
)

df["duration_unit"] = df["duration"].str.extract(
    r"([A-Za-z]+)", expand=False
)

print("Duration column split successfully!")
print(df[["title", "type", "duration",
          "duration_value", "duration_unit"]].head())

# STEP 2: Separate movies and TV shows
movies = df[df["type"] == "Movie"]
tv_shows = df[df["type"] == "TV Show"]

print("\nTotal Movies:", len(movies))
print("Total TV Shows:", len(tv_shows))

# STEP 3: Calculate statistics using NumPy
movie_durations = movies.loc[
    movies["duration_unit"] == "min", "duration_value"
].dropna()

tv_seasons = tv_shows.loc[
    tv_shows["duration_unit"].str.startswith("Season", na=False),
    "duration_value"
].dropna()

print("\nMOVIE DURATION STATISTICS")

if not movie_durations.empty:
    print("Mean:", np.mean(movie_durations))
    print("Median:", np.median(movie_durations))
    print("Standard Deviation:", np.std(movie_durations))

print("\nTV SHOW SEASON STATISTICS")

if not tv_seasons.empty:
    print("Mean:", np.mean(tv_seasons))
    print("Median:", np.median(tv_seasons))
    print("Standard Deviation:", np.std(tv_seasons))

# Export the analysis dataset
df.to_csv("netflix_duration_analysis.csv", index=False)

print("\nAnalysis completed successfully!")
