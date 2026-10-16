import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------- Paleta y fuente ----------
C = {
    "menu": "#1f3c88",
    "menu_hover": "#2a4a9f",
    "menu_activo": "#16306e",
    "acento": "#4da3ff",
    "texto_menu": "#dbe6ff",
    "fondo": "#eef4fc",
    "blanco": "#ffffff",
    "borde": "#d6e4f7",
    "titulo": "#1f3c88",
    "texto": "#334155",
    "gris": "#64748b",
}
FUENTE = "Segoe UI"


def ruta(*partes):
    """Ruta relativa al archivo, funciona sin importar desde dónde se ejecute."""
    return os.path.join(BASE_DIR, *partes)


# ---------- Botón del menú lateral ----------
class BotonMenu(tk.Frame):
    def __init__(self, padre, texto, comando):
        super().__init__(padre, bg=C["menu"])
        self.activo = False

        self.barra = tk.Frame(self, bg=C["menu"], width=4)
        self.barra.pack(side="left", fill="y")

        self.boton = tk.Button(
            self, text=texto, command=comando, anchor="w",
            padx=18, pady=10, bd=0, relief="flat", cursor="hand2",
            font=(FUENTE, 11), bg=C["menu"], fg=C["texto_menu"],
            activebackground=C["menu_hover"], activeforeground="white",
        )
        self.boton.pack(side="left", fill="x", expand=True)
        self.boton.bind("<Enter>", self._entrar)
        self.boton.bind("<Leave>", self._salir)

    def _entrar(self, _):
        if not self.activo:
            self.boton.config(bg=C["menu_hover"])

    def _salir(self, _):
        if not self.activo:
            self.boton.config(bg=C["menu"])

    def activar(self, estado):
        self.activo = estado
        self.boton.config(
            bg=C["menu_activo"] if estado else C["menu"],
            fg="white" if estado else C["texto_menu"],
            font=(FUENTE, 11, "bold" if estado else "normal"),
        )
        self.barra.config(bg=C["acento"] if estado else C["menu"])


