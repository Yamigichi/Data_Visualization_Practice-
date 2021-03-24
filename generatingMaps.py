import numpy as np
import pandas as pd

#install folium
!conda install -c conda-forge folium=0.5.0 --yes
import folium
#print('Folium installed and imported!')
# define the world map
world_map = folium.Map()
# display world map
world_map
