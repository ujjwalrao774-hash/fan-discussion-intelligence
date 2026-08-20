# fan-discussion-intelligence (The Boys Series)
Data analytics project exploring character engagement and character associations in fan discussions using Python and association rule mining.

## The Question

I started with a simple question:

> **Which characters in _The Boys_ are discussed the most by fans?**

After answering that, I wanted to go one step further:

> **Which pairs of characters tend to appear together in discussions more often than expected?**

To answer these questions, I analyzed comments collected from **Reddit and YouTube across all 5 seasons**.

## Approach

The project was built in two stages.

### 1. Character Discussion Analysis

- Collected comments from Reddit and YouTube for each season.
- Extracted top-level Reddit comments from saved HTML pages using Python.
- Combined comments from different sources season-wise.
- Created a dictionary of major characters and their aliases.
- Used **regex-based matching** to identify character mentions.
- Converted aliases to a single canonical character name.
- Prevented duplicate counting when a character appeared multiple times in the same comment.
- Counted the number of comments mentioning each character.

For example:

```text
"Homelander was great. I really liked Homelander."
                    ↓
              Homelander
````

The character is counted once because the analysis measures **whether a character was discussed in a comment**, not how many times their name appeared.

### 2. Character Association Analysis

I then converted each comment into a binary character-presence matrix:

```text
1 → character mentioned
0 → character not mentioned
```

This allowed each comment to be treated as a basket of characters.

I used the **Apriori algorithm** to identify character combinations and applied:

* Minimum support: **0.005**
* **Lift** to measure how unusually often two characters appeared together.

Lift greater than 1 indicates that the pair appeared together more often than would be expected if their appearances were independent.

## What I Found

### Most Discussed Characters

Across the analyzed comments:

| Rank | Character     | Comments |
| ---- | ------------- | -------: |
| 1    | Homelander    |    1,117 |
| 2    | Billy Butcher |      774 |
| 3    | Starlight     |      404 |

The season-wise analysis also showed that discussion patterns changed across seasons. Homelander dominated several seasons, while characters such as Billy Butcher, Starlight and Soldier Boy became particularly prominent in specific seasons.

### Strongest Character Associations

Some of the highest-lift pairs were:

| Character Pair       | Comments |  Lift |
| -------------------- | -------: | ----: |
| Frenchie – Kimiko    |       93 | 10.21 |
| Hughie – Starlight   |      160 |  5.60 |
| Frenchie – Hughie    |       60 |  4.85 |
| Frenchie – Starlight |       54 |  3.96 |
| A-Train – Starlight  |       50 |  3.84 |

One interesting finding was that **the most discussed characters were not necessarily the most strongly associated characters**.

For example, Homelander had the highest overall discussion count, while Frenchie–Kimiko had the highest lift.

## Technical Implementation

**Languages & Libraries**

* Python
* Pandas
* NumPy
* Regular Expressions
* BeautifulSoup
* Mlxtend
* Matplotlib
* Google Colab
* Git / GitHub

**Key techniques**

* HTML parsing
* Data preprocessing
* Regex-based entity matching
* Alias normalization
* Binary feature representation
* Exploratory data analysis
* Apriori association rule mining
* Support and lift analysis

## Repository Structure

```text
fan-discussion-intelligence/
│
├── data/
│   ├── season_1_comments.csv
│   ├── season_2_comments.csv
│   ├── season_3_comments.csv
│   ├── season_4_comments.csv
│   ├── season_5_comments.csv
│   └── all_season_comments_combined.csv
│
├── notebooks/
│   ├── 01_combine_season_data.ipynb
│   └── 02_analysis_and_apriori.ipynb
│
├── results/
│   ├── apriori_lift_result.png
│   └── the_boys_character_analysis.pdf
│
├── src/
│   └── extract_comments.py
│
└── README.md
```

## Results

Detailed visualizations are available in:

* `results/the_boys_character_analysis.pdf`
* `results/apriori_lift_result.png`

The notebooks contain the complete analysis workflow.

## Limitations & Next Steps

The analysis represents discussions from Reddit and YouTube rather than the entire *The Boys* audience.

The current character detection approach also depends on a manually defined character/alias dictionary and does not consider the sentiment or context of a mention.
