import requests
from bs4 import BeautifulSoup as b4 

url = "https://portal.weloveshopping.com/product/L90302979"
web_data = requests.get(url)

# print(web_data.text)
soup = b4(web_data.text,features='html.parser')
find_word = soup.find_all("div",{"class":"shop-detail"})
name = []
for i in find_word:
   na = i.span.get_text(strip=True)
   name.append(na)
print(name)