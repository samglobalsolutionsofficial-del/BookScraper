import requests
import os
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin


# ==========================================
# 1️⃣ FETCH AND SAVE HTML
# ==========================================

def fetch_and_save_html(url: str, output_path: str, headers: dict = None) -> bool:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, mode='w', encoding='utf-8') as f:
            f.write(response.text)

        print("✅ HTML saved successfully")
        return True

    except requests.RequestException as e:
        print(f"❌ Error fetching {url}: {e}")
        return False


# ==========================================
# 2️⃣ PARSE SAVED HTML
# ==========================================

def parse_html_file(file_path: str) -> BeautifulSoup | None:
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

    return soup


# ==========================================
# 3️⃣ EXTRACT DATA
# ==========================================

def extract_data(soup: BeautifulSoup, base_url: str) -> list[dict]:
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    books = []

    products = soup.find_all('article', class_='product_pod')

    for product in products:
        name = product.find('h3').find('a')['title']

        # Clean & convert price
        raw_price = product.find("p", class_="price_color").text
        clean_price = raw_price.replace("£", "").replace("Â", "")
        price = float(clean_price)

        # Rating
        rating_text = product.find("p", class_="star-rating")["class"][1]
        rating_number = rating_map[rating_text]

        # Full link
        relative_link = product.h3.a["href"]
        full_link = urljoin(base_url, relative_link)

        books.append({
            "product name": name,
            "price": price,
            "ratings": rating_number,
            "link": full_link
        })

    return books


# ==========================================
# 4️⃣ SAVE TO CSV USING PANDAS
# ==========================================

def save_to_csv(data: list[dict], output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.DataFrame(data)

    # Sort price highest → lowest
    df = df.sort_values(by="price", ascending=False)

    df.to_csv(output_path, index=False)

    print(f"✅ Data saved & sorted successfully → {output_path}")


# ==========================================
# 5️⃣ MAIN EXECUTION
# ==========================================

if __name__ == "__main__":

    url = 'https://books.toscrape.com/'
    raw_path = 'data/raw-data/books.html'
    output_csv = 'data/processed-data/books_sorted.csv'

    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    # Step 1: Fetch HTML
    if fetch_and_save_html(url, raw_path, headers):

        # Step 2: Parse HTML
        soup = parse_html_file(raw_path)

        if soup:
            # Step 3: Extract Data
            books_data = extract_data(soup, url)

            # Step 4: Save to CSV
            save_to_csv(books_data, output_csv)
