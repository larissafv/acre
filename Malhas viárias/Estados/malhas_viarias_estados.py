import geopandas as gpd
import matplotlib.pyplot as plt

malhas_viarias_estados = gpd.read_file("/BR_UF_2019.shp")

malhas_viarias_estados.plot()