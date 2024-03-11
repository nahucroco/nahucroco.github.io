from customtkinter import *
from CTkTable import CTkTable
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image
import json
from tkcalendar import DateEntry
import cargaTurnos
import cargaMedicos
import cargaPacientes
import cargaObrasSociales

app = CTk()
app.geometry("1156x645")
app.resizable(0,0)
app.title("App Consultorio")
app.iconbitmap('media/cruzar.ico')
set_appearance_mode("light")

################################################ BARRA LATERAL Y VISTA PRINCIPAL ########################################################

def lateralYMain():
    global main_view
    sidebar_frame = CTkFrame(master=app, fg_color="#6BAAA2",  width=176, height=650, corner_radius=0)
    sidebar_frame.pack_propagate(0)
    sidebar_frame.pack(fill="y", anchor="w", side="left")

    logo_img_data = Image.open("media/logo.png")
    logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(140, 140))
    CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(0, 110), anchor="center")

    main_view = CTkFrame(master=app, fg_color="#fff",  width=980, height=650, corner_radius=0)
    main_view.pack_propagate(0)
    main_view.pack(side="left")

    def salir():
        app.destroy()

    def seleccionar_boton(boton_seleccionado, funcion):
        for boton in botones:
            if boton is not boton_seleccionado:
                package_img_data = Image.open(iconosBlancos[botones.index(boton)])
                img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
                boton.configure(fg_color="transparent", text_color="#F9F9FA", hover_color="#55958D", image=img)
            else:
                package_img_data = Image.open(iconosVerdes[botones.index(boton)])
                img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
                boton.configure(fg_color="#F9F9FA", text_color="#6BAAA2", hover_color="#F9F9FA", image=img)
                funcion(app, main_view)

    def crear_boton(data, texto, funcion):
        if texto == "Turnos":
            img = CTkImage(dark_image=data, light_image=data)
            boton = CTkButton(master=sidebar_frame, text=texto, text_color="#6BAAA2", image=img, fg_color="#F9F9FA",font=("Arial", 14, "bold"), hover_color="#F9F9FA", anchor="w", command=lambda b=texto: seleccionar_boton(boton, funcion), width=150)
            boton.pack(anchor="w", ipady=5, pady=(16, 0), padx=(13,0))
            botones.append(boton)
        else:
            img = CTkImage(dark_image=data, light_image=data)
            boton = CTkButton(master=sidebar_frame, text=texto, text_color="#fff", image=img, fg_color="transparent",font=("Arial", 14, "bold"), hover_color="#55958D", anchor="w", command=lambda b=texto: seleccionar_boton(boton, funcion), width=150)
            boton.pack(anchor="w", ipady=5, pady=(16, 0), padx=(13,0))
            botones.append(boton)

    botones = [] 
    iconosVerdes = ["media/turnos_verde.png","media/pacientes_verde.png","media/medicos_verde.png","media/obrasSociales_verde.png"]
    iconosBlancos = ["media/turnos_blanco.png","media/pacientes_blanco.png","media/medicos_blanco.png","media/obrasSociales_blanco.png"]

    package_img_data = Image.open("media/turnos_verde.png")
    crear_boton(package_img_data, "Turnos", cargaTurnos.menuPrincipal)
    list_img_data = Image.open("media/pacientes_blanco.png")
    crear_boton(list_img_data, "Pacientes", cargaPacientes.menuPrincipal)
    returns_img_data = Image.open("media/medicos_blanco.png")
    crear_boton(returns_img_data, "Medicos", cargaMedicos.menuPrincipal)
    settings_img_data = Image.open("media/obrasSociales_blanco.png")
    crear_boton(settings_img_data, "Obras Sociales", cargaObrasSociales.menuPrincipal)
    person_img_data = Image.open("media/cerrar.png")
    person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
    CTkButton(master=sidebar_frame, image=person_img, text="Salir", fg_color="transparent", text_color= "#F9F9FA", font=("Arial", 14, "bold"), hover_color="#55958D", anchor="w", command=salir).pack(anchor="center", ipady=5, pady=(130, 0))

################################### PROGRAMA PRINCIPAL ###########################################

lateralYMain()
cargaTurnos.menuPrincipal(app, main_view)

app.mainloop()