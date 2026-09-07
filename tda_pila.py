class nodopila:
    """clase nodo pila."""
    info, sig = None, None

class pila:
    """clase pila."""
    def __init__(self):
        """Crea pila vacia."""
        self.cima = None
        self.tamanio = 0

def apilar(pila, dato):
    """Apila un dato sobre la cima de la pila."""
    nodo = nodopila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    """Desapila el dato en la cima de la pila y lo devuelve."""
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    """Devuelve True si la pila esta vacia."""
    return pila.cima is None

def en_cima(pila):
    """devuelve el valor almacenado en la cima de la pila."""
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None
    
def tamanio(pila):
    """devuelve el numero de elementos en la pila."""
    return pila.tamanio

def barrido(p):
    """muestra el contenido de la pila sin perder los datos"""
    paux = pila()

    while (not pila_vacia(p)):
        dato = desapilar(p)
        print(dato)
        apilar(paux, dato)
    
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(p, dato)