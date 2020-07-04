
#Para imprimir tabela ou plotar mapa, tirar comentário de um dos últimos dois comandos

import geopandas as gpd
import pandas as pd
import matplotlib

pop08 = pd.read_csv("2008.csv",sep = ";")
pop08["GEOCODIG_M"] = pop08["COD_UF"]*100000 + pop08["COD_MN"]

br08 = gpd.read_file("shp/55mu2500psd.shp")

mapa = br08.merge(pop08, on = "GEOCODIG_M")

#Ver  tabela
#print(mapa)

#Plotar o mapa
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True, legend_kwds={'label': "População Estimada em 2008", 'orientation': "horizontal"})
