import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/readable_eq_data.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
eq_fileinfo_dic = all_eq_data['metadata']

title = eq_fileinfo_dic['title']
megs = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
hover_texts = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]

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
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
