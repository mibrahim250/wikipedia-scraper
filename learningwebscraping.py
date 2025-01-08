''' 
This project is for educational purposes only. Content retrieved from Wikipedia is licensed under the Creative Commons Attribution-ShareAlike License (CC BY-SA). 
Please ensure you adhere to Wikipedia's Terms of Use.
This project is licensed under the MIT License. You are free to use, modify, and distribute this project for educational purposes.
'''

import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_article(topic):
    try:
        # Step 1: Format the Wikipedia URL for the given topic
        base_url = "https://en.wikipedia.org/wiki/"
        url = base_url + topic.replace(" ", "_")
        
        # Step 2: Send an HTTP GET request to the Wikipedia page
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to fetch the article. Status Code:", response.status_code)
            return
        
        # Step 3: Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Step 4: Extract the title and the first meaningful paragraph
        title = soup.find("h1", {"id": "firstHeading"}).text
        paragraphs = soup.find_all("p")
        
        # Find the first non-empty paragraph
        for paragraph in paragraphs:
            if paragraph.text.strip():
                summary = paragraph.text.strip()
                break
        else:
            summary = "No meaningful summary found."

        # Step 5: Display the results
        print(f"Title: {title}\n")
        print(f"Summary: {summary}\n")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Starter UI to test the scraper
if __name__ == "__main__":
    print("Wikipedia Article Summary Scraper")
    topic = input("Enter a topic to search (e.g., Sabrina Carpenter): ")
    scrape_wikipedia_article(topic)
