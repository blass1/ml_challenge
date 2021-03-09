import logging
import requests
import json

# API INFO
url = "https://api.mercadolibre.com"
site_id = "MLA"

url_categoryid = url + "/categories/" + site + category_id


# Creador del registro LOG
logging.basicConfig(
    level=logging.DEBUG,
    format='%(message)s',
    datefmt='%H:%M:%S',
    filename='log_user.txt'
)

seller_id="179571326"
site_id="MLA"

seller_items = {
    "items":[{
        "id":1,
        "title":"Bufanda",
        "category_id":777
    },
    {
        "id":2,
        "title":"Lavadora",
        "category_id":888}]
}

for item in seller_items:
    logging.info(f"Id: {item.id} - Title: {item.title} - Category Id: {item.category_id}")