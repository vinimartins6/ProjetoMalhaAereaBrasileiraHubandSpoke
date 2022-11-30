import pandas as pd
import folium
import os

aeroportos = pd.read_excel('arquivos/aeroportos_entrada_anac - Copy.xlsx')
aeroportos2 = pd.read_excel('arquivos/aeroportos_entrada_anac - Copy.xlsx')


mapa = folium.Map( location=[-15.77972, -47.92972], tiles = 'stamentoner')

    

for index, l_aeroportos in aeroportos.iterrows():
            
    folium.RegularPolygonMarker(
    [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
    tooltip=l_aeroportos['AEROPORTO'],
    color = 'green',
    fill_color='#008000',
    number_of_sides=99,
    radius=6
    ).add_to(mapa)
    print(l_aeroportos['ID'])

mapa.save('mapa2.html')

for index, l_aeroportos in aeroportos.iterrows():
    print(l_aeroportos['ID'])
    for index, l2_aeroportos in aeroportos2.iterrows():
                            
        folium.PolyLine([(l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']), (l2_aeroportos['LATITUDE'],l2_aeroportos['LONGITUDE'])],
        color='#000000',
        weight=1,
        opacity=1).add_to(mapa)

mapa.save('mapa3.html')