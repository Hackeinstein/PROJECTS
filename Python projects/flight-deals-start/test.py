import requests
from pprint import pprint

url = "https://api.sheety.co/b4ea4ccf4b1db3a09ad367f5248decfc/copyOfFlightDeals/prices"
response = requests.get(url=url)
data= response.json()
print(data["prices"])
