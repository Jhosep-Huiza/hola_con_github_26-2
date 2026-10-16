import tkinter as tk
from tkinter import PhotoImage, ttk
from tkinter import messagebox

class SistemaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()

        self.ventana.geometry("1200x600+200+100")

        self.ventana.iconbitmap("./iconos/icono.ico")
        self.ventana.config(bg="#ffffff")
        #self.objeto = DatabaseManager("./BaseDatos/sistema.db")
        self.ventana.resizable(False, False)
        self.ventana.protocol("WM_DELETE_WINDOW", self.confirmar_salida)
        self.ventana.wm_attributes("-alpha", 0.93)
    
        # Menú vertical
        self.menu_vertical = tk.Frame(self.ventana,  bg="#1f3c88", width=200)
        self.menu_vertical.pack(side="left", fill="y")
    
        # logo institucional
        try:
            self.logo = tk.PhotoImage(file="./imagenes/logo2.png")
            label_img = tk.Label(self.menu_vertical, image=self.logo,text="MI SISTEMA", bg="#1f3c88", fg="white")
            label_img.pack(pady=5)
        except:
            pass  # si no encuentra imagen no rompe
    
        # Frame para las interfaces
        self.contenido = tk.Frame(self.ventana, bg="#fff")
        self.contenido.pack(side="right", fill="both", expand=True)
    
        #creacion de objetos
        #self.usuario = UsuarioView(self.contenido, self.objeto, ventana=self.ventana)
        #self.sumita = SumaView(self.contenido, self.objeto)
        #self.triangulito = TrianguloView(self.contenido, self.objeto)
    
    
    
        # Botones del menú
        btn_inicio = tk.Button( self.menu_vertical, text="🏠 Inicio", command=self.mostrar_inicio,
            width=20 )
        btn_inicio.pack(pady=10)
    
        btn_inicio.config(bg="#2c5282", fg="#ffffff", font=("Verdana", 12, "bold"), bd=0, cursor="hand2",
            activebackground="#1a365d", activeforeground="white" )
        btn_registro = tk.Button(self.menu_vertical, text="👤Registro de Usuarios", command="", width=20)#self.usuario.mostrar
        btn_registro.pack(pady=10)
        btn_registro.config(bg="#2c5282", fg="#ffffff", font=("Verdana", 12, "bold"), bd=0, cursor="hand2",
                            activebackground="#1a365d",activeforeground="white" )
    
        btn_suma = tk.Button(self.menu_vertical, text="➕Sumar Dos Números", command="", width=20)#self.sumita.mostrar
        btn_suma.pack(pady=10)
        btn_suma.config(bg="#2c5282", fg="#ffffff", font=("Verdana", 12, "bold"), bd=0, cursor="hand2",
                        activebackground="#1a365d",
                        activeforeground="white"
                        )
    
        btn_triangulo = tk.Button(self.menu_vertical, text="🔺Triángulo", command="", width=20)#self.triangulito.mostrar
        btn_triangulo.pack(pady=10)
        btn_triangulo.config(bg="#2c5282", fg="#ffffff", font=("Verdana", 12, "bold"), bd=0, cursor="hand2",
                            activebackground="#1a365d",
                            activeforeground="white"
                            )
    
        btn_salir = tk.Button(self.menu_vertical, text="🛑Salir", command=self.confirmar_salida, width=20)
        btn_salir.pack(pady=10)
        btn_salir.config(bg="#2c5282", fg="#ffffff", font=("Verdana", 12, "bold"), bd=0, cursor="hand2",
                        activebackground="#1a365d",
                        activeforeground="white"
                        )
    
        self.mostrar_inicio()
    
        self.ventana.mainloop()
 
    def mostrar_inicio(self):
        # Limpiar contenido
        for widget in self.contenido.winfo_children():
            widget.destroy()
    
        # Fondo pastel
        self.contenido.config(bg="#eaf3ff")
    
        # Frame centrado
        frame_central = tk.Frame(self.contenido, bg="#eaf3ff")
        frame_central.place(relx=0.5, rely=0.5, anchor="center")
    
        # Imagen (asegúrate de tener una imagen en /iconos/)
        try:
            self.img_inicio = tk.PhotoImage(file="./imagenes/logo2.png")
            label_img = tk.Label(frame_central, image=self.img_inicio, bg="#eaf3ff")
            label_img.pack(pady=10)
        except:
            pass  # si no encuentra imagen no rompe
    
        # Título principal
        titulo = tk.Label(
            frame_central,
            text="Bienvenido al Sistema Principal",
            font=("Verdana", 24, "bold"),
            bg="#eaf3ff",
            fg="#1f3c88"
        )
        titulo.pack(pady=10)
    
        # Subtítulo
        subtitulo = tk.Label(
            frame_central,
            text="Sistema de Gestión Académica",
            font=("Verdana", 14),
            bg="#eaf3ff",
            fg="#555"
        )
        subtitulo.pack(pady=5)
    
        # Línea decorativa
        linea = tk.Frame(frame_central, bg="#3273db", height=3, width=400)
        linea.pack(pady=15)
    
    
    
    def confirmar_salida(self):
        respuesta = messagebox.askyesno(
            "Confirmar salida",
            "¿Estás seguro de salir del sistema?"
        )
    
        if respuesta:  # Si presiona "Sí"
            self.ventana.destroy()
            