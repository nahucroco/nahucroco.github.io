from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import json

class Turno:
    def __init__(self, idTurno, dia, horario, paciente, medico, obraSocial):
        self.idTurno = idTurno
        self.dia = dia
        self.horario = horario
        self.paciente = paciente
        self.medico = medico
        self.obraSocial = obraSocial


def seleccionar_boton(boton_seleccionado):
    for boton in botones:
        if boton is not boton_seleccionado:
            boton.configure(fg_color="transparent", text_color="#F9F9FA", hover_color="#55958D")
        else:
            boton.configure(fg_color="#F9F9FA", text_color="#6BAAA2", hover_color="#F9F9FA")

# Función para crear un nuevo botón

############################################################### DEFINE VENTANA ###########################################################
        
app = CTk()
app.geometry("856x645")
app.resizable(0,0)
set_appearance_mode("light")

############################################################## WIDGETS ###################################################################
        
########################################### BARRA LATERAL ####################################################

sidebar_frame = CTkFrame(master=app, fg_color="#6BAAA2",  width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

################################################ LOGO ########################################################

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(140, 140))
CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(0, 110), anchor="center")

 ############################################ BOTON TURNOS ####################################################

package_img_data = Image.open("package_icon.png")
package_img = CTkImage(dark_image=package_img_data, light_image=package_img_data)
btn_turnos = CTkButton(master=sidebar_frame, image=package_img, text="Turnos", fg_color="#fff", font=("Arial Bold", 14), text_color="#6BAAA2", hover_color="#eee", anchor="w", command=lambda: seleccionar_boton(btn_turnos)).pack(anchor="center", ipady=5, pady=(110, 0))
 
########################################### BOTON PACIENTES ##################################################

list_img_data = Image.open("list_icon.png")
list_img = CTkImage(dark_image=list_img_data, light_image=list_img_data)
btn_pacientes = CTkButton(master=sidebar_frame, image=list_img, text="Pacientes", fg_color="transparent", font=("Arial Bold", 14), hover_color="#55958D", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

############################################ BOTON MÉDICOS ###################################################

returns_img_data = Image.open("returns_icon.png")
returns_img = CTkImage(dark_image=returns_img_data, light_image=returns_img_data)
btn_medicos = CTkButton(master=sidebar_frame, image=returns_img, text="Médicos", fg_color="transparent", font=("Arial Bold", 14), hover_color="#55958D", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

######################################### BOTON OBRAS SOCIALES ###############################################

settings_img_data = Image.open("settings_icon.png")
settings_img = CTkImage(dark_image=settings_img_data, light_image=settings_img_data)
btn_obrasSociales = CTkButton(master=sidebar_frame, image=settings_img, text="Obras Sociales", fg_color="transparent", font=("Arial Bold", 14), hover_color="#55958D", anchor="w").pack(anchor="center", ipady=5, pady=(16, 0))

 


def crear_boton(data, texto):
    img = CTkImage(dark_image=data, light_image=data)
    boton = CTkButton(master=sidebar_frame, text=texto, text_color="#fff", image=img, fg_color="transparent", font=("Arial", 14, "bold"), hover_color="#55958D", anchor="w", command=lambda b=texto: seleccionar_boton(boton))
    boton.pack(anchor="center", ipady=5, pady=(16, 0))
    botones.append(boton)




botones = [] 

# Crear los cinco botones
package_img_data = Image.open("package_icon.png")
crear_boton(package_img_data, "Turnos")
list_img_data = Image.open("list_icon.png")
crear_boton(list_img_data, "Pacientes")
returns_img_data = Image.open("returns_icon.png")
crear_boton(returns_img_data, "Medicos")
settings_img_data = Image.open("settings_icon.png")
crear_boton(settings_img_data, "Obras Sociales")

############################################## BOTON SALIR ###################################################

person_img_data = Image.open("person_icon.png")
person_img = CTkImage(dark_image=person_img_data, light_image=person_img_data)
CTkButton(master=sidebar_frame, image=person_img, text="Salir", fg_color="transparent", font=("Arial Bold", 14), hover_color="#55958D", anchor="w").pack(anchor="center", ipady=5, pady=(130, 0))

##################################### FRAME TITULO Y AGREGAR #################################################

main_view = CTkFrame(master=app, fg_color="#fff",  width=680, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="left")

title_frame = CTkFrame(master=main_view, fg_color="transparent")
title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))

CTkLabel(master=title_frame, text="Turnos", font=("Arial Black", 25), text_color="#10302E").pack(anchor="nw", side="left")

