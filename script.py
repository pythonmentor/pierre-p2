import requests
from bs4 import BeautifulSoup 


def scraping_book():
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one('.product_main h1')      # remplace find("div", {"class": "col-sm-6 product_main"}).find("h1")
        print(title.text)
        product_description(soup)

      
def product_description(soup):
  description = soup.select_one('.sub-header ~ p')
  print(description.text)
