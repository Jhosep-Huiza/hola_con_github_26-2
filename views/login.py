from tkinter import * 
import tkinter as tk
from tkinter import ttk

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