from geobr import read_metro_area
import matplotlib.pyplot as plt

regioes_metropolitanasBR = read_metro_area(year=2018)
regioes_metropolitanasBR.plot(edgecolor='black', linewidth=0.3)
plt.show()