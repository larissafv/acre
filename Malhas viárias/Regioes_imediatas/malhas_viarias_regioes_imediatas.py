from geobr import read_immediate_region
import matplotlib.pyplot as plt

imedBR = read_immediate_region(code_immediate='all', year=2017)
imedBR.plot()

imedMG = read_immediate_region(code_immediate='MG', year=2017)
imedMG.plot(edgecolor='black')

plt.show()
