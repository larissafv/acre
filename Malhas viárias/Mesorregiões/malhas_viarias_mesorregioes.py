#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import matplotlib

malhas_viarias_mesorregioes = gpd.read_file ("/home/pedro/Área de Trabalho/Mesorregioes/BR_Mesorregioes_2019.shp")

malhas_viarias_mesorregioes.plot()


# In[ ]:




