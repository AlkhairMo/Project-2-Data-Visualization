import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2021_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    headers = {}
    for index, column in enumerate(header_row):
        headers[column] = index

    # Get date, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[headers['DATE']], '%Y-%m-%d')
        try:
            high = int(row[headers['TMAX']])
            low = int(row[headers['TMIN']])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)
    station = row[headers['NAME']]

# Plot the high and low temperatures.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=0.8, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=0.8, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title(f"Daily high and low temperatures - 2021\n{station}", fontsize=13)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylim(5, 135)

plt.show()
