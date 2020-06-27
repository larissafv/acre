from geobr import read_micro_region

# Micro regiões do Brasil
microBR = read_micro_region(code_micro='all', year=2010)
print(microBR)

# Micro regiões em Minas Gerais
microMG = read_micro_region(code_micro='MG', year=2010)
print(microMG)