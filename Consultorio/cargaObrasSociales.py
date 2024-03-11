from customtkinter import *
from CTkTable import CTkTable
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image
import json
from tkcalendar import DateEntry
from clases import *

arrayPlanes = []

def menuPrincipal(app, main_view):
    for widget in main_view.winfo_children():
        widget.destroy()


    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

    CTkLabel(master=title_frame, text="Obras Sociales", font=("Arial Black", 25), text_color="#10302E").pack(anchor="nw", side="left")
    
    search_container = CTkFrame(master=main_view, height=600, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(10, 0), padx=27)

    msj_container = CTkFrame(master=main_view, height=70, width=350, fg_color="transparent")
    msj_container.pack( pady=(30, 0), padx=27)

    msj_label = CTkLabel(master=msj_container,text="", font=("Arial", 15), text_color="#10302E")
    msj_label.pack(anchor="nw", padx=15, pady=10)

    CTkLabel(master=search_container, text="Obra Social", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=1, column=1, sticky="sw", padx=(43,0), pady=(10,0))
    entOS = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese Obra Social", border_color="#85E6C0", border_width=2)
    entOS.grid(row=2, column=1, sticky="sw", padx=(43,0), pady=(0,20))
       
    CTkLabel(master=search_container, text="Plan", text_color="black", font=("Arial Regular", 15, "bold")).grid(row=1, column=2, sticky="sw", padx=(43,0), pady=(10,0))
    entPlan = CTkEntry(master=search_container, width=250, placeholder_text="Ingrese plan", border_color="#85E6C0", border_width=2)
    entPlan.grid(row=2, column=2, sticky="sw", padx=(43,0), pady=(0,20))
    
    ############################################################## AGREGAR PLAN ########################################################

    def agregarPlan():
        nombrePlan = entPlan.get()
        arrayPlanes.append(nombrePlan)
        print(arrayPlanes)
        msj_container.configure(fg_color="#68FD7E")
        msj_label.configure(text="Plan agregado con éxito")
    
    CTkButton(master=search_container, text="Agregar",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", width=35, command=agregarPlan).grid(row=2, column=3, sticky="sw", padx=(10,0), pady=(0,20))

    ########################################################### REGISTRAR PACIENTE #####################################################
    
    def registrarPaciente():
        validaOS = False
        nombre = entOS.get()

        with open("data/ObrasSociales.json", "r", encoding="utf-8") as archivo:
            obrasSociales2 = json.load(archivo)
        for OS in obrasSociales2:
            if OS['nombreObraSocial'] == nombre:
                validaOS = True
        if nombre == "":
            validaOS = True

        if validaOS == False:
            with open("data/ObrasSociales.json", "r", encoding="utf-8") as archivo:
                obrasSociales = json.load(archivo)
            if obrasSociales == []:
                nuevo_id = 0
            else:
                ultimo_id = obrasSociales[-1]["idObraSocial"]
                nuevo_id = ultimo_id + 1

            nueva_instancia = ObraSocial(nuevo_id, nombre, arrayPlanes) 

            print(nueva_instancia)
            nuevo_objeto = {
            "idObraSocial": nueva_instancia.idObraSocial,
            "nombreObraSocial": nueva_instancia.nombreObraSocial,   
            "arrayPlanes": nueva_instancia.arrayPlanes
            }

            nuevo_objeto_json = json.dumps(nuevo_objeto)
            obrasSociales.append(json.loads(nuevo_objeto_json))
            with open("data/ObrasSociales.json", "w", encoding="utf-8") as archivo:
                json.dump(obrasSociales, archivo, indent=4, ensure_ascii=False)

            msj_container.configure(fg_color="#68FD7E")
            msj_label.configure(text="Obra Social cargada con éxito!")

        else:
            msj_container.configure(fg_color="#F85A5A")
            msj_label.configure(text="Obra Social inválida o repetida")

    CTkButton(master=title_frame, text="Registrar obra social",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A", command=registrarPaciente).pack(anchor="ne", side="right")

