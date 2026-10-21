"""
Part 3: Pandas - Counting (value_counts) + Grouping (groupby)
Input : netflix_cleaned.csv  (output of Part 1 - cleaning)
Output: printed results + CSV tables saved in outputs/ folder
"""

import os
import pandas as pd


df = pd.read_csv("netflix_cleaned.csv")
print("Shape:", df.shape)
print(df.columns.tolist())


df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

os.makedirs("outputs", exist_ok=True)


type_counts = df["type"].value_counts()
print("\n--- Content type ---\n", type_counts)
print("\nPercentage:\n", (df["type"].value_counts(normalize=True) * 100).round(2))


rating_counts = df["rating"].value_counts()
print("\n--- Ratings ---\n", rating_counts)


country_split = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)
country_split = country_split[country_split != "Unknown"]
top_countries = country_split.value_counts().head(10)
print("\n--- Top 10 countries ---\n", top_countries)


genre_split = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)
top_genres = genre_split.value_counts().head(10)
print("\n--- Top 10 genres ---\n", top_genres)


added_per_year = df.groupby("year_added").size().sort_index()
print("\n--- Titles added per year ---\n", added_per_year)


released_per_year = df.groupby("release_year").size().sort_index()
print("\n--- Last 10 release years ---\n", released_per_year.tail(10))


year_type = df.groupby(["year_added", "type"]).size().unstack(fill_value=0)
print("\n--- Year added by type ---\n", year_type)


type_summary = df.groupby("type").agg(
    total_titles=("show_id", "count"),
    earliest_release=("release_year", "min"),
    latest_release=("release_year", "max"),
    avg_release_year=("release_year", "mean"),
)
print("\n--- Type summary ---\n", type_summary.round(1))


df_country = df.assign(country=df["country"].str.split(",")).explode("country")
df_country["country"] = df_country["country"].str.strip()
df_country = df_country[df_country["country"] != "Unknown"]

country_type = (
    df_country.groupby(["country", "type"]).size().unstack(fill_value=0)
)
country_type["total"] = country_type.sum(axis=1)
country_type = country_type.sort_values("total", ascending=False).head(10)
print("\n--- Top 10 countries by type ---\n", country_type)


rating_type = df.groupby(["type", "rating"]).size().unstack(fill_value=0)
print("\n--- Rating by type ---\n", rating_type)


type_counts.to_csv("outputs/type_counts.csv")
rating_counts.to_csv("outputs/rating_counts.csv")
top_countries.to_csv("outputs/top_countries.csv")
top_genres.to_csv("outputs/top_genres.csv")
added_per_year.to_csv("outputs/added_per_year.csv")
year_type.to_csv("outputs/year_by_type.csv")
country_type.to_csv("outputs/country_by_type.csv")
print("\nSaved result tables to outputs/")


print("\n=== INSIGHTS ===")
print(f"Most common type   : {type_counts.idxmax()} ({type_counts.max()} titles)")
print(f"Most common rating : {rating_counts.idxmax()} ({rating_counts.max()} titles)")
print(f"Top country        : {top_countries.idxmax()} ({top_countries.max()} titles)")
print(f"Top genre          : {top_genres.idxmax()} ({top_genres.max()} titles)")
print(f"Peak year added    : {int(added_per_year.idxmax())} ({added_per_year.max()} titles)")
