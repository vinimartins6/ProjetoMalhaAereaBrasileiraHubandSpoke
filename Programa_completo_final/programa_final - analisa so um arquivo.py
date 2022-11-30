import numpy as np
import pandas as pd
import folium
import os

temp = ''
temp1 = ''
temp2 = ''
temp3=0
teste=''
temp_hub=0
temp_gateway=0

aeroportos = pd.read_excel('arquivos de entrada/aeroportos_entrada_anac.xlsx')
aeroportos2 = pd.read_excel('arquivos de entrada/hubs.xlsx')
aeroportos3 = pd.read_excel('arquivos de entrada/hubs.xlsx')
demanda = pd.read_excel('arquivos de entrada/demanda.xlsx')

n=0
i=0
j=0
linha_hubs=0
linha_fluxo=0
linha_gateways=0
linha_intergateways=0
qtd_interhubs=0
qtd_intergateways=0
inter_gateways=''
inter_hubs=''
count=0
fluxo_direto=0
fluxo_hub=0
fluxo_gateway=0

arquivo = open('arquivos de entrada/1.txt', 'r')
saida = open('arquivos de saida/saida.txt', 'w')

linhas  =   sum(1 for linha in arquivo)
arquivo.seek(0)

for n in range(0,linhas):
    temp = arquivo.readline()
    if temp != '\n':
        if str(temp[1]) == 'H':
            qtd_interhubs = qtd_interhubs + 1
        if str(temp[1]) == 'G':
            qtd_intergateways = qtd_intergateways + 1
        if str(temp[0]) == 'H':
            linha_hubs = count+1
        if str(temp[0]) == 'G':
            linha_gateways = count+1
        if str(temp[0]) == 'I':
            linha_intergateways = count+1

        
    count = count + 1

linha_interhubs = linha_gateways + 3

arquivo.seek(0)

hubs = arquivo.readlines()[linha_hubs]
teste=hubs.split() 
vetor_hubs = np.asarray(teste)
print(vetor_hubs)
qtd_hubs=(len(vetor_hubs))
arquivo.seek(0)

gateways = arquivo.readlines()[linha_gateways]
teste=gateways.split() 
vetor_gateways = np.asarray(teste)
print(vetor_gateways)
qtd_gateways=(len(vetor_gateways))
arquivo.seek(0)

temp = linha_interhubs

inter_hubs = inter_hubs+'\t'+arquivo.readlines()[temp]
temp = temp + 1
arquivo.seek(0)

for n in range(0,(qtd_interhubs-1)):
    inter_hubs = inter_hubs+'\t'+arquivo.readlines()[temp]
    temp = temp + 1
    arquivo.seek(0)


inter_hubs=inter_hubs.replace('\n','')
teste=inter_hubs.split() 
vetor_inter_hubs = np.asarray(teste)
print(vetor_inter_hubs)

temp = linha_intergateways
temp1 = arquivo.readlines()[temp]
inter_gateways = inter_gateways+'\t'+ temp1[1] + temp1[2] + temp1[3] + temp1[4] + temp1[5] + temp1[6] + temp1[7] + temp1[8] + temp1[9] + temp1[10]
temp = temp + 1
arquivo.seek(0)

for n in range(0,(qtd_intergateways-1)):
    temp1 = arquivo.readlines()[temp]
    inter_gateways = inter_gateways+'\t'+ temp1[1] + temp1[2] + temp1[3] + temp1[4] + temp1[5] + temp1[6] + temp1[7] + temp1[8] + temp1[9] + temp1[10]
    temp = temp + 1
    arquivo.seek(0)


inter_gateways=inter_gateways.replace('\n','')
teste=inter_gateways.split() 
vetor_inter_gateways = np.asarray()
print(vetor_inter_gateways)

print(qtd_intergateways)
print(qtd_interhubs)

mapa = folium.Map( location=[-15.77972, -47.92972], tiles = 'stamentoner')

