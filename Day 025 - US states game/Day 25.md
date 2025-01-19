---
tags:
  - 100_Days_of_Code
  - programming
  - python
---
# Day 25: Working with CSV Data and the Pandas Library

## Notes

CSV (comma separated values) - represents tabular data

### CSV packange

inside `weather_data.csv`:

```csv
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```

```python
import csv

with open("weather_data.csv", mode="r") as data_file:
    data = csv.reader(data_file)

    for row in data:
        print(row)

# OUTPUT:

#day,temp,condition
#Monday,12,Sunny
#Tuesday,14,Rain
#Wednesday,15,Rain
#Thursday,14,Cloudy
#Friday,21,Sunny
#Saturday,22,Sunny
#Sunday,24,Sunny
```

### Pandas Library

a python data analysis package to perform tabular data.

```python
import pandas

data =pandas.read_csv("weather_data.csv")

print(type(data)) #pandas.core.frame.DataFrame 
print(type(data["temp"])) #pandas.core.series.Series
```

#### pandas.core.frame.DataFrame

- DataFrame - the whole entire table

#### pandas.core.series.Series

- Series - a single column in your table

#### Mean

```python

import pandas
data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

print(data["temp"].mean()) #17.428571428571427
```
