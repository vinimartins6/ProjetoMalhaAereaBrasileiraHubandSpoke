import math
import pandas as pd
from math import sin, cos, sqrt, atan2, radians,e

R = float(6371.0)
distancia = float(99999999999999999)
dtemp = float(0)
aeroporto = str(' ')
w = float(0)
count = int(0)

aeroportos1 = pd.read_excel('arquivos/aeroportos_entrada_anac.xlsx')
aeroportos2 = pd.read_excel('arquivos/aeroportos_entrada_anac.xlsx')

colunas = ['ID_AEROPORTO_1','AEROPORTO_1','CLASSE_1','ID_AEROPORTO_2','AEROPORTO_2','CLASSE_2','DISTANCIA']
matriz = pd.DataFrame(columns=colunas)


for index, l1_aeroportos in aeroportos1.iterrows():
    for index, l2_aeroportos in aeroportos2.iterrows():
               
        lat1 = radians(l1_aeroportos['LATITUDE'])
        lon1 = radians(l1_aeroportos['LONGITUDE'])
        lat2 = radians(l2_aeroportos['LATITUDE'])
        lon2 = radians(l2_aeroportos['LONGITUDE'])
 
        dlon = lon2 - lon1
        dlat = lat2 - lat1
 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
 
        dtemp = R * c

        if dtemp < 60 and dtemp > 0:
            info_temp = [l1_aeroportos['ID'],l1_aeroportos['AEROPORTO'],l1_aeroportos['classe'],l2_aeroportos['ID'], l2_aeroportos['AEROPORTO'],l2_aeroportos['classe'],dtemp]
            temp2 = pd.DataFrame([info_temp], columns=colunas)
            matriz = matriz.append(temp2, ignore_index=True)

        

escrever = pd.ExcelWriter('arquivos/distancia60km_excel.xlsx') # pylint: disable=abstract-class-instantiated
matriz.to_excel(escrever, 'DADOS', index=False)
escrever.save()