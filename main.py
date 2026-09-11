import time

# Laberintos

laberinto = [
    [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,1,1,1,1]
]

laberinto2  = [
    [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1]
]

laberinto3  = [
    [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [5,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

laberinto4  = [
    [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

laberinto_sin_salida  = [
    [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [5,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# colores para los prints
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"
MAGENTA = '\033[35m'

# Nuevo soporte opcional de canvas, no rompe el uso de consola, pero permite visualizar el laberinto en una ventana de tkinter.
canvas = None
tam_celda = 25
COLORES_CANVAS = {
    0: "green",      # Camino libre
    1: "red",        # Pared
    2: "yellow",     # Camino activo
    3: "lightgray",  # Camino sin salida
    4: "blue",       # Casilla de inicio / origen
    5: "blue"        # Casilla de salida / meta
}

def configurar_canvas(nuevo_canvas, celda=25):
    "Le dice al módulo que se va a usar canvas y lo configura con el tamaño del laberinto."
    global canvas, tam_celda
    canvas = nuevo_canvas
    tam_celda = celda
#-----------------------------------------------------------------------------------------------

# funcion para mostrar el laberinto con colores distinguidos por consola

def mostrar_laberinto(lab):
    #Se chequea si se ha configurado un canvas para dibujar el laberinto en una ventana de tkinter.
    if canvas is not None:
        canvas.delete("all")                                   #Borra el contenido previo del canvas.
        for i, fila in enumerate(lab):
            for j, valor in enumerate(fila):
                x0, y0 = j * tam_celda, i * tam_celda          #Calcula las coordenadas de la esquina superior izquierda del rectángulo.
                x1, y1 = x0 + tam_celda, y0 + tam_celda        #Calcula las coordenadas de la esquina inferior derecha del rectángulo.
                canvas.create_rectangle(x0, y0, x1, y1, fill=COLORES_CANVAS.get(valor, "white"), outline="black")   #Dibuja un rectángulo en el canvas con el color correspondiente al valor de la celda.
        canvas.update()  #Actualiza el canvas para reflejar los cambios realizados.
        return
    """
    Recibe el laberinto por parametro e imprime cada uno de sus caracteres con el color especifico.
    """
    for fila in lab:
        for numero in fila:

            if numero == 0:
                print(f"{VERDE}0{RESET}", end=" ")

            elif numero == 1:
                print(f"{ROJO}1{RESET}", end=" ")

            elif numero == 2:
                print(f"{AMARILLO}2{RESET}", end=" ")

            elif numero == 3:
                print(f"{MAGENTA}3{RESET}", end=" ")

            elif numero == 4:
                print(f"{AZUL}4{RESET}", end=" ")

            elif numero == 5:
                print(f"{AZUL}5{RESET}", end=" ")

        print()

# Lista donde guardaremos los movimientos del algoritmo.
recorrido = []

# funcion recursiva de backtracking
def backtrack(lab: list, pos: tuple, primero=True):
    """
    Resuelve un laberinto mediante búsqueda en profundidad (DFS) y backtracking.

    Navega recursivamente por la matriz del laberinto en orden de prioridad 
    (Derecha, Abajo, Izquierda, Arriba). Marca el camino activo, visualiza el 
    proceso paso a paso y retrocede cuando alcanza un camino sin salida.

    Parameters
    ----------
    lab : list[list[int]]
        Matriz 2D que representa el laberinto. Codificación esperada de celdas:
        - 1: Pared o obstáculo.
        - 2: Camino visitado (camino activo).
        - 3: Camino sin salida (visitado y descartado).
        - 4: Casilla de inicio / origen.
        - 5: Casilla de salida / meta.
    pos : list[int] o tuple[int, int]
        Coordenadas [fila, columna] de la posición actual en la matriz.
    primero : bool, opcional
        Indica si es la llamada inicial desde el origen. Se usa para evitar 
        detectar la casilla inicial (4) como un bloqueo antes de explorar 
        (por defecto es True).

    Returns
    -------
    None
        Imprime en consola si encontró la salida ("salio") o si no existe 
        solución ("No hay salida").

    Side Effects
    ------------
    - Modifica la matriz `lab` in-place cambiando los valores de las celdas.
    - Modifica la lista global `recorrido` agregando o quitando coordenadas.
    - Llama a `limpiar()`, `mostrar_laberinto()` y `time.sleep()` para la animación.

    Notes
    -----
    Prioridad de movimiento en cada paso:
    1. Derecha:  [fila, columna + 1]
    2. Abajo:    [fila + 1, columna]
    3. Izquierda: [fila, columna - 1]
    4. Arriba:   [fila - 1, columna]
    """

    if (lab[pos[0]][pos[1]] == 4 and not primero):
        print("No hay salida")
        return False

    if (lab[pos[0]][pos[1]] == 5):
        print("salio")
        return True
    
    if (lab[pos[0]][pos[1]] != 4): lab[pos[0]][pos[1]] = 2


    mostrar_laberinto(lab)
        
    time.sleep(0.05)
    if (lab[pos[0]][pos[1] + 1] != 1 and lab[pos[0]][pos[1] + 1] not in [2, 3]):
        recorrido.append([pos[0], pos[1]])
        return backtrack(lab, [pos[0], pos[1] + 1], primero=False)
    
    elif (lab[pos[0] + 1][pos[1]] != 1 and lab[pos[0] + 1][pos[1]] not in [2, 3]):
        recorrido.append([pos[0], pos[1]])
        return backtrack(lab, [pos[0] + 1, pos[1]], primero=False)
    
    elif (lab[pos[0]][pos[1]-1] != 1 and lab[pos[0]][pos[1]-1] not in [2, 3]):
        recorrido.append([pos[0], pos[1]])
        return backtrack(lab, [pos[0], pos[1] - 1], primero=False)
        
    elif (lab[pos[0] - 1][pos[1]] != 1 and lab[pos[0] - 1][pos[1]] not in [2, 3]):
        recorrido.append([pos[0], pos[1]])
        return backtrack(lab, [pos[0] - 1, pos[1]], primero=False)

    else:
        lab[pos[0]][pos[1]] = 3
        print()
        return backtrack(lab, recorrido.pop())

if __name__ == "__main__":
    # Solo se ejecuta si el archivo es el principal, no si se importa como módulo.
    # Podes cambiar el nombre del laberinto y la posición inicial para probar otros escenarios.
    backtrack(lab=laberinto, pos=[0, 1])