from tda_cola import cola, arribo, atencion, cola_vacia, en_frente,barrido_cola
from tda_pila import pila, apilar, desapilar, pila_vacia, en_cima,barrido_pila
from tda_lista import insertar, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

laberinto = [[1,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

recorrido = pila()


inicio = 0, 1

fila = 0
columna = 1

def posicion(fila,columna):
    return laberinto[fila][columna]

def recorrer_laberinto(valor):

    if valor == 2:
        return 2
    elif posicion:
        return  valor

recorrer_laberinto(posicion)        




             