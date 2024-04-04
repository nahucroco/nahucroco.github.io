import tkinter as tk
from tkinter import messagebox
from manage_db import *
from tkinter import ttk

def centrarVentana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto_ventana // 2)
    ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))

ventana = tk.Tk()
ventana.geometry("1300x800")
ventana.title("MiKiosco")
centrarVentana(ventana)
contador_filas = 0

def main():
    global tabla
    ventana.destroy()

    global ventanaMain
    ventanaMain = tk.Tk()
    ventanaMain.geometry("1300x800")
    ventanaMain.title("MiKiosco")

    barraMenu = tk.Menu(ventanaMain)
    ventanaMain.config(menu=barraMenu)
    centrarVentana(ventanaMain)

    archivoMenu=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
    archivoMenu.add_command(label="Nuevo archivo")
    archivoMenu.add_command(label="Nueva ventana")
    archivoMenu.add_separator()
    archivoMenu.add_command(label="Salir")

    menuArticulos=tk.Menu(barraMenu,tearoff=0)
    barraMenu.add_cascade(label="Artículos", menu=menuArticulos)
    menuArticulos.add_command(label="Cargar artículo", command=lambda: ingresoDatos(None))
    menuArticulos.add_command(label="Modificar artículo", command=ingresoCodigo)

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

    marco = tk.Frame(ventanaMain, bg="#D9D9D9")
    marco.grid(row=0, column=0,sticky='nsew', pady=10, padx=10)

    ventanaMain.grid_columnconfigure(0, weight=1)
    ventanaMain.grid_rowconfigure(0, weight=1)

    ############################################### BUSCAR ARTICULO #######################################################

    labelCodigo = tk.Label(marco, text="Código de barras:", font=("Arial", 11), bg="#D9D9D9")
    labelCodigo.grid(pady=(10,0), row=0, column=0, padx=(10,0))

    entryCodigo= tk.Entry(marco, font=("Arial", 11))
    entryCodigo.grid(pady=(5,0), row=0, column=1)

    labelCantidad = tk.Label(marco, text="Cantidad:", font=("Arial", 11), bg="#D9D9D9")
    labelCantidad.grid(pady=(10,0), row=0, column=2, padx=(10,0))

    spinCantidad = tk.Spinbox(marco, from_=0, to=100, increment=1, width=10, font=("Arial", 11))
    spinCantidad.grid(pady=(5,0), row=0, column=3)

    btnAgregar = tk.Button(marco, text="Agregar", command=lambda: agregarArticuloTabla(entryCodigo.get(), int(spinCantidad.get())))
    btnAgregar.grid(pady=(10,0), row=0, column=4, padx=(20,0))

    #################################################### LISTA ############################################################

    # Crear un Treeview (tabla)
    tabla = ttk.Treeview(marco)

    # Configurar las columnas de la tabla
    tabla['columns'] = ('Cantidad', 'Nombre', 'Categoría', 'Peso', 'Marca', 'Precio', 'Código')

    # Encabezados de las columnas
    tabla.heading('#0', text='ID')  # Columna oculta para el ID
    tabla.heading('Cantidad', text='Cantidad')
    tabla.heading('Nombre', text='Nombre')
    tabla.heading('Categoría', text='Categoría')
    tabla.heading('Peso', text='Peso (g - L)')
    tabla.heading('Marca', text='Marca')
    tabla.heading('Precio', text='Precio')
    tabla.heading('Código', text='Código')

    # Insertar datos en la tabla
    datos = [
    ]


    # Ajustar el tamaño de las columnas
    for columna in tabla['columns']:
        tabla.column(columna, stretch=False, width=130)
    
    tabla.column('#0', stretch=False, width=50) 

    tabla.grid(pady=(10,0), row=2, column=0, padx=(20,0), columnspan=4)

    for dato in datos:
        tabla.insert('', tk.END, text=dato[0], values=dato[1:]) 

    ventanaMain.mainloop()

