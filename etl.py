import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.title.string)
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
print(descriptions)