# ---------- Aplicación ----------
class SistemaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión Académica")
        self._centrar(1200, 650)
        self.ventana.resizable(False, False)
        self.ventana.config(bg=C["fondo"])
        self.ventana.protocol("WM_DELETE_WINDOW", self.confirmar_salida)

        try:
            self.ventana.iconbitmap(ruta("iconos", "icono.ico"))
        except tk.TclError:
            pass  # sin icono, la app sigue funcionando

        # self.objeto = DatabaseManager(ruta("BaseDatos", "sistema.db"))

        # Secciones: clave -> (texto del menú, título de cabecera, método)
        self.secciones = {
            "inicio": ("🏠   Inicio", "Inicio", self.mostrar_inicio),
            "usuarios": ("👤   Registro de usuarios", "Registro de usuarios", self.mostrar_usuarios),
            "suma": ("➕   Sumar dos números", "Sumar dos números", self.mostrar_suma),
            "triangulo": ("🔺   Triángulo", "Triángulo", self.mostrar_triangulo),
        }
        self.botones = {}

        self._construir_menu()
        self._construir_area_derecha()

        # Aquí crea tus vistas cuando las tengas listas:
        # self.usuario = UsuarioView(self.contenido, self.objeto, ventana=self.ventana)
        # self.sumita = SumaView(self.contenido, self.objeto)
        # self.triangulito = TrianguloView(self.contenido, self.objeto)

        self.ir_a("inicio")
        self._actualizar_reloj()
        self.ventana.mainloop()

    # ---------- Construcción de la interfaz ----------
    def _centrar(self, ancho, alto):
        x = (self.ventana.winfo_screenwidth() - ancho) // 2
        y = (self.ventana.winfo_screenheight() - alto) // 2
        self.ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def _construir_menu(self):
        menu = tk.Frame(self.ventana, bg=C["menu"], width=250)
        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        # Logo y nombre
        cabecera = tk.Frame(menu, bg=C["menu"])
        cabecera.pack(fill="x", pady=(25, 15))
        try:
            self.logo = tk.PhotoImage(file=ruta("imagenes", "logo2.png"))
            tk.Label(cabecera, image=self.logo, bg=C["menu"]).pack()
        except tk.TclError:
            pass
        tk.Label(cabecera, text="MI SISTEMA", bg=C["menu"], fg="white",
                 font=(FUENTE, 15, "bold")).pack(pady=(5, 0))
        tk.Label(cabecera, text="Gestión Académica", bg=C["menu"], fg=C["texto_menu"],
                 font=(FUENTE, 9)).pack()

        tk.Frame(menu, bg=C["menu_hover"], height=1).pack(fill="x", padx=20, pady=(5, 15))

        # Botones de navegación
        for clave, (texto, _titulo, _fn) in self.secciones.items():
            boton = BotonMenu(menu, texto, lambda k=clave: self.ir_a(k))
            boton.pack(fill="x", pady=1)
            self.botones[clave] = boton

        # Salir, anclado abajo
        tk.Frame(menu, bg=C["menu_hover"], height=1).pack(side="bottom", fill="x", padx=20, pady=(0, 15))
        BotonMenu(menu, "🚪   Salir", self.confirmar_salida).pack(side="bottom", fill="x", pady=(0, 5))

    def _construir_area_derecha(self):
        derecha = tk.Frame(self.ventana, bg=C["fondo"])
        derecha.pack(side="right", fill="both", expand=True)

        # Barra superior
        barra = tk.Frame(derecha, bg=C["blanco"], height=60)
        barra.pack(fill="x")
        barra.pack_propagate(False)

        self.lbl_titulo = tk.Label(barra, text="", bg=C["blanco"], fg=C["titulo"],
                                   font=(FUENTE, 17, "bold"))
        self.lbl_titulo.pack(side="left", padx=30)

        self.lbl_reloj = tk.Label(barra, text="", bg=C["blanco"], fg=C["gris"],
                                  font=(FUENTE, 10))
        self.lbl_reloj.pack(side="right", padx=30)

        tk.Frame(derecha, bg=C["borde"], height=1).pack(fill="x")

        # Zona donde se cargan las vistas
        self.contenido = tk.Frame(derecha, bg=C["fondo"])
        self.contenido.pack(fill="both", expand=True)

    # ---------- Navegación ----------
    def ir_a(self, clave):
        for k, boton in self.botones.items():
            boton.activar(k == clave)

        _texto, titulo, funcion = self.secciones[clave]
        self.lbl_titulo.config(text=titulo)

        for widget in self.contenido.winfo_children():
            widget.destroy()
        funcion()

    def _actualizar_reloj(self):
        self.lbl_reloj.config(text=datetime.now().strftime("📅 %d/%m/%Y   🕒 %H:%M:%S"))
        self.ventana.after(1000, self._actualizar_reloj)

    # ---------- Pantallas ----------
    def mostrar_inicio(self):
        centro = tk.Frame(self.contenido, bg=C["fondo"])
        centro.place(relx=0.5, rely=0.46, anchor="center")

        tk.Label(centro, text="Bienvenido al Sistema Principal", bg=C["fondo"],
                 fg=C["titulo"], font=(FUENTE, 26, "bold")).pack()
        tk.Label(centro, text="Sistema de Gestión Académica", bg=C["fondo"],
                 fg=C["gris"], font=(FUENTE, 13)).pack(pady=(4, 0))
        tk.Frame(centro, bg=C["acento"], height=3, width=120).pack(pady=18)

        fila = tk.Frame(centro, bg=C["fondo"])
        fila.pack(pady=10)

        tarjetas = [
            ("👤", "Usuarios", "Registra y administra usuarios.", "usuarios"),
            ("➕", "Suma", "Suma dos números rápidamente.", "suma"),
            ("🔺", "Triángulo", "Calcula datos de un triángulo.", "triangulo"),
        ]
        for icono, titulo, desc, clave in tarjetas:
            self._tarjeta(fila, icono, titulo, desc, clave).pack(side="left", padx=12)

    def _tarjeta(self, padre, icono, titulo, descripcion, clave):
        tarjeta = tk.Frame(padre, bg=C["blanco"], width=215, height=170, cursor="hand2",
                           highlightthickness=1, highlightbackground=C["borde"])
        tarjeta.pack_propagate(False)

        tk.Label(tarjeta, text=icono, bg=C["blanco"], font=(FUENTE, 28)).pack(pady=(22, 4))
        tk.Label(tarjeta, text=titulo, bg=C["blanco"], fg=C["titulo"],
                 font=(FUENTE, 13, "bold")).pack()
        tk.Label(tarjeta, text=descripcion, bg=C["blanco"], fg=C["gris"],
                 font=(FUENTE, 9), wraplength=170).pack(pady=(4, 0))

        def resaltar(activo):
            tarjeta.config(highlightbackground=C["acento"] if activo else C["borde"])

        for w in (tarjeta, *tarjeta.winfo_children()):
            w.bind("<Button-1>", lambda _e, k=clave: self.ir_a(k))
            w.bind("<Enter>", lambda _e: resaltar(True))
            w.bind("<Leave>", lambda _e: resaltar(False))
        return tarjeta

    def _modulo_pendiente(self, icono, nombre):
        caja = tk.Frame(self.contenido, bg=C["blanco"], highlightthickness=1,
                        highlightbackground=C["borde"])
        caja.place(relx=0.5, rely=0.5, anchor="center", width=460, height=240)
        tk.Label(caja, text=icono, bg=C["blanco"], font=(FUENTE, 36)).pack(pady=(35, 5))
        tk.Label(caja, text=nombre, bg=C["blanco"], fg=C["titulo"],
                 font=(FUENTE, 16, "bold")).pack()
        tk.Label(caja, text="Módulo en construcción", bg=C["blanco"], fg=C["gris"],
                 font=(FUENTE, 10)).pack(pady=5)

    def mostrar_usuarios(self):
        # self.usuario.mostrar()
        self._modulo_pendiente("👤", "Registro de usuarios")

    def mostrar_suma(self):
        # self.sumita.mostrar()
        self._modulo_pendiente("➕", "Sumar dos números")

    def mostrar_triangulo(self):
        # self.triangulito.mostrar()
        self._modulo_pendiente("🔺", "Triángulo")

    # ---------- Salida ----------
    def confirmar_salida(self):
        if messagebox.askyesno("Confirmar salida", "¿Estás seguro de salir del sistema?"):
            self.ventana.destroy()


if __name__ == "__main__":
    SistemaPrincipal()