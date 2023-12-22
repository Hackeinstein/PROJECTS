import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/b4ea4ccf4b1db3a09ad367f5248decfc/copyOfFlightDeals/prices"

    def get_data(self) -> list:
        response = requests.get(url=self.url)
        data = response.json()
        return data["prices"]

    def update_record(self, data: dict):
        url = f"{self.url}/{data['id']}"
        params = {
            "price": {
                "city": data['city'],
                "iataCode": data['iataCode'],
                "lowestPrice": data['lowestPrice']
            }
        }
        response = requests.put(url=url, json=params)
        return response
