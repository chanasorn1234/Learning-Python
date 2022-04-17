import requests
from bs4 import BeautifulSoup as b4 
import time

url = "https://www.lazada.co.th/products/hatgogo-bucket-hat-i1044898930-s2326104258.html?spm=a2o4m.searchlist.list.1.73f91c16HY3e1s&search=1"
web_data = requests.get(url)
time.sleep(3)
# print(web_data.text)
soup = b4(web_data.text, features="html.parser")

find_word = soup.find_all("a",{"class":"pdp-link pdp-link_size_l pdp-link_theme_black seller-name__detail-name"})
# name = []
# for i in find_word:
#    na = i.get_text(strip=True)
#    name.append(na)
# print(name)
print([find_word[0].get_text(strip=True)])