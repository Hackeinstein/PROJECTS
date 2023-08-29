# with open("weather_data.csv") as file:
#     data = file.readlines()


import csv 
with open("weather.csv") as file:
    data = csv.reader(file)
    temperature =[]
    for row in data:
        if row[1] != "temp":
           temperature.append(row[1])

    print()