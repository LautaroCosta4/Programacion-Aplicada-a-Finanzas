# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:07:21 2023

@author: costa
"""
import matplotlib.pyplot as plt
import pandas as pd

class FlujosDeFondos:
    def __init__(self,ff,tasa):
        self.flujos = ff
        self._flujos_aux = ff
        self.tasa = tasa
    def van (self):
        return self.valor(periodo = 0 )
            
    def vp_recursiva (self):
        """Calcula el valor atual de los flujos de fondos"""
        flujos = self._flujos_aux
        print(f' Los flujos son los siguientes: {flujos}')
        tasa = self.tasa
        vp = []
        if len(flujos) == 1:
            vp.append(flujos[0])
            self.flujos_aux = self.flujos.copy() #setea los flujos auxiliares de vuelta en 0
            print(f'{self.flujos_aux}')
            return vp 
        else:
            descontado = flujos[-1] / (1+tasa) ** (len(flujos) -1 )
            print(f' El flujo a descontar es el siguiente: {flujos[-1]}')
            print(f' El flujo descontado es el siguiente: {descontado}')
            vp.append(descontado)
            self._flujos_aux = self._flujos_aux[:-1]
            print(f' {self._flujos_aux}')
            return vp + self.vp_recursiva()

    def valor (self, periodo):
        """Calcula el valor de una serie de flujos de fondos en un momento determinado. Si el momento es 0,
        la funcion calculo el valor actual, caso contrario calcula el valor futuro"""
        ff = self.flujos
        tasa  =self.tasa 
        capitalizados = [round(ff[i] * (1 +tasa )**(periodo - i),2) for i in range (len(ff[:periodo]))]
        descontados = [round(ff[periodo:][i]/(1+tasa)**(i),2) for i in range(len(ff[periodo:]))]
        resultado = round(sum(capitalizados)+sum(descontados),2)
        return resultado
    
    def my_linspace(self,start = 0, stop = 2, num=1000):
        step = (stop - start) / (num - 1)
        return [start + i * step for i in range(num)]
    
    def gr_VAN (self):
        tasas = self.my_linspace()
        van = []
        aux = self.tasa
        for tasa in tasas:
            self.tasa = tasa
            v0 = self.van()
            van.append(v0)
        self.tasa = aux
        plt.figure(figsize=(8, 6))  
        plt.plot(tasas, van, linestyle='-', linewidth=2, color='blue') 
        plt.xlabel('Rates')
        plt.ylabel('npv')
        plt.title('NPV')
        plt.grid(True)
        plt.show()
        
    def tir_GS(self, start=0, stop=45, n=10, tol=0.00001):
        tasas = self.my_linspace(start, stop, n)
        aux = self.tasa
        if stop-start < tol:
            self.tasa = aux
            tir = (stop + start) / 2
            print(f' La TIR es {round(tir,4)}')
        else:
            van,borders = [],[]
            for indice, tasa in enumerate(tasas):
                self.tasa = tasa
                v0 = self.van()
                van.append((indice, v0))
            for i in range(1, len(van)):
                if van[i - 1][1] * van[i][1] <= 0:
                    borders.append((tasas[van[i - 1][0]], tasas[van[i][0]]))
            if len(borders) >= 1:
                interval = max(borders)
                tir = self.tir_GS(interval[0], interval[1])
            else:
                print('No encontré nada')
                tir = 0
        return  tir

    def tir_BI(self, start =0, stop=100, n=3, tol=0.00001):
        tasas = self.my_linspace(start, stop, n)
        aux = self.tasa
        if stop-start < tol:
            self.tasa = aux
            tir = (stop + start) / 2
        else:
            van = []
            for tasa in (tasas):
                self.tasa = tasa
                v0 = self.van()
                van.append(v0)
            if van[0] * van[1] <=0:
                t1,t2 = tasas[0],tasas[1]
                tir =self.tir_BI(t1,t2)
            elif van[1] * van[-1] <=0:
                t1,t2 = tasas[1],tasas[-1]
                tir =self.tir_BI(t1,t2)
            else:
                print('No encontré nada')
                tir = 0
        return tir


flujo_de_fondos = FlujosDeFondos([-365,200,200,200,200,200,-200,-200,-200,-200,-200,0,0,0,0,0,0,0,0,0,400], 0.15)
flujo_de_fondos.gr_VAN()
tir_GS = flujo_de_fondos.tir_GS()
tir_BI = flujo_de_fondos.tir_BI()
# flujo_de_fondos_2 = FlujosDeFondos([-50000,10000, 12000, 15000, 18000, 20000], 0.08)
# tir_GS_2 = flujo_de_fondos_2.tir_GS()
# tir_BI_2 = flujo_de_fondos_2.tir_BI()



