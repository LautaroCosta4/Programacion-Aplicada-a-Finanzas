# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 22:29:56 2023

@author: costa
"""
import re

dividendo = '3x ** 2 + 2x - 8'
divisor =  '1x ** 1 + 2'

"Calcular el grado de ambos polinomios"
"Hacer de cuenta que el polinomio está ordenado entonces el grado se encuentra en el primer elemento del segundo split"

def datos(polinomio):
    coincidencia = re.search("[+-]", polinomio)  # Busca el primer signo de suma o resta en la cadena 
    if coincidencia: #si hubo una coincidencia, puede devolver None sino hubo
        indice_signo = coincidencia.start()
        izquierda_signo = (polinomio[:indice_signo]).replace(' ','')
        grado = izquierda_signo[-1]
        derecha_signo = (polinomio[indice_signo + 1:]).replace(' ','')
        return [grado,izquierda_signo,derecha_signo]
        

def division_termino (dividendo,divisor):
    g_dividendo,t1_dividendo,resto_dividendo = datos(dividendo)
    g_divisor, t1_divisor, resto_divisor = datos(divisor)
    resta_grados = int(g_dividendo) - int(g_divisor)
    resultado = t1_dividendo[0] + '/' +  t1_divisor[0] + ' x**' + str(resta_grados)
    print(resultado)
    return resultado


#%%
def grado (polinomio):
    """Funcion que descubra el grado del polinomio a pesar de que no este completo. El 
    polinomio debe estar escrito de la forma ax^n+bx^(n-1)+c"""
    grados = []
    polinomio = polinomio.replace(' ','')
    for termino in re.findall(r'([-+]?[0-9]*)x\^?(\d*)', polinomio):
        grados.append(termino[-1])
    return max(grados)

#%%
import numpy as np

dividendo = np.array([3,0,0,6,0,-3])
divisor = np.array([1,1])


def division_polinomio (dividendo,divisor):
    inicial = dividendo.copy()
    resultado = []
    if len(inicial) < len (divisor):
        print('El grado del divisor es mayor que el del dividendo')
        print(f'El resto es: {inicial}')
        return resultado 
    else:
        n1_cociente = inicial[0]/divisor[0]
        resultado.append(n1_cociente)
        print(f' El cociente del primer término es {n1_cociente}')
        prod_n1_divisor = n1_cociente * divisor
        print(f' El producto entre el cociente y el divisor del primer termino es {prod_n1_divisor}')
        lista_de_ceros = np.zeros(len(inicial))
        lista_de_ceros[:len(divisor)] = prod_n1_divisor  #siempre agarra conforme la longitud del divisor
        print(f' La lista que se va a restar es la siguiente: {lista_de_ceros}')
        cambio = inicial - lista_de_ceros
        print(f' Repetir el proceso con {cambio}')
        return resultado + division_polinomio(cambio[1:], divisor)
    
resultado = division_polinomio(dividendo, divisor)
print(resultado)

#%%
# VERSION CORTA
import numpy as np

dividendo = np.array([3,0,0,6,0,-3])
divisor = np.array([1,1])

def division_polinomio_2 (dividendo,divisor):
    resultado = []
    if len(dividendo) < len (divisor): #Quiere decir que el grado del divisor es mayor que el del dividendo y, entonces, no puede seguir 
        return resultado
    else:
        n1_cociente = dividendo[0]/divisor[0]
        resultado.append(n1_cociente)
        prod_n1_divisor = n1_cociente * divisor
        lista_de_ceros = np.zeros(len(dividendo))
        lista_de_ceros[:len(divisor)] = prod_n1_divisor  #siempre agarra conforme la longitud del divisor
        return resultado + division_polinomio_2((dividendo-lista_de_ceros)[1:], divisor)
    
resultado = division_polinomio_2(dividendo, divisor)
print(resultado)

#%%
