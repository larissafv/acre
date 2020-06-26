#!/usr/bin/env python
# coding: utf-8

# In[2]:


import geopandas as gpd
import matplotlib


# In[3]:


malhas_viarias_municipios = gpd.read_file("/home/pedro/Área de Trabalho/Municipios/BR_Municipios_2019.shp")

malhas_viarias_municipios.plot()


# In[ ]:




