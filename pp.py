import io
import base64
import pandas as pd
import geopandas as gpd  
import matplotlib.pyplot as plt


caminho_mapa = r'C:\Users\USER\OneDrive\Desktop\rj\Recorte JL.shp' 


geo_df = gpd.read_file(caminho_mapa)


fig, ax = plt.subplots(figsize=(10,8))
geo_df.plot(ax=ax, color='silver', edgecolor='black', linewidth=0.3)
ax.axis('off')


buf = io.BytesIO()
plt.savefig(buf, format='png', bbox_inches='tight')
buf.seek(0)
base64_str = base64.b64encode(buf.read()).decode('utf-8')
plt.close()

html_resultado = f'<img src="data:image/png;base64,{base64_str}" style="width:100%; max-width:800px;"/>'


df_final = pd.DataFrame({'Codigo_HTML': [html_resultado]})
