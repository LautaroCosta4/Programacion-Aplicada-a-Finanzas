# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 12:46:56 2023

@author: costa
"""

class Myarray1 (object):
    """No está permitido almacenar la matriz como una lista de listas"""
    def __init__ (self,lista,r,c,by_row):
        """
        Atributos Comunes
        Parameters
        ----------
        lista : list
            Lista que contiene todos los elementos de la matriz.
        r : int
            Corresponde a la cantidad de filas de la matriz.
        c : int
            Corresponde a la cantidad de columnas de la matriz.
        by_row : bool
            Si recibe True, atraviesa la lista que contiene los elementos de la
            matriz por filas. Caso contrario, lo hace por columnas.
        Returns
        -------
        None.
        """
        self.elems = lista
        self.r = r
        self.c = c
        self.by_row = by_row
    
    def verificacion (self):
        """
        Se encarga de verificar si los datos enviados como parámetros son
        consistentes. En caso de que no lo sean, devuelve False

        Returns
        -------
        salida : bool
            True en caso de que los datos enviados seas consistentes, Falso caso
            contrario.

        """
        if len(self.elems) != self.r * self.c:
            salida = False
        else:
            salida = True
        return salida
    
    def get_pos (self, j,k):
        """
        Toma las coordenadas j,k en la matriz y devuelve la posicion asociada a
        la lista de elementos
        Parameters
        ----------
        j : int
            Hace referencia al numero de fila de un elemento de la matriz.
        k : int
            Hace referencia al numero de columna de un elemento de la matriz.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que el usuario ingrese mal las 
            coordenadas de algún elemento y trate de buscar algún elemento que 
            excede las dimensiones de la matriz o, si la matriz fue creada
            mal inicialmente. 

        Returns
        -------
        pos : int
            Devuelve la posicion asociada en la lista de elementos de la matriz
        """
        if self.verificacion() and 1 <= j <= self.r and 1 <= k <=self.c:
                if self.by_row == False:
                    pos = self.r * (k - 1) -1 + j
                else:
                    pos = self.c * (j - 1) -1 + k
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return pos

    def get_coords (self,m):
        """
        Toma una posición m en la lista y devuelve en forma de tupla las coordenadas
        (j,k) de la matriz

        Parameters
        ----------
        m : int
            Hace referencia a la posición de un elemento en la lista.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que el usuario ingrese la 
            posición de algún elemento  que exceda las dimensiones de la matriz
            o, si la matriz fue creada mal inicialmente. 

        Returns
        -------
        coords : tuple
            Hace referencia a las coordenadas en la matriz del elemento de la 
            lista cuya posición es m.

        """
        if self.verificacion() and 0 <= m <= len(self.elems) - 1:
            if self.by_row:
                j, k = m // self.c + 1, m % self.c + 1
            else:
                j,k = m % self.r + 1, m // self.r + 1
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return (j,k)


    def switch (self):
        """
        Altera la lista elems y cambia el valor de verdad de by row.
        
        Returns
        -------
        Devulve un objeto.
        """
        if self.verificacion():
            paso = 0
            nueva_lista = []
            if self.by_row:
                """Quiere decir que la lista se navega por filas, entonces, para armarla
                por columnas, el paso que se debe dar es de la cantidad de columnas"""
                paso = self.c
                navegacion = False
            else:
                """Quiere decir que la lista se navega por columnas, entonces, para armarla
                por filas, el paso que se debe dar es de la cantidad de filas"""
                paso = self.r
                navegacion = True
            for i in range(paso):
                nueva_lista.extend(self.elems[i::paso])
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(nueva_lista, self.r, self.c, navegacion)
    
    def get_row (self,j):
        """
        Devuelve el contenido de la fila j

        Parameters
        ----------
        j : int
            Fila cuyo contenido se devolverá.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la fila que se desea obtener
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve una lista con los elementos correspondientes a la fila seleccionada
        """
        if self.verificacion() and 1 <= j <= self.r:
            aux = self.elems
            if self.by_row == False:
                """Uso la función Switch definida previamente para facilitar la tarea.
                En vez de separara los dos posibles casos de que byrow sea True o False y
                trabajarlos de forma aislada, se acota la tarea únicamente al caso que se 
                trabaje por filas."""
                aux = (self.switch()).elems
                
            row = aux[(j-1)*self.c : j*self.c]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return row
    
    def get_col (self,k):
        """
        Devuelve el contenido de la columna k
        
        Parameters
        ----------
        k : int
            Columna cuyo contenido se devolverá.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la columna que se desea obtener
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve una lista con los elementos correspondientes a la columna seleccionada.

        """
        if self.verificacion() and 1 <= k <= self.c:
            aux = self.elems
            if self.by_row == False:
                aux = (self.switch()).elems
            col = aux[(k-1):len(aux):self.c]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return col
    
    def get_elem (self,j,k):
        """
        Reutiliza la función get_row para posicionarse sobre la fila de la cual
        se desea extraer un elemento en particular.

        Parameters
        ----------
        j : int
            Hace referencia al numero de fila de un elemento de la matriz.
        k : int
            Hace referencia al numero de columna de un elemento de la matriz.

        Returns
        -------
        Devuelve el elemento m ubicado en la posicion (j,k)
        m : int.
        """
        if self.verificacion() and 1 <= j <= self.r and 1 <= k <= self.c :
            m = self.get_row(j)[k - 1]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return m
    
    
    def index_row (self, j):
        """
        Se encarga de obtener los indices en la lista de todos los elementos
        de una determinada fila j

        Parameters
        ----------
        j : int
            Hace referencia a la fila cuyos elementos se desea obtener el
            indice en la lista

        Raises
        ------
        ValueError
            Se produce este error en caso de que la fila que se desea acceder
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        indices : list
            Lista que contiene todos los índices.

        """
        if self.verificacion() and 1 <= j <= self.r:
            coords = [(j,i) for i in range(1,self.c + 1)]
            indices = []
            for fila, columna in coords:
                indices.append(self.get_pos(fila, columna))
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente') 
        return indices
    
    def index_col (self,k):
        """
        Se encarga de obtener los indices en la lista de todos los elementos
        de una determinada columna k

        Parameters
        ----------
        k : int
            Hace referencia a la columna cuyos elementos se desea obtener el
            indice en la lista

        Raises
        ------
        ValueError
            Se produce este error en caso de que la columna que se desea acceder
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        indices : list
            Lista que contiene todos los índices.

        """
        if self.verificacion() and 1 <= k <= self.c:
            indices = []
            coords = [(i,k) for i in range(1,self.r + 1)]
            for fila, columna in coords:
                indices.append(self.get_pos(fila, columna))
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente') 
        return indices
            

    def del_row (self,j):
        """
        Elimina la fila j de la matriz

        Parameters
        ----------
        j : int
            Hace referencia al numero de la fila que se desea eliminar.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la fila que se desea eliminar
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto de la clase, habiendo eliminado la fila j.
        
        """
        if self.verificacion() and 1 <= j <= self.r:
            indices = self.index_row(j)
            elems = self.elems.copy()
            for indice in sorted(indices, reverse=True):
                """Se debe recorrer la lista en el orden invertido porque sino cambiarían
                los índices posteriores una vez que se vayan eliminando. """
                elems.pop(indice)
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente') 
        return Myarray1(elems, self.r - 1, self.c, self.by_row)
    
    
    def del_col (self,k):
        """"
        Elimina la columna k de la matriz

        Parameters
        ----------
        k : int
            Hace referencia al numero de la columna que se desea eliminar.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la columna que se desea eliminar
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto de la clase, habiendo eliminado la columna k.
        
        """
        if self.verificacion() and 1 <= k <= self.c:
            indices = self.index_col(k)
            elems = self.elems.copy()
            for indice in sorted(indices, reverse=True):
                """Se debe recorrer la lista en el orden invertido porque sino cambiarían
                los índices posteriores una vez que se vayan eliminando. """
                elems.pop(indice)
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente') 
        return Myarray1(elems, self.r, self.c - 1, self.by_row)


    def swap_cols (self,l,m):
        """
        Intercambia las columnas de la matriz

        Parameters
        ----------
        l : int
            Hace referencia a la primer columna
        m : int
            Hace referencia a la segunda columna.
            
        Raises
        ------
        ValueError
            Se produce este error en caso de que alguna de las columnas que se 
            desean intercambiar excedan las dimensiones de la matriz o,en caso
            de que la matriz haya sido creada mal inicialmente. 

        Returns
        -------
        Devuelve un objeto de la clase con las columnas intercambiadas.

        """
        if self.verificacion() and 1 <= l <= self.c and 1 <= m <= self.c:
            elems = self.elems.copy()
            i1 = list(zip( self.index_col(l), self.index_col(m)))
            final = sum((list(tupla) for tupla in i1), [])
            for i in range (0,len(final),2):
                elems[final[i]],elems[final[i + 1]] = elems[final[i + 1]],elems[final[i]]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(elems, self.r, self.c, self.by_row)


    def swap_rows (self,l,m):
        """
        Intercambia las filas de la matriz

        Parameters
        ----------
        l : int
            Hace referencia a la primer fila
        m : int
            Hace referencia a la segunda fila.
            
        Raises
        ------
        ValueError
            Se produce este error en caso de que alguna de las filas que se 
            desean intercambiar excedan las dimensiones de la matriz o,en caso
            de que la matriz haya sido creada mal inicialmente. 

        Returns
        -------
        Devuelve un objeto de la clase con las filas intercambiadas.

        """
        if self.verificacion() and 1 <= l <= self.r and 1 <= m <= self.r:
            elems = self.elems.copy()
            i1 = list(zip( self.index_row(l), self.index_row(m)))
            final = sum((list(tupla) for tupla in i1), [])
            for i in range (0,len(final),2):
                elems[final[i]],elems[final[i + 1]] = elems[final[i + 1]],elems[final[i]]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(elems, self.r, self.c, self.by_row)


    def scale_row (self,j,x):
        """
        Multiplica cada elemento de la fila j por un escalar.

        Parameters
        ----------
        j : int
            Hace referencia a la fila que se desea multiplicar.
        x : int
            Escalar por el que se multiplicará.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la fila que se desea multiplicar
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto pero con la fila j multiplicada por el factor x.

        """
        if self.verificacion() and 1 <= j <= self.r:
            indices = self.index_row(j)
            elems = self.elems.copy()
            for i in range (len(indices)):
                elems[indices[i]] = elems[indices[i]] * x 
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(elems, self.r, self.c, self.by_row)
    
    def scale_col (self,k,y):
        """
        Multiplica cada elemento de la columna k por un escalar.

        Parameters
        ----------
        k : int
            Hace referencia a la columna que se desea multiplicar.
        x : int
            Escalar por el que se multiplicará.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la columna que se desea multiplicar
            exceda las dimensiones de la matriz o, en caso de que la matriz haya
            sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto pero con la columna k multiplicada por el factor y.

        """
        if self.verificacion() and 1 <= k <= self.c:
            indices = self.index_col(k)
            elems = self.elems.copy()
            for i in range (len(indices)):
                elems[indices[i]] = elems[indices[i]] * y 
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(elems, self.r, self.c, self.by_row)

    def Transpose (self):
        """
        Calcula la matriz traspuesta.
        
        Raises
        ------
        ValueError
            Se produce este error en caso de que la matriz haya sido creada
            mal inicialmente.

        Returns
        -------
        Devuelve un elemento de la clase pero con la matriz traspuesta
        """
        if self.verificacion():
            aux = (self.switch()).elems
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray1(aux, self.c, self.r, self.by_row)


    def flip_cols (self):
        """
        Intercambia la primer columna con la última, la segunda con la penúltima
        y así sucesivamente.

        Raises
        ------
        ValueError
            Se produce este error en caso de que la matriz haya sido creada
            mal inicialmente.

        Returns
        -------
        Devuelve un elemento de la clase pero con las columnas intercambiadas.

        """
        matriz = Myarray1(self.elems, self.r, self.c, self.by_row)
        if self.verificacion():
            for i in range(1, self.c//2 + 1):
                matriz = matriz.swap_cols(i, self.c + 1- i )
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return matriz

    def flip_rows (self):
        """
        Intercambia la primer fila con la última, la segunda con la penúltima
        y así sucesivamente.

        Raises
        ------
        ValueError
            Se produce este error en caso de que la matriz haya sido creada
            mal inicialmente.

        Returns
        -------
        Devuelve un elemento de la clase pero con las filas intercambiadas.

        """
        matriz = Myarray1(self.elems, self.r, self.c, self.by_row)
        if self.verificacion():
            for i in range(1, self.r//2 + 1):
                matriz = matriz.swap_rows(i, self.r + 1- i )
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return matriz
    
    def det (self):
        """
        Calcula el determinante de la matriz

        Returns
        -------
        det : int
            Determinante.

        """
        aux = Myarray1(self.elems, self.r, self.c, self.by_row)
        aux_2 = Myarray1(self.elems, self.r, self.c, self.by_row)
        det = 0
        if self.r != self.c:
            det = None
        elif self.r *self.c == 4:
            det = aux.get_elem(1, 1) * aux.get_elem(2, 2) - aux.get_elem(1, 2)  * aux.get_elem(2, 1)
        else:
            for fila in range(self.r):
                """Quiero que la primera fila quede fija. Lo que va a ir variando
                son las columnas que se van eliminando. Mi función del crea un nuevo
                objeto eliminando la fila,columna, entonces tengo que ir reasignándola"""
                primer_elemento = aux.get_elem(1, fila + 1)
                aux_2 = aux.del_col(fila + 1 )
                aux_2 = aux_2.del_row(1)
                det += aux_2.det() * primer_elemento * (-1) ** fila
        return det


    def myprint(self):
        """
        Imprime la matriz
        
        Returns
        -------
        None.

        """
        print('\n')
        for k in range(1,self.r+1):
            print(self.get_row(k))
        print('\n')
        return None


#%%
if __name__ == "__main__":
    
    a = [0,3,11,19,20,1,8,13,15,21,2,9,16,12,32]
    a_1 = Myarray1(a,3,5,True)
    print(f'La lista de elementos es la siguiente: \n {a}')
    print(f'Las dimensiones de la matriz son {a_1.r} x {a_1.c}')
    
    print('Si by_row = True, la matriz es la siguiente:')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('Si by_row = False, la matriz es la siguiente:')
    a_1.by_row = False
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_POS')
    print(a_1.elems)
    a_1.by_row = True
    print(f'Si by_row = True, el elemento (2,5) de la matriz corresponde al índice: {a_1.get_pos(2, 5)}')
    a_1.by_row = False
    print(f'Si by_row = False, el elemento (2,5) de la matriz corresponde al índice: {a_1.get_pos(2, 5)}')
    print('_______________________________________\n')
    
    print('GET_COORDS')
    a_1.by_row = True
    a_1.myprint()
    print(a_1.elems)
    print(f' Si by_row = True, el indice 4 de la lista se corresponde con las coordenadas {a_1.get_coords(4)}')
    print('_______________________________________\n')
    
    print('GET_COORDS')
    a_1.by_row = False
    a_1.myprint()
    print(a_1.elems)
    print(f' Si by_row = False, el indice 4 de la lista se corresponde con las coordenadas {a_1.get_coords(4)}')
    print('_______________________________________\n')
    
    print('SWITCH')
    a_1.by_row = True
    a_2 = a_1.switch()
    print('\n')
    print(f' {a_1.elems} con by_row = {a_1.by_row}')
    print('La función Switch altera la lista y el valor de verdad pero la matriz es la misma')
    print(f'La nueva lista es: {a_2.elems} con by_row = {a_2.by_row}')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('GET_ROW')
    print(f' El contenido de la fila 3 de la matriz es: {a_1.get_row(3)} con by_row = {a_1.by_row}')
    a_1.myprint()
    a_1.by_row = False
    print(f' El contenido de la fila 3 de la matriz es: {a_1.get_row(3)} con by_row = {a_1.by_row}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_COL')
    a_1.by_row = True
    print(f' El contenido de la columna 4 de la matriz es: {a_1.get_col(4)} con by_row = {a_1.by_row}')
    a_1.myprint()
    a_1.by_row = False
    print(f' El contenido de la columna 4 de la matriz es: {a_1.get_col(4)} con by_row = {a_1.by_row}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_ELEM')
    a_1.by_row = True
    print(f'El elemento ubicado en las coordenadas (3,1) es: {a_1.get_elem(3,1)} con by_row = {a_1.by_row}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_ELEM')
    a_1.by_row = False
    print(f'El elemento ubicado en las coordenadas (3,1) es: {a_1.get_elem(3,1)} con by_row = {a_1.by_row}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('DEL_COL')
    a_1.by_row = True
    a_2 = a_1.del_col(4)
    a_1.myprint()
    print(f'La matriz sin la columna 4 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DEL_COL')
    a_1.by_row = False
    a_2 = a_1.del_col(4)
    a_1.myprint()
    print(f'La matriz sin la columna 4 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DEL_ROW')
    a_1.by_row = True
    a_2 = a_1.del_row(2)
    a_1.myprint()
    print(f'La matriz sin la fila 2 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DEL_ROW')
    a_1.by_row = False
    a_2 = a_1.del_row(2)
    a_1.myprint()
    print(f'La matriz sin la fila 2 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_ROWS')
    a_1.by_row = True
    a_2 = a_1.swap_rows(2,3)
    a_1.myprint()
    print(f'La matriz con las filas 2 y 3 intercambiadas  con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_ROWS')
    a_1.by_row = False
    a_2 = a_1.swap_rows(2,3)
    a_1.myprint()
    print(f'La matriz con las filas 2 y 3 intercambiadas con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_COLS')
    a_1.by_row = True
    a_2 = a_1.swap_cols(2,5)
    a_1.myprint()
    print(f'La matriz con las columnas 2 y 5 intercambiadas  con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_COLS')
    a_1.by_row = False
    a_2 = a_1.swap_cols(2,5)
    a_1.myprint()
    print(f'La matriz con las columnas 2 y 5 intercambiadas con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SCALE_COL')
    a_1.by_row = True
    a_2 = a_1.scale_col(3,5)
    a_1.myprint()
    print(f'La matriz con la columna 3 multiplicada 5 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SCALE_COL')
    a_1.by_row = False
    a_2 = a_1.scale_col(3,5)
    a_1.myprint()
    print(f'La matriz con la columna 3 multiplicada 5 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')

    print('SCALE_ROW')
    a_1.by_row = True
    a_2 = a_1.scale_row(1,4)
    a_1.myprint()
    print(f'La matriz con la fila 1 multiplicada 4 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SCALE_ROW')
    a_1.by_row = False
    a_2 = a_1.scale_row(1,4)
    a_1.myprint()
    print(f'La matriz con la fila 1 multiplicada 4 con by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('TRANSPOSE')
    a_1.by_row = True
    a_2 = a_1.Transpose()
    a_1.myprint()
    print(f'La matriz traspuesta by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('TRANSPOSE')
    a_1.by_row = False
    a_2 = a_1.Transpose()
    a_1.myprint()
    print(f'La matriz traspuesta by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')

    print('FLIP COLS')
    a_1.by_row = True
    a_2 = a_1.flip_cols()
    a_1.myprint()
    print(f'La matriz con las columnas intercambiadas by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('FLIP COLS')
    a_1.by_row = False
    a_2 = a_1.flip_cols()
    a_1.myprint()
    print(f'La matriz con las columnas intercambiadas by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('FLIP ROWS')
    a_1.by_row = True
    a_2 = a_1.flip_rows()
    a_1.myprint()
    print(f'La matriz con las filas intercambiadas by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')

    print('FLIP ROWS')
    a_1.by_row = False
    a_2 = a_1.flip_rows()
    a_1.myprint()
    print(f'La matriz con las filas intercambiadas by_row = {a_2.by_row} es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DET')
    b = [1,2,3,4,5,6,7,8,9]
    a_1 = Myarray1(b, 3, 3, True)
    a_2 = a_1.det()
    a_1.myprint()
    print(f'El determinante de la matriz es {a_2}')

