from tkinter import * 
import tkinter as tk
from tkinter import ttk
from typing import Self

class Login(ttk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)

        self.ven = ventana
        self.ven.geometry("350x450")
        self.ven.title("Sistema Login")
        self.ven.config(bg="#00FFFF")
        self.ven.resizable(False, False)
        self.ven.wm_attributes("-alpha", 0.9)
        self.ven.iconbitmap("iconos/icono.ico")

        #Quitamos la barra de menu
        self.ven.overrideredirect(True)

        def Salir():
            self.ven.destroy()

        #Ponemos un boton de salit
        self.btnSalir = tk.Button(self.ven, text="X", width=6, height=2, command=Salir)
        self.btnSalir.place(x=290, y=5)
        self.btnSalir.config(bg="#FF0000", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", cursor="hand2")