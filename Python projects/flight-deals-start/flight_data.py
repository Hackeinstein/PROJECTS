import requests
from datetime import datetime, timedelta


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, current_location: str, currency: str):
        self.current_location = current_location
        self.currency = currency

    def get_price(self, data: dict) -> int:
        url = "https://api.tequila.kiwi.com/v2/search"
        header = {
            "apikey": "WWjF3aaYGPTYlkakwHwU0t3ZdL2rIi61"
        }
        params = {
            "fly_from": self.current_location,
            "fly_to": data['iataCode'],
            "date_from": datetime.now().strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y"),
            "curr": self.currency,
            "price_to": data['lowestPrice'],
            "limit": 1,
        }
        response = requests.get(url=url, headers=header, params=params)
        data = response.json()
        return data['data'][0]['price']
