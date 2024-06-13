import json

# Explore the structure of the data.
filename = 'data/readable_eq_data.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

megs, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    meg = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    megs.append(meg)
    lons.append(lon)
    lats.append(lat)

