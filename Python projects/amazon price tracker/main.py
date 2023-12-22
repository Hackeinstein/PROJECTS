import requests

from bs4 import BeautifulSoup

res=requests.get("https://www.amazon.sa/-/en/gp/product/B07Y9Y69N7/ref=ox_sc_saved_image_1?smid=A13DHZ48BFXWO4&psc=1")

soup=BeautifulSoup(res.text,"html.parser")

print(soup.prettify())

get_price=soup.select_one(".a-price-whole").text

whole_price=get_price.split(".")[0]

print(whole_price) 