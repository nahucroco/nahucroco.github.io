import tkinter as tk
from tkinter import messagebox

def salir():
    i = messagebox.askquestion("Salir", "¿Esta seguro que desea salir?")
    if i == "yes":
        ventana.destroy()



def programaPrincipal():
    global ventana
    """ def centrar_ventana(ventana):
        ventana.update_idletasks()
        ancho_ventana = ventana.winfo_width()
        alto_ventana = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
        ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) """

    """ ventana = tk.Tk()
    ventana.geometry("1300x800")
    ventana.title("MiKiosco")"""
    """ centrar_ventana(ventana) """
    ventana2 = tk.Toplevel()
    barraMenu = tk.Menu(ventana2)
    ventana2.config(menu=barraMenu)


    archivoMenu=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    archivoMenu.add_command(label="Nuevo archivo")
    archivoMenu.add_command(label="Nueva ventana2")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Salir", command=salir)

    menuArticulos=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Artículos", menu=menuArticulos)

    menuVentas = tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Ventas", menu=menuVentas)

    menuCompras = tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Compras", menu=menuCompras)

    menuProveedores = tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Proveedores", menu=menuProveedores)

    menuInformes = tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Informes", menu=menuInformes)

    menuCaja = tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Caja", menu=menuCaja)

    marco = tk.Frame(ventana2, bg="#D9D9D9")
    marco.grid(row=0, column=0,sticky='nsew', pady=10, padx=10)


    ventana2.grid_columnconfigure(0, weight=1)
    ventana2.grid_rowconfigure(0, weight=1)

    labelCodigo = tk.Label(marco, text="Código de barras:", font=("Arial", 11), bg="#D9D9D9")
    labelCodigo.grid(pady=(10,0), row=0, column=0, padx=(10,0))

    entryCodigo= tk.Entry(marco, font=("Arial", 11))
    entryCodigo.grid(pady=(10,0), row=0, column=1)

    labelCantidad = tk.Label(marco, text="Cantidad:", font=("Arial", 11), bg="#D9D9D9")
    labelCantidad.grid(pady=(10,0), row=0, column=2, padx=(10,0))

    entryCantidad= tk.Entry(marco, font=("Arial", 11))
    entryCantidad.grid(pady=(10,0), row=0, column=3)

    btnAgregar = tk.Button(marco, text="Agregar")
    btnAgregar.grid(pady=(10,0), row=0, column=4, padx=(20,0))
    
    ventana2.mainloop()

programaPrincipal()