import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

primary_fur_color = data["Primary Fur Color"]

colors = ["Gray", "Cinnamon", "Black"]
counts = []

for color in colors:
    counts.append(len(primary_fur_color[primary_fur_color == color]))

squirrel_dict = {
    "Fur Color": colors,
    "count": counts
}

squirrel_count = pandas.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")

## Angela's Method

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == 'Grey'])
# red_squirrels_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
# black_squirrels_count = len(data[data["Primary Fur Color"] == 'Black'])

# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")
