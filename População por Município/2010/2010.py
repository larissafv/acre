
#Para imprimir tabela ou plotar mapa, tirar comentário de um dos últimos dois comandos

import geopandas as gpd
import pandas as pd
import matplotlib

pop10 = pd.read_csv("2010.csv", sep = ";")

ac = gpd.read_file("shp/ac/12MUE250GC_SIR.shp")
al = gpd.read_file("shp/al/27MUE250GC_SIR.shp")
am = gpd.read_file("shp/am/13MUE250GC_SIR.shp")
ap = gpd.read_file("shp/ap/16MUE250GC_SIR.shp")
ba = gpd.read_file("shp/ba/29MUE250GC_SIR.shp")
ce = gpd.read_file("shp/ce/23MUE250GC_SIR.shp")
df = gpd.read_file("shp/df/53MUE250GC_SIR.shp")
es = gpd.read_file("shp/es/32MUE250GC_SIR.shp")
go = gpd.read_file("shp/go/52MUE250GC_SIR.shp")
ma = gpd.read_file("shp/ma/21MUE250GC_SIR.shp")
mg = gpd.read_file("shp/mg/31MUE250GC_SIR.shp")
ms = gpd.read_file("shp/ms/50MUE250GC_SIR.shp")
mt = gpd.read_file("shp/mt/51MUE250GC_SIR.shp")
pa = gpd.read_file("shp/pa/15MUE250GC_SIR.shp")
pb = gpd.read_file("shp/pb/25MUE250GC_SIR.shp")
pe = gpd.read_file("shp/pe/26MUE250GC_SIR.shp")
pi = gpd.read_file("shp/pi/22MUE250GC_SIR.shp")
pr = gpd.read_file("shp/pr/41MUE250GC_SIR.shp")
rj = gpd.read_file("shp/rj/33MUE250GC_SIR.shp")
rn = gpd.read_file("shp/rn/24MUE250GC_SIR.shp")
ro = gpd.read_file("shp/ro/11MUE250GC_SIR.shp")
rr = gpd.read_file("shp/rr/14MUE250GC_SIR.shp")
rs = gpd.read_file("shp/rs/43MUE250GC_SIR.shp")
sc = gpd.read_file("shp/sc/42MUE250GC_SIR.shp")
se = gpd.read_file("shp/se/28MUE250GC_SIR.shp")
sp = gpd.read_file("shp/sp/35MUE250GC_SIR.shp")
to = gpd.read_file("shp/to/17MUE250GC_SIR.shp")

br10 = ac.append(al)
br10 = br10.append(am)
br10 = br10.append(ap)
br10 = br10.append(ba)
br10 = br10.append(ce)
br10 = br10.append(df)
br10 = br10.append(es)
br10 = br10.append(go)
br10 = br10.append(ma)
br10 = br10.append(mg)
br10 = br10.append(ms)
br10 = br10.append(mt)
br10 = br10.append(pa)
br10 = br10.append(pb)
br10 = br10.append(pe)
br10 = br10.append(pi)
br10 = br10.append(pr)
br10 = br10.append(rj)
br10 = br10.append(rn)
br10 = br10.append(ro)
br10 = br10.append(rr)
br10 = br10.append(rs)
br10 = br10.append(sc)
br10 = br10.append(se)
br10 = br10.append(sp)
br10 = br10.append(to)
br10["CD_GEOCODM"] = pd.to_numeric(br10["CD_GEOCODM"])

mapa = br10.merge(pop10, on = "CD_GEOCODM")

#Ver  tabela
#print(mapa)

#Plotar o mapa
#mapa.plot(column = "POP_ESTIM", figsize = (20,20), legend = True, legend_kwds={'label': "População Estimada em 2010", 'orientation': "horizontal"})
