#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: CatalinaBernal
"""

import zipfile
import glob
import numpy as np
#import csv, operator
import pandas as pd

carpeta = zipfile.ZipFile("berlin.zip", "r")

carpeta.extractall(path= "/Users/CatalinaBernal/Desktop/Métodos Computacionales/CatalinaBernal_taller3")
#lista = os.listdir("/Users/CatalinaBernal/Desktop/Métodos Computacionales/CatalinaBernal_taller3/s3_files/berlin")
archivos = glob.glob("/Users/CatalinaBernal/Desktop/Métodos Computacionales/CatalinaBernal_taller3/s3_files/berlin/*.csv")

over = list()
acom = list()
bed = list()
price = list()
mins = list()
date = list()

#extraccion de datos
for arc in archivos:
        inf = pd.read_csv(arc, sep = ',')
        datos = np.array(inf)
        datos = datos.T
        over.append(datos[9])
        acom.append(datos[10])
        bed.append(datos[11])
        price.append(datos[13])
        #mins.append(datos[14])
        #date.append(datos[16])

#normalizacion de datos
n_over = over[:]
for i in range(0, len(over)):
    temp = over[i]
    n_over[i] = (temp-np.mean(temp))/np.std(temp)

##
#for i in range(0, len(acom)):
#    go = acom[i]
#    for j in range(0, len(go)):
#        g = go[j]
#        if(type(g) == str):
#            print(g)
        
print(over[1])
        
#n_acom = acom[:]
#for i in range(0, len(acom)):
#    temp = acom[i]
#    n_acom[i] = (temp-np.mean(temp))/np.std(temp)
    
#n_bed = bed[:]
#for k in range(0, len(bed)):
#    temp = bed[k]
#    n_bed[k] = (temp-np.mean(temp))/np.std(temp)
#
#n_price = price[:]
#for l in range(0, len(price)):
#    temp = price[l]
#    n_price[l] = (temp-np.mean(temp))/np.std(temp)  
#    
#n_mins = mins[:]
#for m in range(0, len(mins)):
#    temp = mins[m]
#    n_mins[m] = (temp-np.mean(temp))/np.std(temp)    

#print(n_acom[1])
#print(acom[1])


    