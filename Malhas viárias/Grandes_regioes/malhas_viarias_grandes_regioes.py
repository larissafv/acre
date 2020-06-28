from geobr import read_region
import matplotlib.pyplot as plt

grandes_regioes = read_region(year=2010)
grandes_regioes.plot(edgecolor='black')
plt.show()
