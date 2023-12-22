import requests

API_KEY = "WWjF3aaYGPTYlkakwHwU0t3ZdL2rIi61"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_iata_code(self, flights: list) -> list:
        url = "https://api.tequila.kiwi.com/locations/query"
        headers = {
            "apikey": API_KEY
        }
        for rows in flights:
            params = {
                "term": rows["city"],
                "locale":"en-US",
                "location_types":"city",
                "active_only":True
            }
            response = requests.get(url=url, headers=headers, params=params)
            data = response.json()
            rows['iataCode'] = data['locations'][0]['code']

        return flights

