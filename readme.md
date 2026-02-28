# Amazon Orders

Processing an Amazon orders file for budgeting purposes.

This script reads a raw Amazon order export, cleans and categorises the data, then produces several summarised CSV reports broken down by category and month.

## Machine Learning / Data Science Concepts

Although this project does not train a model, it applies a number of core concepts from the data-science and machine learning workflow:

| Concept | Where it is used |
|---|---|
| **ETL Pipeline** (Extract → Transform → Load) | The `Read`, `Map`, and `Write` classes each own one stage of the pipeline, cleanly separating concerns the same way a typical ML data-prep pipeline does. |
| **Data Cleaning / Pre-processing** | Dollar signs and commas are stripped from monetary values before converting to `float`, preventing downstream type errors — a standard pre-processing step before feeding data into any model. |
| **Categorical Feature Mapping (Label Encoding)** | Raw Amazon category strings (e.g. `PET_FOOD`) are merged with a lookup table to produce a higher-level `Parent Category` label. This mirrors label / ordinal encoding used in ML pipelines to create meaningful categorical features. |
| **Feature Engineering** | A `month` column is derived from the `Order Date` timestamp so that spend can be analysed at the monthly level — a classic time-series feature-extraction technique. |
| **Data Aggregation & Summarisation** | `groupby` / `sum` and `pivot_table` operations condense thousands of raw rows into compact summary statistics, the same aggregation step used when building features for tabular ML models. |
| **Pandas DataFrame API** | The entire pipeline is built on [pandas](https://pandas.pydata.org/), the de-facto standard data-manipulation library in the Python ML ecosystem. |

## Getting Started

Log in to Amazon.com, click on ```account & lists``` in the top right, then ```Download order reports```. Download a report of type ```items``` and place it in the [data/raw/](data/raw/) directory.

### Prerequisites

The script expects a ```categories.csv``` file for sensible budgeting categories in the [data/lookup/](data/lookup/) folder.

The lookup file maps raw Amazon category names to human-readable parent categories:

```
Parent Category  |  Category
-----------------|--------------------
Pets             |  PET_FOOD
Bath             |  BATHWATER_ADDITIVE
Bath             |  SKIN_CLEANING_AGENT
Electronics      |  ELECTRONIC_ADAPTER
```

### Installing

There is a make file with basic functions ... it's a bit problematic, but demonstrates commands you will need.

Help:
```
make help
```

Build:
```
make build-all
```

Run:
```
make run
```

### Output

Files will be generated to the [data/processed/](data/processed/) folder:

| File | Description |
|---|---|
| `orders_by_monthly_spend.csv` | Spend per parent category broken down by calendar month |
| `orders_by_category.csv` | Total spend and quantity per raw Amazon category, sorted descending |
| `orders_by_parent_category.csv` | Total spend and quantity per parent category, sorted descending |
