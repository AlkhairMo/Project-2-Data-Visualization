import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[3])
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', linewidth=0.8, alpha=0.5)
ax.plot(dates, lows, c='blue', linewidth=0.8, alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2021\nDeath Valley, CA", fontsize=14)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)
plt.ylim(5, 135)

plt.show()
