import geopandas as gpd
import folium
import pandas as pd
import branca as bc
import colormaps as cm
from mapclassify import classify 

path_sf = r'C:\Users\USER\OneDrive\Desktop\rj\Recorte JL.shp'
geo_df = gpd.read_file(path_sf)
geo_df.head()


import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(10,8))
geo_df.plot(ax=ax, color='silver', edgecolor='black', linewidth=0.3)
ax.axis('off')
plt.show();






geo_df.explore(tiles="Esri.WorldImagery")



meu_mapa = geo_df.explore(tiles="Esri.WorldImagery")
meu_mapa.save("index.html")

