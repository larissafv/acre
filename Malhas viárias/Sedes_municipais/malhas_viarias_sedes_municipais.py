from geobr import read_municipal_seat
import matplotlib.pyplot as plt

sedes_municipais = read_municipal_seat(year=2010) 
sedes_municipais.plot(edgecolor='black')
plt.show()