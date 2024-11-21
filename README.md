# eBay Scraper

A Python-based web scraping program that retrieves data from eBay search results using queries specified in a CSV file. The results include the title, seller, price, and position of up to 20 listings per query, which are saved to an output CSV file.

## Table of Contents

- [Features](#Features)
- [Usage](#usage)
- [Requirements](#Requirements)
- [License](#license)
- [Contact](#contact)

## Features

1. Reads search terms from a CSV file (queries.csv).
2. Scrapes up to 20 results for each query on eBay.
3. Retrieves:
- Listing title
- Seller name
- Price
4. Position in search results
5. Adds randomized delays (3–6 seconds) between queries to avoid rate limiting.
6. Saves results to a CSV file (results.csv).

## Usage

### Step 1: Clone the Repository
Clone this repository to your local machine:

```
git clone https://github.com/pawelczubak/ebay_scraper.git
cd ebay_scraper
```

### Step 2: Install Dependencies
Install the required Python libraries:

```
pip install selenium webdriver-manager
```

Step 3: Prepare the Input File
Create a queries.csv file in the project directory with the following structure:

```
ebay_query
vw golf 2016 mirror glass
bmw f30 side mirror
audi a3 rear view mirror
```

## Requirements

1. Python 3.8 or higher
2. Dependencies:
- selenium
- webdriver-manager
- csv (built-in)
3. Additional Tools:
- Mozilla Firefox (latest version recommended)
- Geckodriver (managed automatically by webdriver-manager)

## License
<br> --------------------------------------------------------------------------
<br> "THE BEERWARE LICENSE" (Revision 42):
<br>pawelczubak@op.pl wrote this code. As long as you retain this notice,
<br>you can do whatever you want with this stuff. If we meet someday, and you think
<br>this code is worth it, you can buy me a beer in return.
<br> --------------------------------------------------------------------------

## Author

Paweł Czubak
<br>Feel free to reach out via email at pawelczubak@op.pl for any questions or contributions!