def agregarArticuloTabla(codigo, cantidad):
    global contador_filas
    if cantidad == 0:
        messagebox.showerror('Error', "Ingresar una cantidad válida")
    else:       
        articulo = buscarArticuloDB(codigo)
        print(articulo)
        if articulo == None:
            messagebox.showerror('Error', "Ingresar un código válido")
        else:
            if cantidad != None:
                tabla.insert('', 'end', text=str(contador_filas), values=(cantidad,) + articulo)
                contador_filas += 1
            else:
                ingresoDatos(articulo)

def ingresoDatos(articulo):
    ventanaCarga = tk.Toplevel(ventanaMain)
    ventanaCarga.title("Agregar artículo")
    ventanaCarga.geometry("690x120")
    centrarVentana(ventanaCarga)

    if articulo == None:
        var = "agregar"
        nombre = ""
        categoria = ""
        peso = ""
        marca = ""
        precio = ""
        codigo = ""
    else: 
        var = "editar"
        nombre = tk.StringVar()
        nombre.set(articulo[0])
        categoria = tk.StringVar()
        categoria.set(articulo[1])
        peso = tk.StringVar()
        peso.set(articulo[2])
        marca = tk.StringVar()
        marca.set(articulo[3])
        precio = tk.StringVar()
        precio.set(articulo[4])
        codigo = tk.StringVar()
        codigo.set(articulo[5])

    labelNom = tk.Label(ventanaCarga,text="Nombre",font=("Arial", 11))
    labelNom.grid(padx=(20,0), pady=(10,0),row=0,column=0)
    entryNom = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=nombre)
    entryNom.grid(padx=(20,0), pady=(10,0),row=0,column=1)

    labelCat = tk.Label(ventanaCarga,text="Categoría",font=("Arial", 11))
    labelCat.grid(padx=(20,0), pady=(10,0),row=0,column=2)
    entryCat = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=categoria)
    entryCat.grid(padx=(20,0), pady=(10,0),row=0,column=3)

    labelPeso = tk.Label(ventanaCarga,text="Peso (g - L)",font=("Arial", 11))
    labelPeso.grid(padx=(20,0), pady=(10,0),row=1,column=0)
    entryPeso = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=peso)
    entryPeso.grid(padx=(20,0), pady=(10,0),row=1,column=1)

    labelMar = tk.Label(ventanaCarga,text="Marca",font=("Arial", 11))
    labelMar.grid(padx=(20,0), pady=(10,0),row=1,column=2)
    entryMar = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=marca)
    entryMar.grid(padx=(20,0), pady=(10,0),row=1,column=3)

    labelPre = tk.Label(ventanaCarga,text="Precio",font=("Arial", 11))
    labelPre.grid(padx=(20,0), pady=(10,0),row=2,column=0)
    entryPre = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=precio)
    entryPre.grid(padx=(20,0), pady=(10,0),row=2,column=1)

    labelCod = tk.Label(ventanaCarga,text="Código",font=("Arial", 11))
    labelCod.grid(padx=(20,0), pady=(10,0),row=2,column=2)
    entryCod = tk.Entry(ventanaCarga, font=("Arial", 11), textvariable=codigo)
    entryCod.grid(padx=(20,0), pady=(10,0),row=2,column=3)

    btnAgregar = tk.Button(ventanaCarga, text="Agregar", width=12, command=lambda: editarArticuloDB(str(entryNom.get()), entryCat.get(), int(entryCod.get()), entryMar.get(), entryPeso.get(), float(entryPre.get()), ventanaCarga, var))
    btnAgregar.grid(padx=(30,0), pady=(10,0),row=1,column=4)

