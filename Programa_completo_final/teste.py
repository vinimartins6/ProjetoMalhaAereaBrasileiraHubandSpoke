import pandas as pd
import numpy as np
import os

arquivo = open('teste.txt','r')
arquivo1 = open('teste1','w')
valor=str((arquivo.readlines()))
valor=valor.replace('-','\t')
arquivo1.write(valor)


arquivo.close()
arquivo1.close()

