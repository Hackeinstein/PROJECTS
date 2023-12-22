# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

sheet_data = DataManager().get_data()

# sheet_data = FlightSearch().get_iata_code(sheet_data)
#
# print(sheet_data)

# for row in sheet_data:
#     DataManager().update_record(row)

for row in sheet_data:
    try:
        price = FlightData("LON", "GBP").get_price(row)
        print(f"{row['city']}: E: {price}")
    except Exception as e:
        print("No cheaper flight")
