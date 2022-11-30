import pandas as pd
import folium

arquivo = open('saida.txt')

county = int(0)
countx = int(0)
countz = int(0)

fhand = open('saida.txt') 
linhas = 0
for line in fhand:
    linhas = linhas + 1

arquivo.seek(0)

z = list(range(linhas))
y = list(range(linhas))
x = list(range(linhas))

for n in z:
    temp = arquivo.readline()
    if('z' in temp):
        z[countz] = temp[2] + temp[3]
        countz = countz + 1

arquivo.seek(0)

for n in y:
    temp = arquivo.readline()
    if('y' in temp):
        y[county] = temp[2] + temp[3]
        county = county + 1

arquivo.seek(0)

for n in x:
    temp = arquivo.readline()
    if('x' in temp):
        x[countx] = temp[2] + temp[3] + temp[5] + temp[6]
        countx = countx + 1

arquivo.seek(0)

print('Os hubs serão: ')
for n in range(0,county):
    print(y[n])

print('Os gateways serão: ')
for n in range(0,countz):
    print(z[n])

print('As conexoes serão: ')
for n in range(0,countx):
    print(x[n])

aeroportos = pd.read_excel('arquivos/aeroportos.xlsx')

mapa = folium.Map(location=[-19.916667,-43.933333])


for index, l_aeroportos in aeroportos.iterrows():
    
    for n in range(0,county):

        if int(l_aeroportos['ID']) == int(y[n]):
            folium.Marker(
            [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
            tooltip=l_aeroportos['LOCAL'],
            icon=folium.Icon(color='red', icon = 'home')
            ).add_to(mapa)

    for n in range(0,countz):

        if int(l_aeroportos['ID']) == int(z[n]):
            folium.Marker(
            [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
            tooltip=l_aeroportos['LOCAL'],
            icon=folium.Icon(color='green', icon = 'cloud')
            ).add_to(mapa)

mapa.save('aeroportos.html')


            




