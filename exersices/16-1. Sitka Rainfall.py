import csv
from datetime import datetime

import matplotlib.pyplot as plt

with open("../data/sitka_weather_2021_full.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    headers = {}
    for index, column in enumerate(header_row):
        headers[column] = index

    dates, rainfall_amounts = [], []
    for row in reader:
        date = datetime.strptime(row[headers['DATE']], '%Y-%m-%d')
        try:
            rainfall_amount = float(row[headers['PRCP']])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            rainfall_amounts.append(rainfall_amount)
    station = row[headers['NAME']]


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, rainfall_amounts, c='blue', linewidth=1)

plt.title(f"Rainfall Amounts in 2021 - \n{station}", fontsize=14)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()
plt.ylabel('Rainfall Amounts', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylim(-0.2, 3.0)

plt.show()