for index, l_aeroportos in aeroportos2.iterrows():
    for index, l2_aeroportos in aeroportos3.iterrows():
        for n in range(0,qtd_interhubs):
            temp = vetor_inter_hubs[i]
            temp1= temp[2] + temp[3] + temp[4]
            temp2 = temp[6] + temp[7] + temp[8]
            if (int(l_aeroportos['ID']) == int(temp1)) and (int(l2_aeroportos['ID']) == int(temp2)):
                folium.PolyLine([(l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']), (l2_aeroportos['LATITUDE'],l2_aeroportos['LONGITUDE'])],
                color='#008000',
                weight=2,
                opacity=1).add_to(mapa)
            i = i + 1
        i=0


for index, l_aeroportos in aeroportos2.iterrows():
    for index, l2_aeroportos in aeroportos3.iterrows():
        for n in range(0,qtd_intergateways):
            temp = vetor_inter_gateways[i]
            temp1= temp[2] + temp[3] + temp[4]
            temp2 = temp[6] + temp[7] + temp[8]
            if (int(l_aeroportos['ID']) == int(temp1)) and (int(l2_aeroportos['ID']) == int(temp2)):
                folium.PolyLine([(l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']), (l2_aeroportos['LATITUDE'],l2_aeroportos['LONGITUDE'])],
                color='#ff0000',
                weight=2,
                opacity=1).add_to(mapa)
            i=i+1
        i=0


for index, l_aeroportos in aeroportos.iterrows():
    
    for n in range(0,qtd_hubs):

        if int(l_aeroportos['ID']) == int(vetor_hubs[i]):
            folium.RegularPolygonMarker(
                [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
                tooltip=l_aeroportos['AEROPORTO'],
                color = 'green',
                fill_color='#0000ff',
                number_of_sides=3,
                radius=6
            ).add_to(mapa)
        i = i + 1
    i=0


for index, l_aeroportos in aeroportos.iterrows():
   
    for n in range(0,qtd_gateways):

        if int(l_aeroportos['ID']) == int(vetor_gateways[i]):
            folium.RegularPolygonMarker(
                [l_aeroportos['LATITUDE'],l_aeroportos['LONGITUDE']],
                tooltip=l_aeroportos['AEROPORTO'],
                color = 'red',
                fill_color='#008000',
                number_of_sides=25,
                radius=5
            ).add_to(mapa)
        i = i + 1
    i = 0
arquivo.seek(0)

mapa.save('arquivos de saida/aeroportos.html')

linha_fluxo = linha_intergateways + qtd_intergateways + 2

print(linha_fluxo)
count=0
count2=0
demanda_direta=0
demanda_hub=0
demanda_gateway=0
linha=0
linhas=0
local1=0
local2=0
temp4=0
temp5=int(0)
temp6=0
count3=0
count4=0
fluxo_hub2=0
for n in range(0,200):
    temp = arquivo.readlines()[linha_fluxo]
    teste = temp.split()
    vetor_fluxo=np.asarray(teste)
    arquivo.seek(0)


    temp2 = len(vetor_fluxo)

    if temp2 == 3:
        fluxo_direto = fluxo_direto + 1
        temp1 = vetor_fluxo[i]
        temp1 = temp1.replace('f','')
        temp1 = temp1.replace(',','\t')
        temp1 = temp1.replace('(','')
        temp1 = temp1.replace(')','')
        teste = temp1.split()
        temp1=np.asarray(teste)
        arquivo.seek(0)

        local1 = temp1[0]
        local2 = temp1[1]

        linhas = demanda.loc[demanda['ID_AEROPORTO_1']==int(local1)]
        linha = linhas.loc[linhas['ID_AEROPORTO_2']==int(local2)]
        temp5 = linha['DEMANDA'].astype(int) * 1
        temp6 = int(temp5)
        demanda_direta = demanda_direta +  temp6
        print(demanda_direta)

    temp3 = (temp2/3)
    if temp2 > 3:
        i=0
        for l in range(0,int(temp3)):
            temp1 = vetor_fluxo[i]
            temp1 = temp1.replace('f','')
            temp1 = temp1.replace(',','\t')
            temp1 = temp1.replace('(','')
            temp1 = temp1.replace(')','')
            teste = temp1.split()
            temp1=np.asarray(teste)
            arquivo.seek(0)

            for p in range(0,4):

                if int(temp1[j]) > 173:
                    count = count + 1
                
                if int(temp1[j]) < 173:
                    count3 = count3 + 1

                j = j +1

                

            j=0
            if count > 0:
                count2 = 1
            if count3 > temp3/2:
                count4 = 1
            count = 0
            count3 = 0


            i = i + 3


        if count2 > 0:
            fluxo_gateway = fluxo_gateway + 1
            linhas = demanda.loc[demanda['ID_AEROPORTO_1']==int(local1)]
            linha = linhas.loc[linhas['ID_AEROPORTO_2']==int(local2)]
            temp5 = linha['DEMANDA'].astype(int) * 1
            temp6=int(temp5)
            demanda_gateway = demanda_gateway + temp6
            if count4==1:
                   fluxo_hub2 = fluxo_hub2 + 1


        if count2 == 0:
            fluxo_hub = fluxo_hub + 1
            linhas = demanda.loc[demanda['ID_AEROPORTO_1']==int(local1)]
            linha = linhas.loc[linhas['ID_AEROPORTO_2']==int(local2)]
            temp5 = linha['DEMANDA'].astype(int) * 1
            temp6=int(temp5)
            demanda_hub = demanda_hub + temp6
        count2=0
        count4=0
        i=0



    linha_fluxo = linha_fluxo + 1
    print(linha_fluxo)

demanda_total = demanda_direta + demanda_gateway + demanda_hub
fluxo_hub2=fluxo_hub+fluxo_hub2
print('% Demanda atendida direta')
print((demanda_direta/demanda_total)*100)
print('% Demanda atendida Gateway')
print((demanda_gateway/demanda_total)*100)
print('% Demanda atendida Hub')
print((demanda_hub/demanda_total)*100)

fluxo_total = fluxo_direto + fluxo_gateway + fluxo_hub
print('Fluxo direto %')
print((fluxo_direto/fluxo_total)*100)
print('Fluxo por gateway %')
print((fluxo_gateway/fluxo_total)*100)
print('Fluxo por hub %')
print((fluxo_hub/fluxo_total)*100)

saida.write(str(qtd_hubs))
saida.write('\t')
saida.write(str(qtd_gateways))
saida.write('\t')
saida.write(str(qtd_interhubs))
saida.write('\t')
saida.write(str(qtd_intergateways))
saida.write('\t')
saida.write(str((fluxo_direto/fluxo_total)*100))
saida.write('\t')
saida.write(str((fluxo_hub/fluxo_total)*100))
saida.write('\t')
saida.write(str((fluxo_gateway/fluxo_total)*100))
saida.write('\t')
saida.write(str((demanda_direta/demanda_total)*100))
saida.write('\t')
saida.write(str((demanda_hub/demanda_total)*100))
saida.write('\t')
saida.write(str((demanda_gateway/demanda_total)*100))
saida.write('\t')
saida.write(str((fluxo_hub2/fluxo_total)*100))
saida.write('\n')

