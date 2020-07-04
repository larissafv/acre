
#Para imprimir tabela ou plotar mapa, tirar comentário de um dos últimos dois comandos

import geopandas as gpd
import pandas as pd
import matplotlib

pop07 = pd.read_csv("2007.csv",sep = ";")
pop07["GEOCODIG_M"] = pop07["COD_UF"]*100000 + pop07["COD_MN"]

br07 = gpd.read_file("shp/55mu2500psd.shp")

mapa = br07.merge(pop07, on = "GEOCODIG_M")

#Ver  tabela
#print(mapa)

#Plotar o mapa
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True, legend_kwds={'label': "População Estimada em 2007", 'orientation': "horizontal"})
