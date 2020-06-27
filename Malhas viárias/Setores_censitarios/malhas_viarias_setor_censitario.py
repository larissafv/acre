from geobr import read_census_tract

# regiões censitárias do Brasil
censiBR = read_census_tract(code_tract='all', year=2010)
print(censiBR)

# regiões censitárias em Minas Gerais
censiMG = read_census_tract(code_tract='MG', year=2010)
print(censiMG)

# regiões censitárias de BH
censiBH = read_census_tract(code_tract=3106200, year=2010)
print(censiBH)