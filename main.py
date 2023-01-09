import csv
import time
import json
import random
import datetime
from os import system

# Created module - Созданный модуль
from core.config import DOMEN, URL, HEADERS

# Downloaded libraries - Скаченные библиотеки
import requests
from bs4 import BeautifulSoup
count_site = int(input("Сколько страниц спарсить ?  "))

for count in range(1, count_site+1):
    response = requests.get(url = URL, headers = HEADERS, params={"page":f"page-{count}"})
    with open("core/html/index.html", "a", encoding="utf-8") as file:
        file.write(response.text)

# #-------------------------------------------------------------
for count in range(1, count_site+1):
    with open(f"core/html/index.html", "r") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'html.parser').find_all("div", class_="product-item-container")
    with open("core/html/index.html","w") as file :
        file.write(str(soup))
#---------------------------------------------------------------

with open("core/html/index.html", "r") as file:
    src = file.read()
soup = BeautifulSoup(src, "html.parser").find_all("a")
product_info = []
for item in soup:
    # item_price = item.get("new-product__price")
    item_url = DOMEN + item.get("href")
    name_product = item.get("data-name")
    category_product = item.get("data-category").replace("/",",")
    price_product = item.find("span", class_= "new-product__new-price").text.strip()
    # print(price_product.strip())
    # print( "ссылка ",item_url)
    # print("название", name_product)
    # print("категория", category_product)
    # print(f"цена  {price_product} \n")

    information = {
        "url": item_url,
        "name":name_product,
        "category": category_product,
        "new_price": price_product
    }
    product_info.append(information)

with open (f"core/json/name_with_price_dict.json", "w") as file:
    json.dump(product_info, file,indent=4, ensure_ascii=False)
#     print(item_price)
#     item_text = item.text
#     item_url = domen + item.get("href")
#     print(f'{item_text}:{item_url}')
#     all_categories_dict[item_text] = item_url

# new-product__price

# with open (f"core/json/name_with_price_dict.json", "w") as file:
#     json.dump(name_with_price_dict, file,indent=4, ensure_ascii=False)
#-----------------------------------------------------------
