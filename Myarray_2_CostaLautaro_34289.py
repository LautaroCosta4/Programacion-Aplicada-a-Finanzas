# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 09:45:52 2023

@author: costa
"""

class Myarray_2:
    """Todas las funciones que requieran el uso de las coordenadas matriciales,
    se manejan conforme a las matemáticas y no al indexing de Python."""
    def __init__(self, lista,r,c):
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
        
        Returns
        -------
        None.
        """
        self.elems = lista
        self.r = r
        self.c = c
        
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
        if len(self.elems) != self.r or any(len(self.elems[i]) != self.c for i in range(self.r)):
            salida = False
        else:
            salida = True
        return salida

    def get_pos (self,j,k):
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
        pos : tuple
            Devuelve la posicion asociada en la lista de elementos de la matriz
        """
        if self.verificacion() and j<= self.r and k<= self.c:
            pos = (j-1,k-1)
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return pos


    def get_row(self,j):
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
        if self.verificacion() and j<= self.r:
            row = self.elems[j-1]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return row


    def get_row2 (self,j):
        """
        A partir de determinadas filas, construye la submatriz correspondiente

        Parameters
        ----------
        j : list
            Contiene las filas con las cuales se formará la submatriz

        Raises
        ------
        ValueError
            Se produce este error en caso de que el parámetro j no sea una lista,
            si algun elemento de dicha lista excede el número de filas de la matriz o,
            en caso de que la matriz haya sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto con la submatriz correspondiente

        """
        if type(j) == list and all(i <= self.r for i in j):
            submatriz = [self.get_row(i) for i in j]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(submatriz, len(j), self.c)
    
    def get_col(self,k):
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
        if self.verificacion() and k<= self.c:
            col = [lista[k-1] for lista in self.elems]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return col
    
    def get_col2 (self,k):
        """
        A partir de determinadas columnas, construye la submatriz correspondiente

        Parameters
        ----------
        k : list
            Contiene las columnas con las cuales se formará la submatriz

        Raises
        ------
        ValueError
            Se produce este error en caso de que el parámetro k no sea una lista,
            si algun elemento de dicha lista excede el número de columnas de la matriz o,
            en caso de que la matriz haya sido creada mal inicialmente.

        Returns
        -------
        Devuelve un objeto con la submatriz correspondiente

        """
        if type(k) == list and all(i <= self.c for i in k):
            submatriz = [self.get_col(i) for i in k]
            elems = list(map(list, zip(*submatriz)))
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(elems, self.r, len(k))
        
    def get_elem (self,t):
        """
        Reutiliza la función get_row para posicionarse sobre la fila de la cual
        se desea extraer un elemento en particular.

        Parameters
        ----------
        t : lista
            lista que contiene las coordenadas de un elemento de la matriz al 
            cual se desea acceder.

        Raises
        ------
        ValueError
            Se produce este error en caso de que el parámetro t no sea una lista,
            si la primer coordenada excede el número de filas de la matriz,
            si la segunda coordenada excede el número de columnas de la matriz o,
            en caso de que la matriz haya sido creada mal inicialmente.

        Returns
        -------
        elem : int
            Elemento de la matriz correspondiente a las coordenadas t.

        """
        if type(t) == list and t[0]<= self.r and t[-1]<= self.c:
            elem = self.get_row(t[0])[t[-1] -1]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return elem 
    
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
        if self.verificacion() and j<=self.r:
            submatriz = self.elems[: j-1]+self.elems[j:]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return  Myarray_2 (submatriz ,self.r - 1,self.c)
    
    def del_col (self,k):
        """
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
        if self.verificacion() and k<= self.c:
            submatriz = [lista[: k-1] + lista [k:] for lista in self.elems]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(submatriz, self.r, self.c - 1)
    
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
        if self.verificacion() and j<=self.r:
            aux = self.elems.copy()
            aux[j-1] = [i * x for i in self.get_row(j)]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(aux, self.r, self.c)
    
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
        if self.verificacion() and k<= self.c:
            aux = [fila[:] for fila in self.elems]
            for i in range(len(aux)):
                aux[i][k-1] *= y
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(aux, self.r, self.c)

    def swap_rows (self,j,k):
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
        if self.verificacion() and j<=self.r and k<= self.r:
            aux = self.elems.copy()
            aux[j-1],aux[k-1] = aux[k-1],aux[j-1]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(aux, self.r, self.c)
    
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
        if self.verificacion() and l<=self.c and m<= self.c:
            aux = [fila[:] for fila in self.elems]
            for i in range(len(aux)):
                aux[i][l-1],aux[i][m-1] = aux[i][m-1],aux[i][l-1]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(aux, self.r, self.c)
    
    def transpose (self):
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
            elems = list(map(list,zip(*self.elems)))
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(elems, self.c, self.r)
    
    def flip_cols(self):
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
        if self.verificacion():
            elems = [list(reversed(lista)) for lista in self.elems ]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(elems, self.r, self.c)
    
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
        if self.verificacion():
            aux = [fila[:] for fila in self.elems]
            for i in range(self.r//2) :
                aux[i], aux[-(1+i)] = self.elems[-(i+1)], self.elems[i]
        else:
            raise ValueError('Los valores fueron ingresados incorrectamente')
        return Myarray_2(aux, self.r, self.c)
    
    def det (self):
        """
        Calcula el determinante de la matriz

        Returns
        -------
        det : int
            Determinante.

        """
        aux = Myarray_2(self.elems, self.r, self.c)
        aux_2 = Myarray_2(self.elems, self.r, self.c)
        det = 0
        if self.r != self.c:
            det = None
        elif self.r *self.c == 4:
            det = aux.get_elem([1, 1]) * aux.get_elem([2, 2]) - aux.get_elem([1, 2])  * aux.get_elem([2, 1])
        else:
            for fila in range(self.r):
                """Quiero que la primera fila quede fija. Lo que va a ir variando
                son las columnas que se van eliminando. Mi función del crea un nuevo
                objeto eliminando la fila,columna, entonces tengo que ir reasignándola"""
                primer_elemento = aux.get_elem([1, fila + 1])
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
    
    a = [[1,2,3],[4,5,6],[7,8,9]]
    a_1 = Myarray_2(a,3,3)
    print(f'La lista de elementos es la siguiente: \n {a}')
    print(f'Las dimensiones de la matriz son {a_1.r} x {a_1.c}')
    print('La matriz es la siguiente:')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_POS')
    print(a_1.elems)
    print(f'El elemento (2,2) de la matriz corresponde al índice: {a_1.get_pos(2, 2)}')
    print('_______________________________________\n')
    
    print('GET_COORDS')
    print('No se hizo la funcion get_coords por el enfoque de trabajar con lista de listas ')
    print('_______________________________________\n')
    
    print('SWITCH')
    print('No se hizo la funcion switch por el enfoque de trabajar con lista de listas')
    #Prácticamente viene predefinido by_row = True
    print('_______________________________________\n')
    
    print('GET_ROW')
    print(f' El contenido de la fila 3 de la matriz es: {a_1.get_row(3)}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_COL')
    
    print(f' El contenido de la columna 2 de la matriz es: {a_1.get_col(2)}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('GET_ELEM')
    print(f'El elemento ubicado en las coordenadas (3,1) es: {a_1.get_elem([3,1])}')
    a_1.myprint()
    print('_______________________________________\n')
    
    print('DEL_COL')
    a_2 = a_1.del_col(3)
    a_1.myprint()
    print('La matriz sin la columna 3 es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DEL_ROW')
    a_2 = a_1.del_row(3)
    a_1.myprint()
    print('La matriz sin la fila 3 es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_ROWS')
    a_2 = a_1.swap_rows(2,3)
    a_1.myprint()
    print('La matriz con las filas 2 y 3 intercambiadas es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SWAP_COLS')
    a_2 = a_1.swap_cols(1,3)
    a_1.myprint()
    print('La matriz con las columnas 1 y 3 intercambiadas es:')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SCALE_COL')
    a_2 = a_1.scale_col(3,5)
    a_1.myprint()
    print('La matriz con la columna 3 multiplicada 5 es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('SCALE_ROW')
    a_2 = a_1.scale_row(1,4)
    a_1.myprint()
    print('La matriz con la fila 1 multiplicada 4 es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('TRANSPOSE')
    a_2 = a_1.transpose()
    a_1.myprint()
    print('La matriz traspuesta  es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('FLIP COLS')
    a_2 = a_1.flip_cols()
    a_1.myprint()
    print('La matriz con las columnas intercambiadas es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('FLIP ROWS')
    a_2 = a_1.flip_rows()
    a_1.myprint()
    print('La matriz con las filas intercambiadas es')
    a_2.myprint()
    print('_______________________________________\n')
    
    print('DET')
    a_2 = a_1.det()
    a_1.myprint()
    print(f'El determinante de la matriz es {a_2}')

