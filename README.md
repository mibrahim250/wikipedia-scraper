# Wikipedia Article Summary Scraper

This is a simple Python project that extracts the title and summary of Wikipedia articles. It is designed to showcase basic web scraping techniques using the `requests` and `BeautifulSoup` libraries.

---

## Features
- Fetches the title and the first meaningful paragraph (summary) from a Wikipedia article.
- Demonstrates the use of web scraping libraries in Python.
- Beginner-friendly code, easy to understand and extend.

---

## How It Works
1. The user inputs a topic (e.g., "Python programming").
2. The program formats the input into a valid Wikipedia URL.
3. It sends a request to Wikipedia and retrieves the HTML content.
4. Extracts the title and the first meaningful paragraph as a summary.

---

## Requirements
Make sure you have the following installed:
- **Python** (version 3.7 or higher)
- **Libraries**:
  - `requests`
  - `beautifulsoup4`

To install the required libraries, run:
```bash
pip install requests beautifulsoup4
