import pandas as pd
import folium
import os

arquivo3 = open('rotas.txt')

temp = arquivo3.readline()
print(temp[3] + temp[4] + temp[5])
print(temp[7] + temp[8] + temp[9])