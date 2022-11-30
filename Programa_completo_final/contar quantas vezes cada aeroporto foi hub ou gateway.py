import numpy as np
import pandas as pd
import folium
import os

repeticao=30
numero=0
saida = open('arquivos de saida/saida.txt', 'w')

while (repeticao>numero):

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

    arquivo = open('arquivos de entrada/'+str(numero)+'.txt', 'r')
    

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

    arquivo.seek(0)

    hubs = arquivo.readlines()[linha_hubs]
    teste=hubs.split() 
    vetor_hubs = np.asarray(teste)

    qtd_hubs=(len(vetor_hubs))
    arquivo.seek(0)

    gateways = arquivo.readlines()[linha_gateways]
    teste=gateways.split() 
    vetor_gateways = np.asarray(teste)

    qtd_gateways=(len(vetor_gateways))
    arquivo.seek(0)


    saida.write(str(vetor_gateways))
    saida.write('\n')
    numero = numero + 1
    print(numero)

saida.close()

