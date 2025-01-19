

# with open("weather_data.csv", mode="r") as file:
#     temp = file.readlines()
#     data = []

#     for line in temp:
#         data.append(line.strip())
# print(data)


# import csv

# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))


# print(temperatures)

# import pandas
# data = pandas.read_csv("weather_data.csv")

# temperatures = data["temp"]

# print(data)
# print(temperatures)

# Get data in a row
# import pandas
# data = pandas.read_csv("weather_data.csv")

# monday = data[data.day == "Monday"]
# monday_temp_fahrenheit = (monday.temp[0] * (9/5)) + 32
# print(monday_temp_fahrenheit)


#Create a datafram from scratch
import pandas
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")

