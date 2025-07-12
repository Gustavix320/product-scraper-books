# 📚 Product Scraper – BooksToScrape

A simple yet professional web scraping project using Python and BeautifulSoup to extract book data from the [BooksToScrape](http://books.toscrape.com) demo website.

## 🚀 Features

- Scrapes **all 50 pages** of product listings
- Collects:
  - 📘 Book title
  - 💷 Price
  - ⭐ Rating (text-based: One, Two, etc.)
  - 🔗 Link to the product page
- Saves data in two formats:
  - `data/books.json`
  - `data/books.csv` (Excel-compatible)
- Handles character encoding (UTF-8 and UTF-8-SIG)
- Clean, well-commented code and organized project structure


## 🗂 Project Structure

product-scraper-books/
│
├── data/
│ ├── books.csv # CSV export
│ └── books.json # JSON export
│
├── scraper.py # Main scraping script
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🛠️ Technologies Used

- Python 3.x
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/)
- Built-in `csv`, `json`, and `os` modules


## ⚙️ How to Run

1. Clone this repository:
  - git clone https://github.com/your-username/product-scraper-books.git
  - cd product-scraper-books

2. Create a virtual environment (optional but recommended):
  - python -m venv venv
  - venv\Scripts\activate  # Windows
  - source venv/bin/activate  # Mac/Linux

3. Install the required packages:
  - pip install -r requirements.txt

4. Run the scraper:
  - python scraper.py

5. Output files will be saved in the data/ folder.


## Example Output (JSON)
[
  {
    "title": "A Light in the Attic",
    "price": "£51.77",
    "rating": "Three",
    "link": "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  },
  ...
]

## 📌 Purpose
This project is part of a professional portfolio to demonstrate experience in:
- Web scraping with BeautifulSoup
- Handling pagination
- Exporting structured data
- Building clean, production-ready scripts

## 👤 Author

**Gustavo Santos**  
Backend Developer | Python Web Scraper | Open to Remote Opportunities  
• [LinkedIn](https://www.linkedin.com/in/gustavo-santos-502364338/) 
• [GitHub](https://github.com/Gustavix320)
