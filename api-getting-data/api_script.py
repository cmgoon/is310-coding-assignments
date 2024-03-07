import requests
import apikey
import json

api_key = apikey.load("api_key")
url = 'https://api.spoonacular.com/food/products/search?query=yogurt&apiKey='

response = requests.get(url + api_key)
#print(response.json())
api_data = response.json()
with open('spoonacular.json', 'w') as f:
    json.dump(api_data, f)