import requests
from bs4 import BeautifulSoup 


def scraping_book():
  url = "h ttp://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
  response = requests.get(url)
  if response.ok:
      soup = BeautifulSoup(response.content, "html.parser")
      title = soup.find("div", {"class": "col-sm-6 product_main"}).find("h1")
      print(title.text)