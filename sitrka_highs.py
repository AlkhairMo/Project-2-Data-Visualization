import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2021_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file.
    highs = [int(row[4]) for row in reader]

# Plot the high temperatures.
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format plot.
plt.title("Daily high temperatures, July 2021", fontsize=18)
plt.xlabel('', fontsize=13)
plt.ylabel("Temperature (F)", fontsize=13)
plt.tick_params(axis='both', which='major', labelsize=13)

plt.show()
