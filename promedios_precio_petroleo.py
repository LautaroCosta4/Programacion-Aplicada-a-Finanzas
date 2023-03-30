# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:30:53 2023

@author: costa
"""
# pip install openpyxl
import pandas as pd
dt = pd.read_excel('petroleo-wti-1983-2022.xlsx')


def promedios_petroleo(data_frame):
    """Calcula los promedios anuales del precio del petróleo, y un promedio general del periodo comprendido
    entre el año 1983 y 2022 a partir de los datos provsitos de un archivo excel"""
    promedios_anuales = [round(data_frame.loc[0:7,'precio'].mean(),4)] #Arranca con el promedio del año 1983
    for i in range(8,len(data_frame)-9,12): #Agrega los promedios desde el 84 al 2021
        promedios_anuales.append(round(data_frame.loc[i:i + 11,'precio'].mean(),4))
    promedios_anuales.append(round(data_frame.loc[464:475,'precio'].mean(),4)) #Agrega los promedios del año 2022
    promedio_final = round(sum(data_frame['precio'])/len(data_frame),4) #calcula el promedio total
    return promedios_anuales,promedio_final

def elegir_año(lista_promedios, fecha):
    'Muestra el promedio del precio del petróleo en un año dado comprendido entre el 1983 y el 2022'
    lista_años =[año for año in range (1983,2022 + 1)]
    lista_con_index = [(indice, año) for indice,año in enumerate(lista_años)]
    indice_a_usar = 0
    for indice,año in lista_con_index:
        if año == fecha:
            indice_a_usar = indice
    print(f' El promedio de los precios del petróleo en el año {fecha} es {lista_promedios[indice_a_usar]} ')
    return lista_promedios[indice_a_usar]


anuales,final = promedios_petroleo(dt)
print(f' Los promedios por año son los siguientes: {anuales}')
deseado = elegir_año(anuales, fecha = 1986)

#%%

