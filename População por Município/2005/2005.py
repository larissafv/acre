import pandas as pd
import geopandas as gpd
import matplotlib

pop05 = pd.read_csv("2005.csv",sep = ";")
pop05["Codmun6"] = pop05["COD_UF"]*10000 + pop05["COD_MN"]

br05 = gpd.read_file("shp/55mu2500pc.shp")

trans_cod = pd.read_csv('cod00.csv', sep =";")
br05 = br05.merge(trans_cod, on = "GEOCODIGO")

mapa = br05.merge(pop05, on = "Codmun6")

#Ver dados
#print(mapa)

#Plotar
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True)