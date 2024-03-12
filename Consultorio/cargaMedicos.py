from customtkinter import *
from CTkTable import CTkTable
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image
import json
from tkcalendar import DateEntry
from clases import *

obraSocial_seleccionada_1 = None
obraSocial_seleccionada_2 = None
obraSocial_seleccionada_3 = None
arregloOS = []


def menuPrincipal(app, main_view):
    for widget in main_view.winfo_children():
        widget.destroy()


    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Médicos", font=("Arial Black", 25), text_color="#10302E").pack(anchor="nw", side="left")
    
    search_container = CTkFrame(master=main_view, height=600, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(10, 0), padx=27)

    CTkLabel(master=search_container, text="Nombre", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entNom = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese nombre", border_color="#85E6C0", border_width=2)
    entNom.grid(row=1, column=1, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="Apellido", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=2, sticky="sw", padx=(43,0), pady=(10,0))
    entApe = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese apellido", border_color="#85E6C0", border_width=2)
    entApe.grid(row=1, column=2, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="Mail", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=3, sticky="sw", padx=(43,0), pady=(10,0))
    entMail = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese mail", border_color="#85E6C0", border_width=2)
    entMail.grid(row=1, column=3, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="Teléfono", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=2, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entTel = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese teléfono", border_color="#85E6C0", border_width=2)
    entTel.grid(row=3, column=1, sticky="sw", padx=(43,0), pady=(0,20))
    

    CTkLabel(master=search_container, text="Usuario de AMR", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=2, column=2, sticky="sw", padx=(43,0), pady=(10,0))
    entUser = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese usuario", border_color="#85E6C0", border_width=2)
    entUser.grid(row=3, column=2, sticky="sw", padx=(43,0), pady=(0,20))
    

    CTkLabel(master=search_container, text="Contraseña de AMR", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=2, column=3, sticky="sw", padx=(43,0), pady=(10,0))
    entPass = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese contraseña", border_color="#85E6C0", border_width=2)
    entPass.grid(row=3, column=3, sticky="sw", padx=(43,0), pady=(0,20))
    
    ############################################## ELIMINAR MEDICO #############################################################
    
    def eliminarMedico(usuarioAMR):
        encontrado = False
        with open('data/Medicos.json', 'r') as archivo:
            medicos = json.load(archivo)
        for medico in medicos:
            if medico["usuarioAMR"] == usuarioAMR:
                encontrado = True
                medicos.remove(medico)
                mensajeError("Medico eliminado")
                break
        if encontrado == False: 
            mensajeError("Médico no encontrado")
        with open('data/Medicos.json', 'w') as archivo:
            json.dump(medicos, archivo, indent=4)

    delete_container = CTkFrame(master=main_view, height=260, fg_color="#F0F0F0")
    delete_container.pack(fill="x", padx=27, pady=(70))

    CTkLabel(master=delete_container, text="Usuario de AMR", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entUser2 = CTkEntry(master=delete_container, width=250, placeholder_text="Ingrese usuario", border_color="#85E6C0", border_width=2)
    entUser2.grid(row=1, column=1, sticky="sw", padx=(43,0), pady=(0,20))
    
    CTkButton(master=delete_container, text="Eliminar medico",  font=("Arial", 15, "bold"), text_color="#6BAAA2", fg_color="transparent", border_color="#6BAAA2", border_width=2, hover_color="#E6E6E6", command=lambda: eliminarMedico(entUser2.get())).grid(row=1, column=3, sticky="sw", padx=(480,0), pady=(0,15))

    ####################################################### ELECCION OBRA SOCIAL ##################################################
    
    with open('data/ObrasSociales.json', 'r') as file:
        arreglo_OS = json.load(file)   
    arreglo_nombres_OS = []
    for obraSocial in arreglo_OS:
        arreglo_nombres_OS.append(obraSocial['nombreObraSocial'])

    def actualizar_opciones_OS(event):
        texto_ingresado = campo_entrada_OS_1.get()
        opciones_filtradas = [nombre for nombre in arreglo_nombres_OS if texto_ingresado.lower() in nombre.lower()]
        comboOS1["values"] = opciones_filtradas


    def seleccionar_opcion_OS(event):
        global obraSocial_seleccionada_1
        obraSocial_seleccionada_1 = campo_entrada_OS_1.get()
        print("Obra Social 1:", obraSocial_seleccionada_1)
    
    opcion_seleccionada_OS = tk.StringVar()

    
    label1 = CTkLabel(master=search_container, text='Obras Sociales', fg_color="transparent",font=("Arial", 14, "bold"))
    label1.grid(row=4, column=1,sticky="sw", padx=(43,0), pady=(10,0))

    comboOS1 = ttk.Combobox(master=search_container, textvariable=opcion_seleccionada_OS, width=35)
    comboOS1.grid(row=5, column=1, sticky="sw", padx=(43,0), pady=(0,20))
    comboOS1.bind("<<ComboboxSelected>>", seleccionar_opcion_OS)
    campo_entrada_OS_1 = comboOS1
    campo_entrada_OS_1.bind("<KeyRelease>", actualizar_opciones_OS)
    comboOS1["values"] = arreglo_nombres_OS
    
    def agregarOS():
        arregloOS.append(obraSocial_seleccionada_1)
    
    CTkButton(master=search_container, text="+",  font=("Arial", 15, "bold"), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", width=35, command=agregarOS).grid(row=5, column=2, sticky="sw", padx=(0), pady=(0,15))

    ########################################################### REGISTRAR MEDICO #####################################################
    
    def registrarMedico():
        global arregloOS
        nombre = entNom.get()
        apellido = entApe.get()
        mail = entMail.get()
        telefono = entTel.get()
        usuario = entUser.get()
        contrasena = entPass.get()
        arrayOS = []
        with open("data/ObrasSociales.json", "r", encoding="utf-8") as archivo:
            obrasSociales = json.load(archivo)
        for os in arregloOS:
            for obraSocial in obrasSociales:
                if obraSocial['nombreObraSocial'] == os:
                    arrayOS.append(obraSocial)
        if nombre != "": 
            if apellido != "": 
                if arrayOS != []:
                    with open("data/Medicos.json", "r", encoding="utf-8") as archivo:
                        medicos = json.load(archivo)
                    if medicos == []:
                        nuevo_id = 0
                    else:
                        ultimo_id = medicos[-1]["idMedico"]
                        nuevo_id = ultimo_id + 1

                    nueva_instancia = Medico(nuevo_id, usuario, contrasena, apellido, nombre, telefono, mail, arrayOS) 

                    print(nueva_instancia)
                    nuevo_objeto = {
                    "idMedico": nueva_instancia.idMedico,
                    "usuarioAMR": nueva_instancia.usuarioAMR,    
                    "contrasenaAMR": nueva_instancia.contrasenaAMR,
                    "apellidoMedico": nueva_instancia.apellidoMedico,
                    "nombreMedico": nueva_instancia.nombreMedico,   
                    "telefono": nueva_instancia.telefono,
                    "mail": nueva_instancia.mail,
                    "arrayOS": nueva_instancia.arrayOS
                    }

                    nuevo_objeto_json = json.dumps(nuevo_objeto)
                    medicos.append(json.loads(nuevo_objeto_json))
                    with open("data/Medicos.json", "w", encoding="utf-8") as archivo:
                        json.dump(medicos, archivo, indent=4, ensure_ascii=False)
                    mensajeError("Médico cargado con éxito!")
                    arregloOS = []
                else: 
                    mensajeError("Ingresar al menos una obra social")
            else:
                mensajeError("Apellido inválido")
        else:
            mensajeError("Nombre inválido")

    CTkButton(master=search_container, text="Registrar médico",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", command=registrarMedico).grid(row=5, column=3, sticky="sw", padx=(185,0), pady=(0,20))

    ########################################################### MENSAJES DE ERROR #####################################################

    def mensajeError(error):
        notificacion = CTkToplevel(app)
        notificacion.title("Mensaje")
        notificacion.geometry("300x100")
        x = app.winfo_x()
        y = app.winfo_y()
        width = app.winfo_width()
        height = app.winfo_height()
    
        # Calcular la posición centrada para la ventana emergente
        x_pos = x + (width - notificacion.winfo_reqwidth()) // 2
        y_pos = y + (height - notificacion.winfo_reqheight()) // 2
    
        # Establecer la posición de la ventana emergente
        notificacion.geometry("+{}+{}".format(x_pos, y_pos))
        mensaje = CTkLabel(notificacion, text=error)
        mensaje.pack(pady=10)
        boton_cerrar = CTkButton(notificacion, text="Cerrar", command=notificacion.destroy, fg_color="#6BAAA2", font=("Arial", 13, "bold"))
        boton_cerrar.pack()
        notificacion.attributes('-topmost', True)
