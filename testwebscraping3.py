import requests
from bs4 import BeautifulSoup as b4 

url = "https://www.ebay.com/itm/144353029865?_trkparms=%26rpp_cid%3D623976926e9668f2e34bcd42%26rpp_icid%3D623976926e9668f2e34bcd41&_trkparms=pageci%3A36aae677-b973-11ec-b90c-3a15c89609df%7Cparentrq%3A17c931661800a0a68aeb6785fffc5b36%7Ciid%3A2"
web_data = requests.get(url)

soup = b4(web_data.text,features='html.parser')
find_word = soup.find_all("span",{"class":"ux-textspans ux-textspans--PSEUDOLINK ux-textspans--BOLD"})

na = find_word[0].get_text(strip=True)
print(na)