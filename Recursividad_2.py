# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 09:56:06 2023

@author: costa
"""

# RECURSIVIDAD: Algoritmo de Euclides

def MCD_Euclides (numero_1, numero_2):
    # numero_1 es el mayor
    if numero_1 % numero_2 == 0:
        return numero_2
    # Si la división es exacta (Si el resto es 0), el MCD es el Divisor
    else:
    # Si no es exacta, dividimos el divisor entre el resto obtenido y continuamos hasta
    # obtener una división exacta
        resto = numero_1 % numero_2 
        return MCD_Euclides (numero_2,resto)


MCD = MCD_Euclides(150, 39)
MCD_2 = MCD_Euclides(72, 16)

#%%
def MCD_factorizacion (numero):
    #Encontrar todos los divisores del numero en cuestión
    divisores = []
    for valor in range (1, numero + 1):
        resto = numero % valor
        if resto == 0:
            divisores.append(valor)
        else:
            continue
    return divisores


def MCD (numero_1, numero_2):
    #Arma una lista con todos los divisores comunes y luego encuentra el elemento
    # más grande de esa lista
    divisores_n1 = MCD_factorizacion(numero_1)
    print(divisores_n1)
    divisores_n2 = MCD_factorizacion(numero_2)
    print(divisores_n2)
    divisores_comunes = []
    for elemento in divisores_n1:
        if elemento in divisores_n2:
            divisores_comunes.append(elemento)
    print(divisores_comunes)
    return max(divisores_comunes)

respuesta = MCD(150, 39)

#%%

# Usar sets
def factorizacion_primos (numero):
    descomposicion = []
    for elemento in range (2, numero +1):
        while numero % elemento ==0:
            descomposicion.append(elemento)
            numero = numero // elemento
    return descomposicion


def mcd (numero_1, numero_2):
    respuesta = 1
    descomposicion_1 = factorizacion_primos(numero_1)
    descomposicion_2 = factorizacion_primos (numero_2)
    print(descomposicion_1)
    print(descomposicion_2)
    repetidos = []
    for elemento in descomposicion_1:
        if elemento not in repetidos and elemento in descomposicion_1 and elemento in descomposicion_2:
            repetidos.append(elemento)
            print(repetidos)
        
    for primo in repetidos:
        cantidad_1 = descomposicion_1.count(primo)
        cantidad_2 = descomposicion_2.count(primo)
        minimo_exp = min(cantidad_1,cantidad_2)
        respuesta = respuesta * primo ** minimo_exp
        print(cantidad_1)
        print(cantidad_2)
        print(minimo_exp)
        print(respuesta)
    return respuesta
            
mcd_por_descomposicion = mcd(450,360)
    
    

#%%
def binarios (decimal):
    lista_binarios = []
    if decimal // 2  == 0: #1//2 = 0
        lista_binarios.append(1)
        return lista_binarios
    else:
        # decimal // 2 == x  725/2 = 362
        cociente = decimal // 2
        resto = decimal % 2
        lista_binarios.append(resto)
        return lista_binarios + binarios(cociente)

# numero_decimal = binarios (725)

numero_decimal = binarios (1264)
print(numero_decimal[::-1])

# 10011110000

#%%

dic = {'A':'Alpha','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo','F':'Foxtrop','G':'Golf',
        'H': 'Hotel','I': 'India', 'J':'Juliet','K':'Kilo','L':'Lima','M':'Mike','N':'November',
        'O':'Oscar', 'P':'Papa','Q':'Quebec', 'R':'Romeo','S':'Sierra','T':'Tango','U':'Uniform',
        'V':'Victor','W': 'Whiskey','X': 'Xray', 'Y':'Yankee', 'Z': 'Zulu'}

def alphabet (nato,palabra):
    lista_final = []
    if palabra == '':
        return lista_final
    else:
        letra = palabra [0].upper()
        tail = palabra[1:len(palabra)]
        lista_final.append(nato[letra])
        return lista_final + alphabet(nato, tail)
    
respuesta = alphabet(dic, 'Chiche')
print(respuesta)

#%%

romanos = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1, '':0}

def conversion_romanos (dic,numero):
    resultado = 0
    if numero == '':
        return 0
    else:
        primer_digito = numero[0]
        resto_digitos = numero [1:len(numero)]
        if len(resto_digitos)==0:
            resultado += dic[primer_digito]
            return resultado + conversion_romanos(dic, resto_digitos)
        if dic[primer_digito] >= dic[resto_digitos[0]] :
            resultado += dic[primer_digito]
            return resultado + conversion_romanos(dic, resto_digitos)
        if  dic[primer_digito] < dic[resto_digitos[0]] :
            resultado -= dic[primer_digito]
            return resultado  + conversion_romanos(dic, resto_digitos)

respuesta = conversion_romanos(romanos, 'MDLXXXIV')
print(respuesta)

#%%

def palindromo (palabra):
    palabra = palabra.replace(' ','')
    if palabra == '':
        return True
    elif len(palabra) == 1:
        return True 
    else:
        primer_caracter = palabra [0]
        ultimo_caracter = palabra [-1]
        nueva_palabra = palabra [1:-1]
        if primer_caracter == ultimo_caracter:
            return  True and palindromo(nueva_palabra) 
        else:
            return False
    
def mensaje_usuario (resultado):
    if resultado == True:
        print('La palabra ingresada es palíndromo')
    else:
        print('La palabra ingresada NO es palíndromo')
        
        
respuesta = palindromo('hola')
# respuesta = palindromo('sometamos o matemos')
mensaje_usuario(respuesta)

#%%
def flatter (lista):
    lista_final = []
    if len(lista) == 0:
        return lista_final
    else:
        primer_elemento = lista[0]
        resto = lista[1:len(lista)]
        if type(primer_elemento) != list:
            lista_final.append(primer_elemento)
            return lista_final + flatter (resto)
        else:
            return flatter (primer_elemento) + flatter(resto)
a = flatter ( [1,[2,3],[4,[5,[6,7]]],[[[8],9],[10]]])
print(a)


#%%
#ESTE ESTA BIEN

def encoding (lista_de_letras):
    lista_final = []
    if len (lista_de_letras) == 0:              #Si tengo 3W tengo que evitar que llegue al 
                                                #indice 2 poeque sino sumaria un elemento 
        return lista_final
    for indice in range (len(lista_de_letras)):
        if len(lista_de_letras) > 1 and indice < len (lista_de_letras)-1 :   
            if lista_de_letras[indice] == lista_de_letras[indice + 1]:
                continue  #el indice tiene que ser distinto a len porque sino el ultimo elemento
                            #le suma 1 y da error el indexing
            else:
                lista_original = lista_de_letras[:indice + 1]
                nueva_lista = lista_de_letras[indice + 1:]
                cantidad = lista_original.count(lista_de_letras[indice])
                lista_final.extend((lista_de_letras[indice],cantidad))
                return lista_final + encoding(nueva_lista)
        else:
            cantidad = indice + 1 #si cambia de A a W(lista_de_letras) el range vale 0 y devuelve 1
            lista_final.extend((lista_de_letras[0],cantidad))
            return lista_final 
respuesta = ['A','A','A','A','B','B','A','W','W','W']
solucion = encoding(respuesta)
print(solucion)

#%%


