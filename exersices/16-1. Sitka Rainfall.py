import csv
from datetime import datetime

import matplotlib.pyplot as plt

with open("../data/sitka_weather_2021_full.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfall_amounts = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rainfall_amount = float(row[5])
        except ValueError:
            print(f'Missing data for {date}')
        else:
            dates.append(date)
            rainfall_amounts.append(rainfall_amount)


plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, rainfall_amounts, c='blue', linewidth=1)

plt.title("Rainfall Amounts in 2021 - Sitka, Alaska", fontsize=16)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()
plt.ylabel('Rainfall Amounts', fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.show()
