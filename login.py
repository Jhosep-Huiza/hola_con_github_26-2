from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from typing import Self
from views.sistema_principal import *

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
            
        def Ingresar():
            try:
                if(self.user.get() == "" or self.pas.get() == ""):
                    messagebox.showerror("Error", "Debe ingresar usuario y contraseña")
                else:
                    usuario = self.user.get()
                    clave = self.pas.get()

                    if usuario == "admin" and clave == "1234":
                        messagebox.showinfo("Exito", "¡Inicio de sesión exitoso!, credenciales correctas")
                        self.ven.destroy()
                        SistemaPrincipal()
                    else:
                        messagebox.showerror("Login", "Usuario o contraseña incorrectos")
            except:
                messagebox.showerror("Error", "Error al intentar iniciar sesión")

        #Ponemos un boton de salit
        self.btnSalir = tk.Button(self.ven, text="X", width=6, height=2, command=Salir)
        self.btnSalir.place(x=290, y=5)
        self.btnSalir.config(bg="#FF0000", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", cursor="hand2")

        #variables
        self.user = tk.StringVar()
        self.pas = tk.StringVar()

        #imagenes
        self.img = tk.PhotoImage(file="imagenes/logo2.png")

        #etiquetas
        #eqtiqueta para la imagen
        self.lblLogo = tk.Label(self.ven, image=self.img)
        self.lblLogo.place(x=140, y=60)
        self.lblLogo.config(bg="#00FFFF")

        self.lblTitulo = tk.Label(self.ven, text="ACCESO", font=("Arial", 20, "bold"))
        self.lblTitulo.place(x=140, y=170)
        self.lblTitulo.config(bg="#00FFFF")

        self.lblUser = tk.Label(self.ven, text="USUARIO", font=("Arial", 17, "bold"))
        self.lblUser.place(x=60, y=210)
        self.lblUser.config(bg="#00FFFF")
        self.txtUser = tk.Entry(self.ven, textvariable=self.user, font=("Arial", 15))
        self.txtUser.place(x=60, y=240, width=230, height=30)
        self.txtUser.config(bg="#FFFFFF")

        self.lblPass = tk.Label(self.ven, text="CONTRASEÑA", font=("Arial", 17, "bold"))
        self.lblPass.place(x=60, y=280)
        self.lblPass.config(bg="#00FFFF")
        self.txtPass = tk.Entry(self.ven, textvariable=self.pas, font=("Arial", 15), show="*")
        self.txtPass.place(x=60, y=310, width=230, height=30)
        self.txtPass.config(bg="#FFFFFF")

        self.btnIngresar = tk.Button(self.ven, text="INGRESAR", width=20, height=2, command=Ingresar)
        self.btnIngresar.place(x=90, y=360)
        self.btnIngresar.config(bg="#FF0000", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", cursor="hand2")