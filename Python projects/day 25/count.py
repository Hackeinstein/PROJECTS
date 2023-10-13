import pandas

data = pandas.read_csv("2018.csv")
# simple algorithm to collect colours in list and add to list
fur_color = data['Primary Fur Color'].to_list()
colors = []
for color in fur_color:
    if colors.count(color)==0:
        colors.append(color)

# create a dictionary and cross info to it
colors_count = []
for color in colors:
    colors_count.append(fur_color.count(color))

new_df_data = {
    "Fur_Color": colors,
    "Count": colors_count
}


new_df = pandas.DataFrame(new_df_data)
data.to_csv("data.csv")


