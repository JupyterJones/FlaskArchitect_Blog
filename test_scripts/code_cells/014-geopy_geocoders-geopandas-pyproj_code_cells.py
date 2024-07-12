%matplotlib inline

# sphinx_gallery_thumbnail_number = 3
import geopandas

# sphinx_gallery_thumbnail_number = 3
import geopandas
geopandas.datasets.available

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
loc = geolocator.geocode("New York, NY")
loc


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
loc = geolocator.geocode("Eureka Springs, AR")
loc


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
loc = geolocator.geocode("Manila, PH")
loc

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-application")
loc = geolocator.geocode("Gaya Gaya, Bulacan")
loc

import geopandas
gdf = geopandas.read_file(geopandas.datasets.get_path("naturalearth_cities"))
gdf.crs

import pyproj
crs = pyproj.CRS("EPSG:31370")
crs

%matplotlib inline
import contextily as ctx
df = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = df.plot(figsize=(12, 12), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite, zoom=12)
ax.set_axis_off()


import contextily as ctx
df = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, zoom=12)

df = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
ax = df.plot(figsize=(16, 16), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, zoom=12)

df = geopandas.read_file(geopandas.datasets.get_path('nybb'))
ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')

df = df.to_crs(epsg=3857)

import contextily as ctx

ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax)

ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, zoom=12)

ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor='k')
ctx.add_basemap(ax, source=ctx.providers.Stamen.TonerLite)
ax.set_axis_off()



!pip install contextily

!pip install descartes

!pip install geopandas



