
#Para imprimir tabela ou plotar mapa, tirar comentário de um dos últimos dois comandos

import geopandas as gpd
import pandas as pd
import matplotlib

pop09 = pd.read_csv("2009.csv",sep = ";")
pop09["GEOCODIG_M"] = pop09["COD_UF"]*100000 + pop09["COD_MN"]

br09 = gpd.read_file("shp/55mu2500psd.shp")

mapa = br09.merge(pop09, on = "GEOCODIG_M")

#Ver  tabela
#print(mapa)

#Plotar o mapa
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True, legend_kwds={'label': "População Estimada em 2009", 'orientation': "horizontal"})