def ingresoCodigo():
    ventanaBuscar = tk.Toplevel(ventanaMain)
    ventanaBuscar.title("Buscar artículo")
    ventanaBuscar.geometry("400x50")
    centrarVentana(ventanaBuscar)

    labelCod = tk.Label(ventanaBuscar,text="Código:",font=("Arial", 11))
    labelCod.grid(padx=(20,0), pady=(10,0),row=0,column=0)
    entryCod = tk.Entry(ventanaBuscar, font=("Arial", 11))
    entryCod.grid(padx=(20,0), pady=(10,0),row=0,column=1)

    btnBuscar = tk.Button(ventanaBuscar, text="Buscar", width=12, command=lambda: agregarArticuloTabla(entryCod.get(), None))
    btnBuscar.grid(padx=(30,0), pady=(10,0),row=0,column=2)

def validarContrasena(usuario, pass1, pass2):
    if pass1 == pass2:
        if registrarUsuario(usuario, pass1) == 'error1':
            messagebox.showerror("Error", 'El usuario ya existe en la base de datos.')
        elif registrarUsuario(usuario, pass1) == 'error2':
            messagebox.showerror("Error", 'Error al insertar usuario')
        else:
            messagebox.showinfo("Completado", 'Usuario insertado correctamente.')
    else:
        messagebox.showerror("Error", "Las contraseñas no coinciden")

def validarUsuario(usuario, contrasena):
    if usuario_existe(usuario, contrasena):
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        main()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def limpiarVentana():
    # Eliminar todos los widgets de la ventana
    for widget in ventana.winfo_children():
        widget.destroy()

def registro():
    limpiarVentana()
    marco = tk.Frame(ventana, bg="#D9D9D9", width=500, height=500)
    marco.pack(pady=90)
    marco.pack_propagate(False)
    # Etiqueta y entrada para el usuario
    tk.Label(marco, text="Usuario:", font=("Arial", 16), bg="#D9D9D9").pack(pady=(80,0))
    entry_usuario = tk.Entry(marco, font=("Arial", 14))
    entry_usuario.pack()

    # Etiqueta y entrada para la contraseña
    tk.Label(marco, text="Contraseña:", font=("Arial", 16), bg="#D9D9D9").pack(pady=(20,0))
    entry_contrasena1 = tk.Entry(marco, show="*", font=("Arial", 14))
    entry_contrasena1.pack()

    # Etiqueta y entrada para la contraseña
    tk.Label(marco, text="Repetir contraseña:", font=("Arial", 16), bg="#D9D9D9").pack(pady=(20,0))
    entry_contrasena2 = tk.Entry(marco, show="*", font=("Arial", 14))
    entry_contrasena2.pack()

    # Botón para registrarse
    btn_registro = tk.Button(marco, text="Registrarse", command=lambda: validarContrasena(entry_usuario.get(), entry_contrasena1.get(), entry_contrasena2.get()))
    btn_registro.pack(pady=(40,0))

    # Botón para login
    btn_iniciar_sesion = tk.Button(marco, text="Iniciar sesión", command=iniciarSesion)
    btn_iniciar_sesion.pack(pady=(10,0))

def iniciarSesion():
    limpiarVentana()
    marco = tk.Frame(ventana, bg="#D9D9D9", width=500, height=500)
    marco.pack(pady=90)
    marco.pack_propagate(False)
    # Etiqueta y entrada para el usuario
    tk.Label(marco, text="Usuario:", font=("Arial", 16), bg="#D9D9D9").pack(pady=(110,0))
    entry_usuario = tk.Entry(marco, font=("Arial", 14))
    entry_usuario.pack()

    # Etiqueta y entrada para la contraseña
    tk.Label(marco, text="Contraseña:", font=("Arial", 16), bg="#D9D9D9").pack(pady=(20,0))
    entry_contrasena = tk.Entry(marco, show="*", font=("Arial", 14))
    entry_contrasena.pack()

    # Botón para iniciar sesión
    btn_iniciar_sesion = tk.Button(marco, text="Iniciar sesión", command=lambda: validarUsuario(entry_usuario.get(), entry_contrasena.get()))
    btn_iniciar_sesion.pack(pady=(40,0))

    # Botón para registrarse
    btn_registro = tk.Button(marco, text="Crear nuevo usuario", command=registro)
    btn_registro.pack(pady=(10,0))

iniciarSesion()

ventana.mainloop()