CTkButton(master=title_frame, text="Reservar turno",  font=("Arial Regular", 15), text_color="#1E1E1E", fg_color="#85E6C0", hover_color="#25B47A").pack(anchor="ne", side="right")

metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(10, 0))

shipped_metric = CTkFrame(master=metrics_frame, fg_color="#85E6C0", width=630, height=160)
shipped_metric.grid_propagate(0)
shipped_metric.pack(side="left",expand=True, anchor="center")

####################################### FRAME BUSQEDA Y FILTROS #############################################

search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
search_container.pack(fill="x", pady=(10, 0), padx=27)

CTkEntry(master=search_container, width=305, placeholder_text="Buscar paciente", border_color="#85E6C0", border_width=2).pack(side="left", padx=(13, 0), pady=15)

CTkComboBox(master=search_container, width=125, values=["Fecha", "Most Recent Order", "Least Recent Order"], button_color="#85E6C0", border_color="#85E6C0", border_width=2, button_hover_color="#85E6C0",dropdown_hover_color="#85E6C0" , dropdown_fg_color="#25B47A", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)
CTkComboBox(master=search_container, width=125, values=["Médico", "Processing", "Confirmed", "Packing", "Shipping", "Delivered", "Cancelled"], button_color="#85E6C0", border_color="#85E6C0", border_width=2, button_hover_color="#85E6C0",dropdown_hover_color="#85E6C0" , dropdown_fg_color="#25B47A", dropdown_text_color="#fff").pack(side="left", padx=(13, 0), pady=15)

""" 
orders_metric = CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
orders_metric.grid_propagate(0)
orders_metric.pack(side="left")  """

 
""" 

CTkLabel(master=orders_metric, text="Orders", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=orders_metric, text="123", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10)) 

 """


analytics_img_data = Image.open("analytics_icon.png")
analytics_img = CTkImage(dark_image=analytics_img_data, light_image=analytics_img_data)


CTkLabel(master=shipped_metric, text="Shipping", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=shipped_metric, text="91", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))

delivered_metric = CTkFrame(master=metrics_frame, fg_color="#2A8C55", width=200, height=60)
delivered_metric.grid_propagate(0)
delivered_metric.pack(side="right",) 


CTkLabel(master=delivered_metric, text="Delivered", text_color="#fff", font=("Arial Black", 15)).grid(row=0, column=1, sticky="sw")
CTkLabel(master=delivered_metric, text="23", text_color="#fff",font=("Arial Black", 15), justify="left").grid(row=1, column=1, sticky="nw", pady=(0,10))


############################################################### BUSQUEDA ###########################################################

def buscar_turnos_por_medico(nombre_medico, archivo_json, fecha):
    with open(archivo_json) as file:
        turnos = json.load(file)
    
    turnos_del_medico = [turno for turno in turnos if turno['medico']['nombreMedico'] == nombre_medico and turno['dia'] == fecha]
    
    return turnos_del_medico

# Ejemplo de uso:
nombre_medico = "Claudia"
archivo_json = "Turnos.json"
fecha = "2024, 2, 24"

turnos_encontrados = buscar_turnos_por_medico(nombre_medico, archivo_json, fecha)
for turno in turnos_encontrados:
    print(turno) 



table_data = [
            ["08:00", "15:30"],
            ["08:20", "15:50"],
            ["08:40", "16:10"],
            ["09:00", "16:30"],
            ["09:20", "16:50"],
            ["09:40", "17:10"],
            ["10:00", "17:30"],
            ["10:20", "17:50"],
            ["10:40", "18:10"],
            ["11:00", "18:30"],
            ["11:20", "18:50"],
            ["11:40", "19:10"]
]




for fila_index, fila in enumerate(table_data):
    for columna_index, elemento in enumerate(fila):
        for turno in turnos_encontrados:
            if elemento == turno['horario']:
                print(fila_index, columna_index)
                elemento = table_data[fila_index][columna_index]
                string = elemento + '                          ' + turno['paciente']['nombrePaciente'] + ' ' +turno['paciente']['apellidoPaciente']
                table_data[fila_index][columna_index] = string
            else:
                string = elemento + '                                                Libre       '
                table_data[fila_index][columna_index] = string

table_frame = CTkFrame(master=main_view, fg_color="transparent")
table_frame.pack(expand=True, fill="both", padx=27, pady=10)
table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"],  hover_color="#B4B4B4", width=600)
table.pack(expand=True)

app.mainloop()