import pandas as pd
import geopandas as gpd
import matplotlib

pop06 = pd.read_csv("2006.csv",sep = ";")
pop06["Codmun6"] = pop06["COD_UF"]*10000 + pop06["COD_MN"]

br06 = gpd.read_file("shp/55mu2500pc.shp")

trans_cod = pd.read_csv('cod00.csv', sep =";")
br06 = br06.merge(trans_cod, on = "GEOCODIGO")

mapa = br06.merge(pop06, on = "Codmun6")

#Ver dados
#print(mapa)

#Plotar
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True)