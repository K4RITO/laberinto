import tkinter as tk

def menu_principal(ventana, frame):
    frame.destroy()
    frame = tk.Frame(ventana)
    frame.pack(expand=True)
    titulo = tk.Label(frame, text="Laberinto", font=("Arial", 24))
    titulo.pack(pady=20)

    boton_empezar = tk.Button(frame, text="Empezar", font=("Arial", 16), command=lambda: empezar_laberinto(ventana, frame))
    boton_empezar.pack(pady=10)
    boton_salir = tk.Button(frame, text="Salir", font=("Arial", 16), command=ventana.destroy)
    boton_salir.pack(pady=10)