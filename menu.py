import tkinter as tk
from tkinter import ttk
from main import *
import copy
import sys

sys.setrecursionlimit(10000)  # Aumentamos el límite de recursión para permitir laberintos más grandes


LABERINTOS = {
    "Laberinto 1": laberinto,
    "Laberinto 2": laberinto2,
    "Laberinto 3": laberinto3,
    "Laberinto 4": laberinto4,
    "Sin salida": laberinto_sin_salida
}  # Diccionario que contiene los laberintos disponibles para el juego, con sus nombres como claves y las matrices correspondientes como valores.

def menu_principal(ventana, frame):
    frame.destroy()
    frame = tk.Frame(ventana)                                      #Crea un nuevo frame para el menú principal
    frame.pack(expand=True)                                        #Empaqueta el frame para que se expanda y se centre en la ventana
    titulo = tk.Label(frame, text="Laberinto", font=("Arial", 24))
    titulo.pack(pady=20)                                           #Agrega un título al frame con un margen vertical de 20 píxeles


    lbl_instruccion = tk.Label(frame, text="Selecciona un laberinto:", font=("Arial", 14, "bold"))
    lbl_instruccion.pack(pady=(10, 2))                                   #Agrega una etiqueta de instrucción al frame con un margen vertical de 10 píxeles
    seleccion_laberinto = tk.StringVar(value=list(LABERINTOS.keys())[0])          #Variable que almacena la selección del laberinto
    combo = ttk.Combobox(frame, textvariable=seleccion_laberinto, values=list(LABERINTOS.keys()),state="readonly", font=("Arial", 12))  #Crea un despegable para seleccionar el laberinto
    combo.pack(pady=5)

    boton_empezar = tk.Button(frame, text="Laberinto automatico", font=("Arial", 16), command=lambda: empezar_laberinto(ventana, frame, seleccion_laberinto.get()))  #Crea un botón para empezar el laberinto automático
    boton_empezar.pack(pady=10)
    boton_manual = tk.Button(frame, text="Laberinto manual", font=("Arial", 16), command=lambda: laberinto_manual(ventana, frame, seleccion_laberinto.get()))  #Crea un botón para empezar el laberinto manual
    boton_manual.pack(pady=10)
    boton_salir = tk.Button(frame, text="Salir", font=("Arial", 16), command=ventana.destroy)
    boton_salir.pack(pady=10)

def empezar_laberinto(ventana, frame, nombre_lab):
    frame.destroy()
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    lab = copy.deepcopy(LABERINTOS[nombre_lab])         # Crea una copia del laberinto original para poder modificarlo sin afectar el original
    recorrido.clear()                         # Limpia el recorrido previo antes de iniciar un nuevo laberinto

    fila, columnas = len(lab), len(lab[0])
    celda = 12
    canvas = tk.Canvas(frame, width=columnas * celda, height=fila * celda, bg="white")
    canvas.pack(pady=10)

    configurar_canvas(canvas, celda)            # Configura el canvas para dibujar el laberinto


    # Buscamos automáticamente dónde está el inicio (valor 4) en la matriz,
    # en vez de asumir que siempre está en [0, 1] (por ejemplo, en
    # laberinto3 y laberinto_sin_salida el inicio está en otra fila).
    inicio = next((i, j) for i, fila in enumerate(lab) for j, valor in enumerate(fila) if valor == 4)
    resultado = backtrack(lab, list(inicio))
    mensaje = "¡Has salido del laberinto!" if resultado else "No hay salida en este laberinto."
    tk.Label(frame, text=mensaje, font=("Arial", 14), fg="green" if resultado else "red").pack(pady=5)

    tk.Button(frame, text="Jugar de nuevo", font=("Arial", 12), command=lambda: empezar_laberinto(ventana, frame, nombre_lab)).pack(pady=5)
    tk.Button(frame, text="Volver al menú", font=("Arial", 12), command=lambda: menu_principal(ventana, frame)).pack(pady=5)

def laberinto_manual(ventana, frame, nombre_lab):
    frame.destroy()
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    lab = copy.deepcopy(LABERINTOS[nombre_lab])
    filas, columnas = len(lab), len(lab[0])

    celda = 12
    canvas = tk.Canvas(frame, width=columnas * celda, height=filas * celda, bg="white")
    canvas.pack(pady=10)

    inicio = next((i, j) for i, f in enumerate(lab) for j, v in enumerate(f) if v == 4)
    # Guardamos el estado del jugador en un dict para poder modificarlo
    # desde las funciones internas (dibujar/mover) sin usar "global".
    jugador = {"pos": list(inicio), "activo": True}

    etiqueta = tk.Label(frame, text="Usá las flechas del teclado para moverte",font=("Arial", 12))
    etiqueta.pack(pady=5)

    def dibujar():
        canvas.delete("all")
        for i, fila_ in enumerate(lab):
            for j, valor in enumerate(fila_):
                x0, y0 = j * celda, i * celda
                x1, y1 = x0 + celda, y0 + celda
                color = COLORES_CANVAS.get(valor, "white")
                canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="gray")

        # Dibujamos al jugador arriba de todo, como un círculo naranja
        pi, pj = jugador["pos"]
        canvas.create_oval(
            pj * celda + 2, pi * celda + 2,
            pj * celda + celda - 2, pi * celda + celda - 2,
            fill="orange", outline="black",
        )

    def mover(dr, dc):
        if not jugador["activo"]:
            return  # ya ganó (o el juego terminó); ignoramos más teclas

        pi, pj = jugador["pos"]
        ni, nj = pi + dr, pj + dc

        # Chequeamos límites de la matriz y que la celda destino no sea pared (1)
        if 0 <= ni < filas and 0 <= nj < columnas and lab[ni][nj] != 1:
            jugador["pos"] = [ni, nj]
            if lab[ni][nj] == 5:
                jugador["activo"] = False
                etiqueta.config(text="¡Llegaste a la salida!", fg="green")

        dibujar()

    ventana.bind("<Up>", lambda e: mover(-1, 0))
    ventana.bind("<Down>", lambda e: mover(1, 0))
    ventana.bind("<Left>", lambda e: mover(0, -1))
    ventana.bind("<Right>", lambda e: mover(0, 1))

    dibujar()

    def volver():
        # Desenganchamos las teclas para que no sigan disparando "mover"
        # cuando ya estamos en otra pantalla.
        for tecla in ("<Up>", "<Down>", "<Left>", "<Right>"):
            ventana.unbind(tecla)
        menu_principal(ventana, frame)

    tk.Button(frame, text="Volver al menú", font=("Arial", 12), command=volver).pack(pady=5)