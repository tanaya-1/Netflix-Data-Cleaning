
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


# --------------------------------------------------
# STEP 1: SET UP FILE PATHS AND OUTPUT FOLDER
# --------------------------------------------------

# Get the folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent

# Path to the cleaned Netflix dataset
DATA_PATH = BASE_DIR / "netflix_cleaned.csv"

# Folder where our results will be saved
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# STEP 2: LOAD AND INSPECT THE DATASET
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("NETFLIX OTT ANALYSIS: FILTERING AND SORTING")
print("=" * 60)

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

# Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)


# --------------------------------------------------
# STEP 3: FILTER MOVIES RELEASED AFTER 2015
# --------------------------------------------------

movies_after_2015 = df[
    (df["type"] == "Movie") &
    (df["release_year"] > 2015)
].copy()

print("\n" + "=" * 60)
print("1. MOVIES RELEASED AFTER 2015")
print("=" * 60)

print("Total movies:", len(movies_after_2015))

print(
    movies_after_2015[
        ["title", "release_year", "rating"]
    ].head(10).to_string(index=False)
)

movies_after_2015.to_csv(
    OUTPUT_DIR / "movies_after_2015.csv",
    index=False
)


# --------------------------------------------------
# STEP 4: FILTER TITLES ASSOCIATED WITH INDIA
# --------------------------------------------------

india_titles = df[
    df["country"].str.contains(
        r"\bIndia\b",
        case=False,
        na=False,
        regex=True
    )
].copy()

print("\n" + "=" * 60)
print("2. TITLES ASSOCIATED WITH INDIA")
print("=" * 60)

print("Total titles:", len(india_titles))

print(
    india_titles[
        ["title", "type", "country", "release_year"]
    ].head(10).to_string(index=False)
)

india_titles.to_csv(
    OUTPUT_DIR / "india_titles.csv",
    index=False
)


# --------------------------------------------------
# STEP 5: FILTER TITLES RATED TV-MA
# --------------------------------------------------

tv_ma_titles = df[
    df["rating"].eq("TV-MA")
].copy()

print("\n" + "=" * 60)
print("3. TITLES RATED TV-MA")
print("=" * 60)

print("Total TV-MA titles:", len(tv_ma_titles))

print(
    tv_ma_titles[
        ["title", "type", "rating", "release_year"]
    ].head(10).to_string(index=False)
)

tv_ma_titles.to_csv(
    OUTPUT_DIR / "tv_ma_titles.csv",
    index=False
)


# --------------------------------------------------
# STEP 6: FIND THE LONGEST MOVIES
# --------------------------------------------------

# Extract the numeric duration from values like "90 min"
df["duration_value"] = pd.to_numeric(
    df["duration"].str.extract(r"(\d+)", expand=False),
    errors="coerce"
)

# Keep movies with valid runtimes in minutes
movies_with_duration = df[
    (df["type"] == "Movie") &
    (df["duration"].str.contains(
        r"\bmin\b",
        case=False,
        na=False,
        regex=True
    )) &
    (df["duration_value"].notna())
].copy()

# Sort from longest to shortest
longest_movies = movies_with_duration.sort_values(
    by="duration_value",
    ascending=False
)

print("\n" + "=" * 60)
print("4. TOP 10 LONGEST MOVIES")
print("=" * 60)

print(
    longest_movies[
        ["title", "release_year", "duration", "duration_value"]
    ].head(10).to_string(index=False)
)

longest_movies.to_csv(
    OUTPUT_DIR / "longest_movies.csv",
    index=False
)


# --------------------------------------------------
# STEP 7: FIND THE NEWEST NETFLIX ADDITIONS
# --------------------------------------------------

newest_additions = df.sort_values(
    by="date_added",
    ascending=False,
    na_position="last"
)

print("\n" + "=" * 60)
print("5. TOP 10 NEWEST NETFLIX ADDITIONS")
print("=" * 60)

print(
    newest_additions[
        ["title", "type", "date_added", "release_year"]
    ].head(10).to_string(index=False)
)

newest_additions.to_csv(
    OUTPUT_DIR / "newest_additions.csv",
    index=False
)


# --------------------------------------------------
# STEP 8: VISUALIZE MOVIES VS TV SHOWS
# --------------------------------------------------

type_counts = df["type"].value_counts()

print("\n" + "=" * 60)
print("6. MOVIES VS TV SHOWS")
print("=" * 60)

print(type_counts)

print("\nPercentage distribution:")
print(
    (df["type"].value_counts(normalize=True) * 100).round(2)
)

# Create the pie chart
plt.figure(figsize=(7, 7))

type_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Movies vs TV Shows on Netflix",
    ylabel="",
    shadow=True
)

plt.tight_layout()

# Save the chart to the outputs folder
plt.savefig(
    OUTPUT_DIR / "movies_vs_tv_shows.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# STEP 9: PRINT A SUMMARY OF OUR ANALYSIS
# --------------------------------------------------

print("\n" + "=" * 60)
print("FINAL FILTERING AND SORTING SUMMARY")
print("=" * 60)

print("Total titles in dataset:", len(df))
print("Movies released after 2015:", len(movies_after_2015))
print("Titles associated with India:", len(india_titles))
print("Titles rated TV-MA:", len(tv_ma_titles))
print("Movies with valid runtimes:", len(movies_with_duration))

if not longest_movies.empty:
    longest = longest_movies.iloc[0]
    print(
        f"Longest movie: {longest['title']} "
        f"({longest['duration']})"
    )

if df["date_added"].notna().any():
    latest = newest_additions.dropna(
        subset=["date_added"]
    ).iloc[0]

    print(
        f"Most recently added title in dataset: "
        f"{latest['title']} ({latest['date_added'].date()})"
    )

print("\nContent type counts:")
print(type_counts)

print("\nAll results saved in:", OUTPUT_DIR)
print("Filtering and sorting analysis completed successfully!")
