import geopandas as gpd
import matplotlib.pyplot as plt

intermed = gpd.read_file('C:\\Users\\rafae\\OneDrive\\Desktop\\trabalhos\\cda\\Acre\\Malhas viárias\\Regioes_intermediarias\\BR_RG_Intermediarias_2019.shp')

intermed.plot(edgecolor='black')
plt.show()
