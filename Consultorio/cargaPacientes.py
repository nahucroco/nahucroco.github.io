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

    CTkLabel(master=title_frame, text="Pacientes", font=("Arial Black", 25), text_color="#10302E").pack(anchor="nw", side="left")
    
    search_container = CTkFrame(master=main_view, height=600, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(10, 0), padx=27)

    msj_container = CTkFrame(master=main_view, height=70, width=350, fg_color="transparent")
    msj_container.pack( pady=(30, 0), padx=27)

    msj_label = CTkLabel(master=msj_container,text="", font=("Arial", 15), text_color="#10302E")
    msj_label.pack(anchor="nw", padx=15, pady=10)

    CTkLabel(master=search_container, text="Nombre", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entNom = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese nombre", border_color="#85E6C0", border_width=2)
    entNom.grid(row=1, column=1, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="Apellido", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=2, sticky="sw", padx=(43,0), pady=(10,0))
    entApe = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese apellido", border_color="#85E6C0", border_width=2)
    entApe.grid(row=1, column=2, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="DNI", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=0, column=3, sticky="sw", padx=(43,0), pady=(10,0))
    entDNI = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese DNI", border_color="#85E6C0", border_width=2)
    entDNI.grid(row=1, column=3, sticky="sw", padx=(43,0), pady=(0,10))
    

    CTkLabel(master=search_container, text="Teléfono", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=2, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entTel = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese teléfono", border_color="#85E6C0", border_width=2)
    entTel.grid(row=3, column=1, sticky="sw", padx=(43,0), pady=(0,20))
    

    CTkLabel(master=search_container, text="Número de afiliado", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=2, column=2, sticky="sw", padx=(43,0), pady=(10,0))
    entNum = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese número de afiliado", border_color="#85E6C0", border_width=2)
    entNum.grid(row=3, column=2, sticky="sw", padx=(43,0), pady=(0,20))
    

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
    
    CTkButton(master=search_container, text="Agregar",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", width=35, command=agregarOS).grid(row=5, column=2, sticky="sw", padx=(10,0), pady=(0,15))

    ####################################################### ELECCION PLAN ##################################################
    
    planes = []
    with open('data/ObrasSociales.json', 'r') as file:
        arreglo_OS = json.load(file)   
    for obraSocial in arreglo_OS:
        if obraSocial['nombreObraSocial'] == obraSocial_seleccionada_1:
            planes.append(obraSocial['arrayPlanes'])
            print(planes)

    def actualizar_opciones_Planes(event):
        texto_ingresado = campo_entrada_Planes_1.get()
        opciones_filtradas = [plan for plan in planes if texto_ingresado.lower() in plan.lower()]
        comboPlanes1["values"] = opciones_filtradas


    def seleccionar_opcion_Planes(event):
        global plan_seleccionado
        plan_seleccionado = campo_entrada_Planes_1.get()
        print("Plan:", plan_seleccionado)
    
    opcion_seleccionada_Planes = tk.StringVar()

    
    label1 = CTkLabel(master=search_container, text='Obras Sociales', fg_color="transparent",font=("Arial", 14, "bold"))
    label1.grid(row=4, column=1,sticky="sw", padx=(43,0), pady=(10,0))

    comboPlanes1 = ttk.Combobox(master=search_container, textvariable=opcion_seleccionada_Planes, width=35)
    comboPlanes1.grid(row=5, column=1, sticky="sw", padx=(43,0), pady=(0,20))
    comboPlanes1.bind("<<ComboboxSelected>>", seleccionar_opcion_Planes)
    campo_entrada_Planes_1 = comboPlanes1
    campo_entrada_Planes_1.bind("<KeyRelease>", actualizar_opciones_Planes)
    comboPlanes1["values"] = planes
    
    """ def agregarPlanes():
        arregloPlanes.append(obraSocial_seleccionada_1) """
    
    CTkButton(master=search_container, text="Agregar",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", width=35, command=agregarOS).grid(row=5, column=2, sticky="sw", padx=(10,0), pady=(0,15))

    ########################################################### REGISTRAR PACIENTE #####################################################
    def registrarPaciente():
        validaDNI = False
        arregloOS.append(obraSocial_seleccionada_1)
        arregloOS.append(obraSocial_seleccionada_2)
        arregloOS.append(obraSocial_seleccionada_3)
        nombre = entNom.get()
        apellido = entApe.get()
        dni = entDNI.get()
        telefono = entTel.get()
        numAfiliado = entNum.get()
        arrayOS = []

        with open("data/ObrasSociales.json", "r", encoding="utf-8") as archivo:
            obrasSociales = json.load(archivo)
        for os in arregloOS:
            for obraSocial in obrasSociales:
                if obraSocial['nombreObraSocial'] == os:
                    arrayOS.append(obraSocial)

        with open("data/Pacientes.json", "r", encoding="utf-8") as archivo:
            pacientes2 = json.load(archivo)
        for paciente in pacientes2:
            if paciente['dni'] == dni:
                validaDNI = True
        if dni == "":
            validaDNI = True

        if nombre != "": 
            if apellido != "": 
                if arrayOS != []:
                    if validaDNI == False:
                        with open("data/Pacientes.json", "r", encoding="utf-8") as archivo:
                            pacientes = json.load(archivo)
                        if pacientes == []:
                            nuevo_id = 0
                        else:
                            ultimo_id = pacientes[-1]["idPaciente"]
                            nuevo_id = ultimo_id + 1



                        nueva_instancia = Paciente(nuevo_id, dni, telefono, apellido, nombre, numAfiliado, arrayOS) 

                        print(nueva_instancia)
                        nuevo_objeto = {
                        "idPaciente": nueva_instancia.idPaciente,
                        "dni": nueva_instancia.dni,    
                        "telefono": nueva_instancia.telefono,
                        "apellidoPaciente": nueva_instancia.apellidoPaciente,
                        "nombrePaciente": nueva_instancia.nombrePaciente,   
                        "nroAfiliado": nueva_instancia.nroAfiliado,
                        "arrayOS": nueva_instancia.arrayOS
                        }

                        nuevo_objeto_json = json.dumps(nuevo_objeto)
                        pacientes.append(json.loads(nuevo_objeto_json))
                        with open("data/Pacientes.json", "w", encoding="utf-8") as archivo:
                            json.dump(pacientes, archivo, indent=4, ensure_ascii=False)

                        msj_container.configure(fg_color="#85E6C0")
                        msj_label.configure(text="Paciente cargado con éxito!")
                    else:
                        msj_container.configure(fg_color="#F85A5A")
                        msj_label.configure(text="Numero de DNI inválido o repetido")
                else: 
                    msj_container.configure(fg_color="#F85A5A")
                    msj_label.configure(text="Ingresar al menos una obra social")
            else:
                msj_container.configure(fg_color="#F85A5A")
                msj_label.configure(text="Apellido inválido")
        else:
            msj_container.configure(fg_color="#F85A5A")
            msj_label.configure(text="Nombre inválido")
    CTkButton(master=title_frame, text="Registrar paciente",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", command=registrarPaciente).pack(anchor="ne", side="right")