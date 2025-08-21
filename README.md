# UN Data Structure Project

This repository contains tools and processes for scraping, processing, and storing human rights-related data from various UN sources. The project collects data from the Universal Human Rights Index and UN Treaty Collection to create structured datasets for analysis and visualization.

## Project Overview

The UN Data Structure project aims to:

1. Extract structured data from UN websites about human rights recommendations and treaty participation
2. Process and clean the data to create consistent, analyzable datasets
3. Store the data in both CSV files and MongoDB for flexible access
4. Provide a foundation for data analysis and visualization tools

## Repository Structure

```
un-data-structure/
├── scrapers/                       # Web scraping notebooks
│   ├── scraper_universal-human-rights-index.ipynb  # Web scraper for human rights recommendations
│   ├── treatiy_collection-checkpoint.ipynb         # Web scraper for UN treaty participation data
│   └── unConcerns_cleainging-checkpoint.ipynb      # Additional scrapers for UN concerns
├── data_cleaning/                  # Data cleaning notebooks
│   ├── cleaning_CAC-dataset.ipynb  # Data cleaning for Committee Against Torture dataset
│   ├── cleaning_CAT-dataset.ipynb  # Data cleaning for Convention Against Torture dataset
│   └── treatiy_collection.ipynb    # Treaty collection data processing
├── data-sets/                      # Processed and cleaned datasets
│   ├── Key_Differences_CAT.csv     # Analyzed differences in CAT data
│   ├── ohchr_cac_2022_2024.csv     # Committee against Torture data
│   ├── ohchr_cat_2022_2024.csv     # Convention against Torture data
│   └── scraped-dataset.csv         # Combined scraped data
├── project-background-information/ # Research materials and context
├── pymongo/                        # Database integration scripts
│   └── database_creater.py         # Script to populate MongoDB with scraped data
└── README.md                       # Project documentation
```

## Data Collection Process

### 1. Web Scraping

The project uses two main approaches for data collection:

#### A. Universal Human Rights Index Scraper

The [`scraper_universal-human-rights-index.ipynb`](./scrapers/scraper_universal-human-rights-index.ipynb) notebook:

- Uses Playwright (async browser automation) to interact with dynamic web content
- Extracts data from the Committee against Torture (CAT) and the Special Rapporteur in the field of cultural rights
- Collects information about:
  - Countries receiving recommendations
  - Affected groups (women, children, minorities, etc.)
  - Human rights themes (right to education, freedom from torture, etc.)
  - Recommendation types and dates

**Data Structure:**
```json
{
    "year": "2022",
    "country": "Republic of Korea", 
    "term": "Fundamental legal safeguards",
    "concerned-group": ["Children", "Youth & juveniles"],
    "human-rights-theme": ["Right to liberty and security of person"],
    "annotation-type": ["Recommendation", "Concern"]
}
```

#### B. UN Treaty Collection Scraper

The [`treatiy_collection.ipynb`](./data_cleaning/treatiy_collection.ipynb) notebook:

- Uses BeautifulSoup for HTML parsing
- Extracts country participation data for UN treaties
- Identifies signature status and type of approval (ratification, accession, succession)

**Data Structure:**
```json
{
    "country-name": "Afghanistan",
    "signature-status": "signed",
    "approval-status": "approved"
}
```

### 2. Data Cleaning

The [`cleaning_CAC-dataset.ipynb`](./data_cleaning/cleaning_CAC-dataset.ipynb) and [`cleaning_CAT-dataset.ipynb`](./data_cleaning/cleaning_CAT-dataset.ipynb) notebooks:

- Standardize country names and format
- Handle missing values
- Extract and parse dates
- Normalize text fields for consistent analysis
- Convert lists stored as strings back to proper Python lists
- Remove duplicates and merge related records

### 3. Data Export

Each notebook exports the processed data to CSV files in the `data-sets/` directory:

- `ohchr_cac_2022_2024.csv`: Committee against Torture data
- `ohchr_cat_2022_2024.csv`: Convention against Torture data
- Other specialized datasets for specific analyses

### 4. Database Integration

The [`database_creater.py`](./pymongo/database_creater.py) script:

- Connects to MongoDB Atlas cloud database
- Creates a database called `humanrights_database`
- Imports CSV data into appropriate collections
- Enables more complex queries and aggregations than possible with CSV files

## Setting Up the MongoDB Database

To create and populate the MongoDB database:

1. Ensure MongoDB is installed or use MongoDB Atlas cloud service
2. Update the connection string in `database_creater.py` with your credentials
3. Run the script to import data from the CSV files:

```bash
python pymongo/database_creater.py
```

The script will:
- Connect to MongoDB using the provided URI
- Create a database called `humanrights_database`
- Create collections for different data types (e.g., `committiee_against_torture`)
- Import data from the CSV files into the appropriate collections

## Potential Applications

The collected and structured data enables:

- Analysis of patterns in human rights concerns across countries
- Tracking changes in recommendations over time
- Identifying frequently affected groups by country or region
- Supporting human rights advocacy with data-driven insights
- Creating visualizations and dashboards for public awareness

## Dependencies

- Python 3.x
- Pandas
- BeautifulSoup4
- Playwright
- requests
- PyMongo
- Jupyter Notebook

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NourSaf/un-data-structure.git
cd un-data-structure
```

2. Install required packages:
```bash
pip install pandas beautifulsoup4 playwright requests pymongo jupyter
python -m playwright install
```

3. Run the Jupyter notebooks to collect and process data:
```bash
jupyter notebook
```

4. Set up the database:
```bash
python pymongo/database_creater.py
```

## Disclaimer

The classification labels for Concerned persons/groups, Human Rights Themes and SDGs are provided for informational purposes only. While we strive for accuracy, these labels may not be exhaustive and should be considered as indicative insights rather than definitive categorizations.
