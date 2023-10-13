# with open("weather_data.csv") as file:
#     data = file.readlines()


# import csv
# with open("weather.csv") as file:
#     data = csv.reader(file)
#     temperature =[]
#     for row in data:
#         if row[1] != "temp":
#            temperature.append(row[1])
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather.csv")
# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
#
max = data['temp'].max()
# print(max)

# fetch row
# print(data[data.day=="Monday"])

# print(data[data.temp==max])

monday = data[data.day == "Monday"]
temp = (monday["temp"] * (9 / 5)) + 32
print(temp)
