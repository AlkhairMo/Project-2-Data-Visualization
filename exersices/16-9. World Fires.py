import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = '../data/world_fires_7_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    headers = {}
    for index, column in enumerate(header_row):
        headers[column] = index

    lats, lons, brts, dates = [], [], [], []
    for row in reader:
        lat = row[headers['latitude']]
        lon = row[headers['longitude']]
        brt = row[headers['brightness']]
        date = row[headers['acq_date']]
        lats.append(float(lat))
        lons.append(float(lon))
        brts.append(float(brt))
        dates.append(date)
    first_date = dates[0]
    last_date = dates[-1]
    if first_date == last_date:
        date_info = f'in {first_date}'
    else:
        date_info = f'between {first_date} and {last_date}'

data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'marker': {
             'color': brts,
             'colorscale': 'Hot',
             'reversescale': True,
             'colorbar': {
                 'title': 'brightness'
             },
         },
         }]
my_layout = Layout(title=f"World Fires {date_info}")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
