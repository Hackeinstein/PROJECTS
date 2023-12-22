import requests
import datetime

TOKEN = "steinapi2023"
USERNAME = "hackeinstein"
GRAPHID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": "hackeinstein",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPHID,
    "name": "Cycling Graph",
    "unit": "Km",
    "color": "momiji",
    "type": "float"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, headers=headers, json=config)
#
# print(response.text)

date = datetime.datetime.now().strftime("%Y%m%d")
pixel_endpoint = f"{graph_endpoint}/{GRAPHID}"
pixel_config = {
    "date": date,
    "quantity": "300.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

put_pixel_endpoint = f"{pixel_endpoint}/{date}"
put_config = {
    "quantity": "90.5",
}
response = requests.put(url=put_pixel_endpoint, json=put_config, headers=headers)
print(response.text)
