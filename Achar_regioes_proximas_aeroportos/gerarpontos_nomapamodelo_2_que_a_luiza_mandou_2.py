import pandas as pd
import folium
import os

temp = ''
temp1 = ''
temp2 = ''
pasta = 1

while pasta <= 30:

    arquivo1 = open('Resultados-v1[1361]/'+str(pasta)+'/hubs.txt')
    arquivo2 = open('Resultados-v1[1361]/'+str(pasta)+'/gateways.txt')
    arquivo3 = open('Resultados-v1[1361]/'+str(pasta)+'/rotas.txt')
    arquivo4 = open('Resultados-v1[1361]/'+str(pasta)+'/rotas2.txt')

    aeroportos = pd.read_excel('arquivos/aeroportos_entrada_anac.xlsx')
    aeroportos2 = pd.read_excel('arquivos/hubs.xlsx')
    aeroportos3 = pd.read_excel('arquivos/hubs.xlsx')


    mapa = folium.Map( location=[-15.77972, -47.92972], tiles = 'stamentoner')

    linhas  =   sum(1 for linha in arquivo3)
    arquivo3.seek(0)

    for index, l_aeroportos in aeroportos2.iterrows():
        for index, l2_aeroportos in aeroportos3.iterrows():
            for n in range(0,linhas):
                temp = arquivo3.readline()
                temp1= temp[3] + temp[4] + temp[5]
                temp2 = temp[7] + temp[8] + temp[9]
                if (int(l_aeroportos['ID']) == int(temp1)) and (int(l2_aeroportos['ID']) == int(temp2)):
                    folium.PolyLine([(l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']), (l2_aeroportos['LATITUDE'],l2_aeroportos['LONGITUDE'])],
                    color='#008000',
                    weight=2,
                    opacity=1).add_to(mapa)
            arquivo3.seek(0)

    linhas  =   sum(1 for linha in arquivo4)
    arquivo4.seek(0)

    for index, l_aeroportos in aeroportos2.iterrows():
        for index, l2_aeroportos in aeroportos3.iterrows():
            for n in range(0,linhas):
                temp = arquivo4.readline()
                temp1= temp[3] + temp[4] + temp[5]
                temp2 = temp[7] + temp[8] + temp[9]
                if (int(l_aeroportos['ID']) == int(temp1)) and (int(l2_aeroportos['ID']) == int(temp2)):
                    folium.PolyLine([(l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']), (l2_aeroportos['LATITUDE'],l2_aeroportos['LONGITUDE'])],
                    color='#ff0000',
                    weight=2,
                    opacity=1).add_to(mapa)
            arquivo4.seek(0)
    
    linhas  =   sum(1 for linha in arquivo1)
    arquivo1.seek(0)

    for index, l_aeroportos in aeroportos.iterrows():
    
        for n in range(0,linhas):

            if int(l_aeroportos['ID']) == int(arquivo1.readline()):
                folium.RegularPolygonMarker(
                    [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
                    tooltip=l_aeroportos['AEROPORTO'],
                    color = 'green',
                    fill_color='#0000ff',
                    number_of_sides=3,
                    radius=6
                ).add_to(mapa)
    
        arquivo1.seek(0)

    linhas  =   sum(1 for linha in arquivo2)
    arquivo2.seek(0)

    for index, l_aeroportos in aeroportos.iterrows():
   
        for n in range(0,linhas):

            if int(l_aeroportos['ID']) == int(arquivo2.readline()):
                folium.RegularPolygonMarker(
                    [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
                    tooltip=l_aeroportos['AEROPORTO'],
                    color = 'red',
                    fill_color='#008000',
                    number_of_sides=25,
                    radius=5
                ).add_to(mapa)
    
        arquivo2.seek(0)




    print('PASTA'+str(pasta))
    mapa.save('Resultados-v1[1361]/aeroportos'+str(pasta)+'.html')
    pasta = pasta + 1


            




