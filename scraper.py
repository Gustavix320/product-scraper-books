import requests
from bs4 import BeautifulSoup
import csv
import json
import os

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_books():
    all_books = []

    for page in range(1, 51):  # BooksToScrape tem 50 páginas
        print(f"Scraping página {page}...")
        url = BASE_URL.format(page)
        response = requests.get(url, headers=HEADERS)
        response.encoding = 'utf-8' 


        if response.status_code != 200:
            print(f"Erro na página {page}: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.select('.product_pod')

        for book in books:
            title = book.h3.a['title']
            price = book.select_one('.price_color').text.strip()
            rating = book.p.get('class')[1]  # Ex: "One", "Two", "Three"
            link = book.h3.a['href']
            full_link = "http://books.toscrape.com/catalogue/" + link

            all_books.append({
                'title': title,
                'price': price,
                'rating': rating,
                'link': full_link
            })

    return all_books

def save_data(books):
    os.makedirs('data', exist_ok=True)

    # Salvar como JSON
    with open('data/books.json', 'w', encoding='utf-8') as f_json:
        json.dump(books, f_json, indent=4, ensure_ascii=False)

    # Salvar como CSV
    with open('data/books.csv', 'w', newline='', encoding='utf-8-sig') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=['title', 'price', 'rating', 'link'])
        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    books = scrape_books()
    save_data(books)
    print("✅ Dados salvos em 'data/books.json' e 'data/books.csv'")
