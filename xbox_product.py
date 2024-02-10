import sys

import requests
import json

url = "https://cart.production.store-web.dynamics.com/cart/v1.0/cart/loadCart?cartType=consumer&appId=XboxWeb"

with open("xbox.txt", "r") as fp:
    data = fp.readlines()

product_id = data[0].strip().replace("product_id=", "")
friendly_name = data[1].strip().replace("friendly_name=", "")

payload = json.dumps({
  "market": "AR",
  "locale": "es-AR",
  "riskSessionId": "289a7dc9-c32e-4879-a76d-b4f849a600d3",
  "catalogClientType": "storeWeb",
  "clientContext": {
    "client": "XboxCom",
    "deviceFamily": "web"
  },
  "friendlyName": friendly_name,
  "itemsToAdd": {
    "items": [
      {
        "productId": product_id,
        "skuId": "0010",
        "availabilityId": "B4C3NDSG0WT9",
        "quantity": 1,
        "campaignId": "xboxcomct"
      }
    ]
  }
})

headers = {
  'authority': 'cart.production.store-web.dynamics.com',
  'accept': '*/*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'content-type': 'application/json',
  'ms-cv': 'vOEyD61xEHGDdX7Au9cObH.25',
  'origin': 'https://www.xbox.com',
  'referer': 'https://www.xbox.com/',
  'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/121.0.0.0 Safari/537.36',
  'x-authorization-muid': '9D154A4427E7423FA4CA4CD995AE4ED5',
  'x-ms-vector-id': '5A0EF167E65F5525B16304799771CD8814D5B86757CFAEED48FCB10F43DAE238',
  'x-validation-field-1': '9p6pwp9q367c'
}

print("Sending request to xbox api..")
response = requests.request("PUT", url, headers=headers, data=payload)
print(f"request sent with productID {product_id} and friendly name {friendly_name} successfully, "
      f"received response {response.status_code}")
