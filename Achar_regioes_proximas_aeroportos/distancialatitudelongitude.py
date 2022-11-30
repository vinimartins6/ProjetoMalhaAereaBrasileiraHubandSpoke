import pandas as pd
from math import sin, cos, sqrt, atan2, radians

distancia = float(99999999999999999)
dtemp = float(0)
aeroporto = str(' ')
loading = int(0)
R = float(6371.0)

cidades = pd.read_excel('arquivos/cidades.xls')
aeroportos = pd.read_excel('arquivos/aeroportos_entrada_anac.xlsx')

colunas = ['CIDADE','UF', 'AEROPORTO','DISTÂNCIA']
matriz = pd.DataFrame(columns=colunas)

for index, l_cidades in cidades.iterrows():
    for index, l_aeroportos in aeroportos.iterrows():
        
        
        lat1 = radians(l_cidades['LATITUDE'])
        lon1 = radians(l_cidades['LONGITUDE'])
        lat2 = radians(l_aeroportos['LATITUDE'])
        lon2 = radians(l_aeroportos['LONGITUDE'])
 
        dlon = lon2 - lon1
        dlat = lat2 - lat1
 
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
 
        dtemp = R * c

        if dtemp < distancia:

            aeroporto = l_aeroportos['AEROPORTO']
            distancia = dtemp
    
    info_temp = [l_cidades['LOCAL'],l_cidades['UF'], aeroporto, distancia]
    temp2 = pd.DataFrame([info_temp], columns=colunas)
    matriz = matriz.append(temp2, ignore_index=True) 
   
    distancia = 9999999999
    aeroporto = ''

    loading = loading + 1
    print(loading)

escrever = pd.ExcelWriter('arquivos/saida.xlsx') # pylint: disable=abstract-class-instantiated
matriz.to_excel(escrever, 'DADOS', index=False)
escrever.save()





