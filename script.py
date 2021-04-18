import requests
from bs4 import BeautifulSoup 


def scraping_book():
    url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.select_one('.product_main h1').text      # remplace find("div", {"class": "col-sm-6 product_main"}).find("h1")
        print(title)
        description = product_description(soup)
        category = product_category(soup)
        upc = product_upc(soup)

     
def product_description(soup):
  description = soup.select_one('.sub-header ~ p').text
  print(description)
  return description

def product_category(soup):
  category = soup.select('.breadcrumb li')[-2].text
  print(category)
  return category

def product_upc(soup):
  upc = soup.select('table',{'table-striped' : 'td'})
  print(upc)
  return upc