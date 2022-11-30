import math
import pandas as pd
from math import sin, cos, sqrt, atan2, radians,e

R = float(6371.0)
distancia = float(99999999999999999)
dtemp = float(0)
aeroporto = str(' ')
w = float(0)
maiornumero= int(0)
countcomum = int(0)
counthub = int(0)
countgateway = int(0)

aeroportos1 = pd.read_excel('arquivos/entrada.xlsx')
aeroportos2 = pd.read_excel('arquivos/entrada.xlsx')
contagem = pd.read_excel('arquivos/entrada.xlsx')

arquivo = open('arquivos/saida.txt','w')


for index, l_contagem in contagem.iterrows():
    if (str(l_contagem['CANDIDATO']) == 'COMUM'):
        countcomum = countcomum + 1
    
    if (str(l_contagem['CANDIDATO']) == 'HUB'):
        counthub = counthub + 1
    
    if (str(l_contagem['CANDIDATO']) == 'GATEWAY'):
        countgateway = countgateway + 1

arquivo.write(str(countcomum))
arquivo.write('\n')
arquivo.write(str(counthub))
arquivo.write('\n')
arquivo.write(str(countgateway))
arquivo.write('\n')

for index, l_aeroportos in aeroportos1.iterrows():
    arquivo.write(l_aeroportos['ID_REGIAO'])
    arquivo.write('\t')
    arquivo.write(l_aeroportos['ID_AEROPORTO'])
    arquivo.write('\t')
    arquivo.write(l_aeroportos['LATITUDE'])
    arquivo.write('\t')
    arquivo.write(l_aeroportos['LONGITUDE'])
    arquivo.write('\n')

arquivo.write('\n')

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

        w = l1_aeroportos['POPULACAO'] * l2_aeroportos['POPULACAO'] * l1_aeroportos['PIB'] * l2_aeroportos['PIB'] * e**(-0.01*dtemp)

        if dlon == 0 and dlat == 0:
            w=0
        
        if dtemp < 300:
            w=0

        arquivo.write('{:.4f}\t'.format(w))

    
    arquivo.write('\n')

arquivo.write('\n')

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

        w = l1_aeroportos['POPULACAO'] * l2_aeroportos['POPULACAO'] * l1_aeroportos['PIB'] * l2_aeroportos['PIB'] * e**(-0.01*dtemp)

        if dlon == 0 and dlat == 0:
            w=0
        
        if dtemp < 300:
            w=0

        arquivo.write('{:.4f}\t'.format(dtemp))

    
    arquivo.write('\n')

arquivo.close()