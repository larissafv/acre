from geobr import read_micro_region
import matplotlib.pyplot as plt

# Micro regiões do Brasil
microBR = read_micro_region(code_micro='all', year=2010)
microBR.plot(edgecolor='black')

# Micro regiões em Minas Gerais
microMG = read_micro_region(code_micro='MG', year=2010)
microMG.plot(edgecolor='black')
plt.show()