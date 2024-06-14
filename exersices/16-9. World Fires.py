import csv

from plotly.graph_objs import Layout
from plotly import offline

filename = '../data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    headers = {}
    for index, column in enumerate(header_row):
        headers[column] = index

    lats, lons, brts = [], [], []
    for row in reader:
        lat = row[headers['latitude']]
        lon = row[headers['longitude']]
        brt = row[headers['brightness']]
        lats.append(float(lat))
        lons.append(float(lon))
        brts.append(float(brt))

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
my_layout = Layout(title=f"World Fires in {row[headers['acq_date']]}")
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
