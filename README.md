# Netflix Movies and TV Shows Analysis

## Project Description

This mini project explores the Netflix Movies and TV Shows dataset using Python and Pandas. The project focuses on data cleaning, filtering, sorting, grouping, and statistical analysis to understand the content available on Netflix.

**Important:** The original/raw CSV dataset is preserved and must not be modified. All cleaning and analysis are performed on a separate dataset.

## Project Objectives

- Clean and prepare the Netflix dataset for analysis.
- Handle missing values and duplicate records.
- Filter titles based on release year, country, and content rating.
- Sort movies by runtime and titles by date added.
- Analyze content types, ratings, countries, genres, and yearly trends.
- Calculate movie runtime and TV show season statistics.
- Export analysis results for further use.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook / Python scripts
- Git and GitHub
- GitHub Codespaces

## Project Tasks

### 1. Data Cleaning

- Loaded the original Netflix dataset.
- Checked missing values and duplicate records.
- Filled missing director, cast, and country values with `"Unknown"`.
- Removed records missing rating or duration.
- Removed duplicate records.
- Converted `date_added` into datetime format.
- Exported the cleaned dataset as `netflix_cleaned.csv`.

### 2. Filtering and Sorting

- Filtered movies released after 2015.
- Identified titles associated with India.
- Filtered titles rated `TV-MA`.
- Sorted movies by runtime to identify the longest movies.
- Sorted titles by date added to identify the newest additions.
- Compared the distribution of Movies and TV Shows.

### 3. Counting and Grouping

- Counted Movies and TV Shows and calculated their percentage distribution.
- Analyzed content ratings.
- Identified the top 10 countries and genres.
- Examined titles added to Netflix by year.
- Compared release-year trends.
- Grouped content by type, country, and rating.

### 4. Duration Analysis

- Extracted numerical duration values and duration units.
- Separated Movies from TV Shows.
- Calculated mean, median, and standard deviation for movie runtimes.
- Calculated mean, median, and standard deviation for TV show seasons.

## Project Files

| File / Folder | Description |
|---|---|
| `netflix_cleaned.csv` | Cleaned dataset used for analysis |
| `netflix_data_cleaning.py` | Data cleaning script |
| `filter_sort_analysis.py` | Filtering and sorting analysis |
| `part3_counting_grouping.py` | Counting and grouping analysis |
| `duration_numpy.py` | Duration analysis using NumPy |
| `outputs/` | Exported analysis results and visualization |

*File names above describe the expected project structure; verify that each file exists in the repository.*

## Analysis Outputs

The filtering and sorting analysis generates:

- `movies_after_2015.csv`
- `india_titles.csv`
- `tv_ma_titles.csv`
- `longest_movies.csv`
- `newest_additions.csv`
- `movies_vs_tv_shows.png`

The counting and grouping script exports summary tables to the `outputs/` folder. The duration analysis exports `netflix_duration_analysis.csv`.

## Key Learning Outcomes

- Data cleaning and preprocessing using Pandas.
- Boolean filtering and sorting DataFrames.
- Handling missing values and duplicates.
- Grouping, aggregation, and statistical calculations.
- Working with CSV files.
- Data visualization using Matplotlib.
- Collaborative development using Git and GitHub.

## How to Run the Project

1. Clone the repository.
2. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib
   ```

3. Ensure the required input CSV files are available in the expected locations.
4. Run the relevant Python scripts:

   ```bash
   python netflix_data_cleaning.py
   python filter_sort_analysis.py
   python part3_counting_grouping.py
   python duration_numpy.py
   ```

5. Check the generated CSV files and visualization in the output locations.

**Note:** Run the cleaning script first if `netflix_cleaned.csv` needs to be generated. Keep the original/raw CSV unchanged.

## Team Project

This project was developed collaboratively using Git and GitHub, with different team members contributing to different parts of the analysis.
