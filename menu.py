import tkinter as tk
from main import *
import random
import copy

LABERINTOS = [laberinto, laberinto2, laberinto3, laberinto4, laberinto_sin_salida]  # Lista de laberintos disponibles

def menu_principal(ventana, frame):
    frame.destroy()
    frame = tk.Frame(ventana)                                      #Crea un nuevo frame para el menú principal
    frame.pack(expand=True)                                        #Empaqueta el frame para que se expanda y se centre en la ventana
    titulo = tk.Label(frame, text="Laberinto", font=("Arial", 24))
    titulo.pack(pady=20)                                           #Agrega un título al frame con un margen vertical de 20 píxeles

    boton_empezar = tk.Button(frame, text="Empezar", font=("Arial", 16), command=lambda: empezar_laberinto(ventana, frame))
    boton_empezar.pack(pady=10)
    boton_salir = tk.Button(frame, text="Salir", font=("Arial", 16), command=ventana.destroy)
    boton_salir.pack(pady=10)

def empezar_laberinto(ventana, frame):
    frame.destroy()
    frame = tk.Frame(ventana)
    frame.pack(expand=True)

    lab_original = random.choice(LABERINTOS)  # Selecciona un laberinto aleatorio de la lista de laberintos
    lab = copy.deepcopy(lab_original)         # Crea una copia del laberinto original para poder modificarlo sin afectar el original
    recorrido.clear()                         # Limpia el recorrido previo antes de iniciar un nuevo laberinto

    fila, columnas = len(lab), len(lab[0])
    celda = 25
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

    tk.Button(frame, text="Jugar de nuevo", font=("Arial", 12), command=lambda: empezar_laberinto(ventana, frame)).pack(pady=5)
    tk.Button(frame, text="Volver al menú", font=("Arial", 12), command=lambda: menu_principal(ventana, frame)).pack(pady=5)