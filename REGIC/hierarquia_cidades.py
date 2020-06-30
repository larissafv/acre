import geopandas as gpd
import matplotlib.pyplot as plt

mapa = gpd.read_file("data/REGIC2018_Cidades_poligono.shp")

mapa.plot(column="classe", figsize = (20,20), legend=True, cmap="YlGnBu")
