import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        dates.append(date)
        highs.append(high)

# Plot the high temperatures.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2021", fontsize=18)
plt.xlabel('', fontsize=13)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.show()
