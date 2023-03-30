# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 22:00:56 2023

@author: costa
"""


import random
import string


def diccionario_posibilidades_2(seed = '1'):
    random.seed(seed)
    dic = {letra: random.sample(string.punctuation + string.digits, 6) for letra in string.ascii_letters}
    keys_restantes = string.digits + string.punctuation
    for key in keys_restantes:
        if key in string.digits:
            dic[key] = random.sample(string.ascii_letters + string.punctuation ,6)
        else:
            dic[key] = random.sample(string.ascii_letters + string.digits ,6)
    return dic

def encriptar (password, dic, seed = 1):
    random.seed(seed)
    contraseña_encriptada = ''
    for caracter in password:
        if caracter in dic:
            contraseña_encriptada += ''.join(random.sample(dic[caracter], 2))
    return contraseña_encriptada

def verificacion (encriptada, dic, contraseña):
    nueva = encriptar(contraseña, dic)
    if encriptada == nueva:
        print('La contraseña es correcta')
        return True
    else:
        print('La contraseña es incorrecta')
        return False

diccionario = diccionario_posibilidades_2()
password_original = 'Nico25'
contraseña_encriptada = encriptar(password_original, diccionario)
print(password_original)
print(contraseña_encriptada)
verificacion(contraseña_encriptada, diccionario, 'Nico5')

#%%

class  Usuario:
    __encriptacion = diccionario_posibilidades_2()
    ide = 0
    def __init__(self, nombre, apellido,email,contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.encriptada = encriptar(contraseña, Usuario.__encriptacion)
        Usuario.ide += 1
        self.numero = Usuario.ide 
        
    def contabilizar (self):
        print(f'Soy el usuario: {self.numero}')
        
    def verificacion_(self, contraseña):
        verificacion(self.encriptada, Usuario.__encriptacion, contraseña)


usuario_1 = Usuario('Lautaro','Costa','lcsota@udesa.edu.ar','Nico25')
usuario_1.contabilizar()
print(f' \nMi nombre es {usuario_1.nombre} {usuario_1.apellido}.\nMi email es {usuario_1.email}.\nEl banco me dio la siguiente contraseña encriptada:{usuario_1.encriptada}\n')
usuario_2 = Usuario('Lucas','Gens','lgens@udesa.edu.ar','Pepe32')
usuario_2.contabilizar()
print(f' \nMi nombre es {usuario_2.nombre} {usuario_2.apellido}. \n Mi email es {usuario_2.email}. \n El banco me dio la siguiente contraseña encriptada: {usuario_2.encriptada}')
print(f'La cantidad de usuarios del Banco es: {Usuario.ide}')

class Cuentas(Usuario):
    monedas = ["ARS", "USD"]
    ide_2 = 0
    def __init__(self,nombre, apellido, email, contraseña, balance_0, balance_1):
        super().__init__(nombre, apellido, email, contraseña)
        self.alias_pesos = self.nombre + self.apellido + '.' + Cuentas.monedas[0]
        self.alias_dolares = self.nombre +' ' + self.apellido + '.' + Cuentas.monedas[1]
        self.balance_pesos = balance_0
        Cuentas.ide_2 += 1 
        self.ide_pesos = Cuentas.ide_2
        self.balance_dolares = balance_1
        Cuentas.ide_2 += 1 
        self.ide_dolares = Cuentas.ide_2

usuario_3 = Cuentas('Tiziano','Levi','tbernal@udesa.edu.ar','Lolo97',230000,3000)



