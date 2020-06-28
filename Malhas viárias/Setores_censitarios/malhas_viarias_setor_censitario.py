from geobr import read_census_tract
import matplotlib.pyplot as plt

# regiões censitárias do Brasil
censiBR = read_census_tract(code_tract='all', year=2010)
censiBR.plot()

# regiões censitárias em Minas Gerais
censiMG = read_census_tract(code_tract='MG', year=2010)
censiMG.plot()

# regiões censitárias de BH
censiBH = read_census_tract(code_tract=3106200, year=2010)
censiBH.plot()
plt.show()