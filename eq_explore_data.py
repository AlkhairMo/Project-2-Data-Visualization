import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/readable_eq_data.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

megs, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    meg = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    megs.append(meg)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# Map the earthquakes
data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_texts,
         'marker': {
             'size': [3*meg for meg in megs],
             'color': megs,
             'colorscale': 'Hot',
             'reversescale': True,
             'colorbar': {'title': 'Magnitude'},
         },
         }]
my_layout = Layout(title="Global Earthquakes")

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
