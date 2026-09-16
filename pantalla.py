import tkinter as tk
from menu import menu_principal

ventana = tk.Tk()
ventana.title("Laberinto")
ventana.geometry("1080x720")

frame = tk.Frame(ventana)
frame.pack(expand=True)

menu_principal(ventana, frame)

ventana.mainloop()
