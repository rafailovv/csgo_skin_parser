import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Pistol&category_730_Type%5B%5D=tag_CSGO_Type_SMG&category_730_Type%5B%5D=tag_CSGO_Type_Rifle&category_730_Type%5B%5D=tag_CSGO_Type_SniperRifle&category_730_Type%5B%5D=tag_CSGO_Type_Shotgun&category_730_Type%5B%5D=tag_CSGO_Type_Machinegun&category_730_Type%5B%5D=tag_CSGO_Type_Knife&category_730_Type%5B%5D=tag_Type_Hands&appid=730')
soup = BeautifulSoup(response.content, 'html.parser')


products_div = soup.select('.market_listing_row')
products = {}

for i in range(len(products_div)):
    product = []

    id = str(products_div[i]['id'])[len(products_div[i]['id'])-1]
    title = str((soup.select('.market_listing_item_name'))[i].get_text())
    number = str((soup.select('.market_listing_num_listings_qty'))[i].get_text())
    price = str((soup.select('.sale_price'))[i].get_text())

    product.append(title)
    product.append(number)
    product.append(price)
    products[id] = product

with open('db.json', 'w') as outfile:
    json.dump(products, outfile)