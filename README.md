# 📚 BookScraper – Web Scraping Project

A professional Python web scraping project that extracts book data from  
👉 https://books.toscrape.com/

The scraper collects:

- ✅ Product Name
- ✅ Price
- ✅ Rating (Converted to Numeric)
- ✅ Product Link

The data is then:
- Sorted by price (Highest → Lowest)
- Saved into a CSV file using **pandas**
- Organized in a clean project structure

---

## 🚀 Features

- Modular and clean code structure
- Uses custom request headers
- Saves raw HTML locally
- Parses HTML using BeautifulSoup
- Converts ratings (One–Five) → Numeric (1–5)
- Cleans and converts price to float
- Sorts data by price descending
- Saves processed data using pandas
- Professional folder organization

---

## 📁 Project Structure

```
BookScraper/
│
├── data/
│   ├── raw-data/
│   │   └── books.html
│   │
│   └── processed-data/
│       └── books_sorted.csv
│
├── scraper.py
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.x
- requests
- BeautifulSoup (bs4)
- pandas
- lxml
- urllib.parse
- os

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/BookScraper.git
cd BookScraper
```

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas lxml
```

---

## ▶️ How to Run

```bash
python scraper.py
```

The script will:

1. Fetch HTML from the website
2. Save raw HTML into `data/raw-data/`
3. Extract book information
4. Sort by price (highest to lowest)
5. Save final CSV into `data/processed-data/`

---

## 📊 Example Output (books_sorted.csv)

| product name              | price | ratings | link |
|---------------------------|-------|---------|------|
| Book Title A              | 57.20 | 4       | https://... |
| Book Title B              | 54.32 | 5       | https://... |
| Book Title C              | 20.15 | 3       | https://... |

---

## 🖼 Result Output Screenshot

After running the script, your CSV file will look like this:

![Output Screenshot](images/output_example.png)

> 💡 Tip: Take a screenshot of your CSV file and save it inside:
>
> ```
> images/output_example.png
> ```

---

## 🧠 How Rating Conversion Works

HTML rating example:

```html
<p class="star-rating Three"></p>
```

Converted using dictionary mapping:

```
One   → 1
Two   → 2
Three → 3
Four  → 4
Five  → 5
```

---

## 🧹 Data Cleaning

- Removed special encoding characters (Â£)
- Converted price from string → float
- Used `urljoin()` to generate full product links
- Sorted price using pandas

---

## 📌 Future Improvements

- Scrape all 50 pages (Pagination)
- Add delay & retry system
- Add logging
- Export to Excel (.xlsx)
- Add CLI arguments
- Convert into production-level Scraper class

---

## 👨‍💻 Author

**Sameer Khan**  
Python Developer | Web Scraping Enthusiast  

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!
