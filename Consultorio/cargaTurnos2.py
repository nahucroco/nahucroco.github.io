from customtkinter import *
from CTkTable import CTkTable
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image
import json
from tkcalendar import DateEntry
from clases import *



medico_seleccionado = None
paciente_seleccionado = None
fecha_formateada = None
horario_seleccionado = None
var_paciente = None
arreglo_OS_paciente = []
arreglo_horarios = [            
            "08:00",
            "08:20",
            "08:40",
            "09:00",
            "09:20",
            "09:40",
            "10:00",
            "10:20",
            "10:40",
            "11:00",
            "11:20",
            "11:40",
            "15:30",
            "15:50",
            "16:10",
            "16:30",
            "16:50",
            "17:10",
            "17:30",
            "17:50",
            "18:10",
            "18:30",
            "18:50",
            "19:10",
            
    ]
table_data = [
            ["08:00", "Libre", "15:30", "Libre"],
            ["08:20", "Libre", "15:50", "Libre"],
            ["08:40", "Libre", "16:10", "Libre"],
            ["09:00", "Libre", "16:30", "Libre"],
            ["09:20", "Libre", "16:50", "Libre"],
            ["09:40", "Libre", "17:10", "Libre"],
            ["10:00", "Libre", "17:30", "Libre"],
            ["10:20", "Libre", "17:50", "Libre"],
            ["10:40", "Libre", "18:10", "Libre"],
            ["11:00", "Libre", "18:30", "Libre"],
            ["11:20", "Libre", "18:50", "Libre"],
            ["11:40", "Libre", "19:10", "Libre"]
    ]
arreglo_nombres_pacientes = []
arreglo_nombres_medicos = []





def menuPrincipal(app, main_view):
    global shipped_metric
    for widget in main_view.winfo_children():
        widget.destroy()


    ####################################### BUSQUEDA PACIENTES #############################################


    def actualizar_opciones_pac(event):
        global arreglo_nombres_pacientes
        with open('data/Pacientes.json', 'r') as file:
            arreglo_pacientes = json.load(file)   
        arreglo_nombres_pacientes = []
        for paciente in arreglo_pacientes:
            arreglo_nombres_pacientes.append(paciente['nombrePaciente'] + ' ' + paciente['apellidoPaciente'])
        texto_ingresado = campo_entrada_pac.get()
        opciones_filtradas = [nombre for nombre in arreglo_nombres_pacientes if texto_ingresado.lower() in nombre.lower()]
        comboPacientes["values"] = opciones_filtradas

    
    def seleccionar_opcion_pac(event):
        global arreglo_OS_paciente
        global  paciente_seleccionado
        paciente_seleccionado = campo_entrada_pac.get()
        print("Paciente seleccionado:", paciente_seleccionado)
        
        with open('data/Pacientes.json', 'r') as file:
            arreglo_pacientes = json.load(file)   
        for paciente in arreglo_pacientes:
            if paciente['nombrePaciente'] + ' ' + paciente['apellidoPaciente'] == paciente_seleccionado:
                for OS in paciente['arrayOS']:
                    arreglo_OS_paciente.append(OS['nombreObraSocial'])
                    comboOS["values"] = arreglo_OS_paciente
        
    ####################################### BUSQUEDA OBRA SOCIAL #############################################

    def actualizar_opciones_OS(event):
        texto_ingresado = campo_entrada_OS.get()
        opciones_filtradas = [OS for OS in arreglo_OS_paciente if texto_ingresado.lower() in OS.lower()]
        comboOS["values"] = opciones_filtradas

    
    def seleccionar_opcion_OS(event):
        global  OS_seleccionada
        OS_seleccionada = campo_entrada_OS.get()
        print("Obra Social seleccionada:", OS_seleccionada)
    
    ################################################# SELECCIONAR HORARIO ####################################################

    def actualizar_opciones_hora(event):
        texto_ingresado = campo_entrada_hora.get()
        opciones_filtradas = [hora for hora in arreglo_horarios if texto_ingresado.lower() in hora.lower()]
        comboHorario["values"] = opciones_filtradas

    
    def seleccionar_opcion_hora(event):
        global  horario_seleccionado
        horario_seleccionado = campo_entrada_hora.get()
        print("Horario seleccionado:", horario_seleccionado)
    
    ####################################### BUSQUEDA MEDICOS #############################################


    def actualizar_opciones_med(event):
        global arreglo_nombres_medicos
        with open('data/Medicos.json', 'r') as file:
            arreglo_medicos = json.load(file)   
        arreglo_nombres_medicos = []
        for medico in arreglo_medicos:
            arreglo_nombres_medicos.append(medico['nombreMedico'] + ' ' + medico['apellidoMedico'])

        texto_ingresado = campo_entrada_med.get()
        opciones_filtradas = [nombre for nombre in arreglo_nombres_medicos if texto_ingresado.lower() in nombre.lower()]
        comboMedicos["values"] = opciones_filtradas

    
    def seleccionar_opcion_med(event):
        global medico_seleccionado
        medico_seleccionado = campo_entrada_med.get()
        print("Medico seleccionado:", medico_seleccionado)
    
    ####################################### BUSQUEDA FECHA #############################################

    def mostrar_fecha(event):
        global  fecha_formateada
        fecha_seleccionada = cal.get_date()
        fecha_formateada = fecha_seleccionada.strftime("%d-%m-%Y")
        combo_fecha.set(fecha_formateada)
        print("Fecha seleccionada:",fecha_formateada)


    def buscarTurno(nombre):
        turno = None
        with open('data/Turnos.json') as file:
            turnos = json.load(file)
        for turno in turnos:
            if turno['paciente']['nombrePaciente'] + ' ' + turno['paciente']['apellidoPaciente'] == nombre and turno['medico']['nombreMedico'] + ' ' + turno['medico']['apellidoMedico'] == medico_seleccionado and turno['dia'] == fecha_formateada:
                print("Turno encontrado")
                return turno

        print("Turno no encontrado")

    ##############################################################################################

    def infoTurno(celda):
        global nombreCelda
        global hora_seleccionada
        nombreCelda = celda["value"]
        turno = buscarTurno(nombreCelda)
        if turno == None:
            lblNomPaciente.configure(text="Nombre: ")
            lblDNIPaciente.configure(text="DNI: ")
            lblOSPaciente.configure(text="Obra Social: ")
            lblNumPaciente.configure(text="Numero de afiliado:                     ")
            lblTelPaciente.configure(text="Teléfono: ")
            lblNomMedico.configure(text="Nombre: ")
            lblMailMedico.configure(text="Mail: ")
            lblUsuarioMedico.configure(text="Usuario de AMR: ")
            lblContrasenaMedico.configure(text="Contraseña de AMR: ")
            lblTelMedico.configure(text="Teléfono: ")
        else:
            hora_seleccionada = turno["horario"]
            lblNomPaciente.configure(text="Nombre: " + turno['paciente']['nombrePaciente'] + ' ' + turno['paciente']['apellidoPaciente'])
            lblDNIPaciente.configure(text="DNI: " + turno['paciente']['dni'])
            lblOSPaciente.configure(text="Obra Social: " + turno['obraSocial']['nombreObraSocial'])
            lblNumPaciente.configure(text="Numero de afiliado: " + turno['paciente']['nroAfiliado'])
            lblTelPaciente.configure(text="Teléfono: " + turno['paciente']['telefono'])
            lblNomMedico.configure(text="Nombre: " + turno['medico']['nombreMedico'] + ' ' + turno['medico']['apellidoMedico'])
            lblMailMedico.configure(text="Mail: " + turno['medico']['mail'])
            lblUsuarioMedico.configure(text="Usuario de AMR: " + turno['medico']['usuarioAMR'])
            lblContrasenaMedico.configure(text="Contraseña de AMR: " + turno['medico']['contrasenaAMR'])
            lblTelMedico.configure(text="Teléfono: " + turno['medico']['telefono'])

    ############################################## TABLA TURNOS ################################################

    def buscar_turnos_por_medico(nombre_medico, fecha):
        print(nombre_medico)
        print(fecha)
        turnos_del_medico = []
        turnos = []
        turno = None
        with open('data/Turnos.json') as file:
            turnos = json.load(file)
        for turno in turnos:
            if turno['medico']['nombreMedico'] + ' ' + turno['medico']['apellidoMedico'] == medico_seleccionado and turno['dia'] == fecha_formateada:
                turnos_del_medico.append(turno)
                for arreglo_interno in table_data:
                    arreglo_interno[1] = "Libre"
                    arreglo_interno[3] = "Libre"
                    if turnos_del_medico != []:
                        for turno in turnos_del_medico:
                            if arreglo_interno[0] == turno['horario']:
                                string = turno['paciente']['nombrePaciente'] + ' ' +turno['paciente']['apellidoPaciente']
                                arreglo_interno[1] = string
                            if arreglo_interno[2] == turno['horario']:
                                string = turno['paciente']['nombrePaciente'] + ' ' +turno['paciente']['apellidoPaciente']
                                arreglo_interno[3] = string
        print(turnos_del_medico)
        table.configure(values=table_data)
        table.update_values(table_data)

    ######################################### ELIMINAR TURNO ####################################################

    def eliminarTurno():
        turnoEliminar = buscarTurno(nombreCelda)
        with open('data/Turnos.json', 'r') as archivo:
            turnos = json.load(archivo)
        for turno in turnos:
            if turno == turnoEliminar:
                turnos.remove(turno)
                break
        with open('data/Turnos.json', 'w') as archivo:
            json.dump(turnos, archivo, indent=4)

    ############################################## BOTON RESERVAR TURNOS ################################################

    def reservarTurno():
        with open("data/Turnos.json", "r", encoding="utf-8") as archivo:
            turnos = json.load(archivo)
        if turnos == []:
            nuevo_id = 0
        else:
            ultimo_id = turnos[-1]["idTurno"]
            nuevo_id = ultimo_id + 1

        with open("data/Pacientes.json", "r", encoding="utf-8") as archivo:
            pacientes = json.load(archivo)
        for paciente in pacientes:
            if paciente['nombrePaciente'] + ' ' + paciente['apellidoPaciente'] == paciente_seleccionado:
                pacienteTurno = paciente

        with open("data/Medicos.json", "r", encoding="utf-8") as archivo:
            medicos = json.load(archivo)
        for medico in medicos:
            if medico['nombreMedico'] + ' ' + medico['apellidoMedico'] == medico_seleccionado:
                medicoTurno = medico

        with open("data/ObrasSociales.json", "r", encoding="utf-8") as archivo:
            obrasSociales = json.load(archivo)
        for OS in obrasSociales:
            if OS['nombreObraSocial'] == OS_seleccionada:
                obraSocialTurno = OS
                
        nueva_instancia = Turno(nuevo_id, fecha_formateada, horario_seleccionado, pacienteTurno, medicoTurno, obraSocialTurno)
        print(nueva_instancia)
        nuevo_objeto = {
            "idTurno": nueva_instancia.idTurno,
            "dia": nueva_instancia.dia,    
            "horario": nueva_instancia.horario,
            "paciente": nueva_instancia.paciente,
            "medico": nueva_instancia.medico,   
            "obraSocial": nueva_instancia.obraSocial
        }

        nuevo_objeto_json = json.dumps(nuevo_objeto)
        turnos.append(json.loads(nuevo_objeto_json))
        with open("data/Turnos.json", "w", encoding="utf-8") as archivo:
            json.dump(turnos, archivo, indent=4, ensure_ascii=False)
        print("Turno registrado")
        
    def validarTurno():
        ocupado = False
        if paciente_seleccionado == None:
            print("No seleccionó ningun paciente")
        elif fecha_formateada == None:
            print("No seleccionó ninguna fecha")
        elif medico_seleccionado == None:
            print("No seleccionó ningun medico")
        elif horario_seleccionado == None:
            print("No seleccionó ningun horario")
        else:
            with open('data/Turnos.json') as file:
                turnos = json.load(file)
            for turno in turnos:
                if turno['medico']['nombreMedico'] + ' ' + turno['medico']['apellidoMedico'] == medico_seleccionado and turno['horario'] == horario_seleccionado and turno['dia'] == fecha_formateada:
                    ocupado = True
            if ocupado == True:
                print("Fecha y horario ocupado para el medico seleccionado")
            else:
                reservarTurno()

    ######################################### PROGRAMA PRINCIPAL #########################################################
                
    ########################################## TÍTULO ####################################################

    title_frame = CTkFrame(master=main_view, fg_color="transparent")
    title_frame.pack(anchor="n", fill="x",  padx=27, pady=(29, 0))
    CTkLabel(master=title_frame, text="Turnos", font=("Arial Black", 25), text_color="#10302E").pack(anchor="nw", side="left")

    metrics_frame = CTkFrame(master=main_view, fg_color="transparent")
    metrics_frame.pack(anchor="n", fill="x",  padx=27, pady=(10, 0))

    ########################################## RESERVAR TURNO ####################################################

    resevar_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    resevar_container.pack(fill="x", pady=(10, 0), padx=27)
    CTkButton(master=resevar_container, text="Reservar turno",  font=("Arial", 14, "bold"), text_color="#F9F9FA", fg_color="#6BAAA2", hover_color="#55958D", width=130, command=validarTurno).grid(row=0, column=7, padx=(50,0), pady=10)    
    
    opcion_seleccionada_pac = tk.StringVar()

    data = Image.open("media/pacientes_verde.png")
    img = CTkImage(dark_image=data, light_image=data)
    label = CTkLabel(master=resevar_container, text='', image=img, fg_color="transparent",font=("Arial", 14, "bold"))
    label.grid(row=0, column=1, padx=(25,0), pady=10)

    comboPacientes = ttk.Combobox(master=resevar_container, textvariable=opcion_seleccionada_pac, width=20)
    comboPacientes.grid(row=0, column=2, padx=(10,25), pady=10)
    comboPacientes.bind("<<ComboboxSelected>>", seleccionar_opcion_pac)
    campo_entrada_pac = comboPacientes
    campo_entrada_pac.bind("<KeyRelease>", actualizar_opciones_pac)
    comboPacientes["values"] = arreglo_nombres_pacientes

    opcion_seleccionada_OS = tk.StringVar()

    data = Image.open("media/archivos.png")
    img = CTkImage(dark_image=data, light_image=data)
    label = CTkLabel(master=resevar_container, text='', image=img, fg_color="transparent",font=("Arial", 14, "bold"))
    label.grid(row=0, column=3, padx=(25,0), pady=10)

    comboOS = ttk.Combobox(master=resevar_container, textvariable=opcion_seleccionada_OS, width=35)
    comboOS.grid(row=0, column=4, padx=(10,25), pady=10)
    comboOS.bind("<<ComboboxSelected>>", seleccionar_opcion_OS)
    campo_entrada_OS = comboOS
    campo_entrada_OS.bind("<KeyRelease>", actualizar_opciones_OS)
    print(arreglo_OS_paciente)

    opcion_seleccionada_hora = tk.StringVar()

    comboHorario = ttk.Combobox(master=resevar_container, textvariable=opcion_seleccionada_hora, width=15)
    comboHorario.grid(row=0, column=6, padx=(10,0), pady=10)
    comboHorario.bind("<<ComboboxSelected>>", seleccionar_opcion_hora)
    campo_entrada_hora = comboHorario
    campo_entrada_hora.bind("<KeyRelease>", actualizar_opciones_hora)
    comboHorario["values"] = arreglo_horarios

    data = Image.open("media/hora.png")
    img = CTkImage(dark_image=data, light_image=data)
    label = CTkLabel(master=resevar_container, text='', image=img, fg_color="transparent",font=("Arial", 14, "bold"))
    label.grid(row=0, column=5, padx=(50,0), pady=10)


    ################################################### BUSCAR TURNOS ################################################################

    search_container = CTkFrame(master=main_view, height=50, fg_color="#F0F0F0")
    search_container.pack(fill="x", pady=(10, 0), padx=27)

    opcion_seleccionada_med = tk.StringVar()

    data = Image.open("media/medicos_verde.png")
    img = CTkImage(dark_image=data, light_image=data)
    label = CTkLabel(master=search_container, text='', image=img, fg_color="transparent",font=("Arial", 14, "bold"))
    label.grid(row=0, column=0, padx=(120,0), pady=10)

    comboMedicos = ttk.Combobox(master=search_container, textvariable=opcion_seleccionada_med, width=35)
    comboMedicos.grid(row=0, column=1, padx=(10,25), pady=10)
    comboMedicos.bind("<<ComboboxSelected>>", seleccionar_opcion_med)
    campo_entrada_med = comboMedicos
    campo_entrada_med.bind("<KeyRelease>", actualizar_opciones_med)
    comboMedicos["values"] = arreglo_nombres_medicos

    data = Image.open("media/turnos_verde.png")
    img = CTkImage(dark_image=data, light_image=data)
    label = CTkLabel(master=search_container, text='', image=img, fg_color="transparent",font=("Arial", 14, "bold"))
    label.grid(row=0, column=3, padx=(120,0), pady=10)

    cal = DateEntry(master=search_container, width=12, background='darkblue', foreground='white', borderwidth=2, locale="es_ES", date_pattern="dd-mm-yy")
    cal.grid(row=0, column=4, padx=(10,25), pady=10)
    combo_fecha = tk.StringVar()
    cal.bind("<<DateEntrySelected>>", mostrar_fecha) 

    ########################################## INFORMACION DEL TURNO ####################################################

    shipped_metric = CTkFrame(master=metrics_frame, fg_color="#85E6C0", width=930, height=160)
    shipped_metric.grid_propagate(0)
    shipped_metric.pack(side="left",expand=True, anchor="center")

    CTkLabel(master=shipped_metric, text="Informacion del paciente:", font=("Arial", 17, "bold"), anchor="w", text_color="black").grid(row=0, column=1, sticky="sw", pady=(10,15), padx=(15))

    lblNomPaciente = CTkLabel(master=shipped_metric, text="Nombre: ", font=("Arial", 15), anchor="w", text_color="black")
    lblNomPaciente.grid(row=1, column=1, sticky="sw", padx=15, pady=(4,0))
    lblDNIPaciente = CTkLabel(master=shipped_metric, text="DNI: ", font=("Arial", 15), anchor="w", text_color="black")
    lblDNIPaciente.grid(row=2, column=1, sticky="sw", padx=15, pady=(4,0))
    lblOSPaciente = CTkLabel(master=shipped_metric, text="Obra Social: ", font=("Arial", 15), anchor="w", text_color="black")
    lblOSPaciente.grid(row=3, column=1, sticky="sw", padx=15, pady=(4,0))
    
    lblPlanPaciente = CTkLabel(master=shipped_metric, text="Plan: ", font=("Arial", 15), anchor="w", text_color="black")
    lblPlanPaciente.grid(row=1, column=2, sticky="sw", padx=15)
    lblNumPaciente = CTkLabel(master=shipped_metric, text="Numero de afiliado:                     ", font=("Arial", 15), anchor="w", text_color="black")
    lblNumPaciente.grid(row=2, column=2, sticky="sw", padx=15)
    lblTelPaciente = CTkLabel(master=shipped_metric, text="Teléfono: ", font=("Arial", 15), anchor="w", text_color="black")
    lblTelPaciente.grid(row=3, column=2, sticky="sw", padx=15)

    CTkLabel(master=shipped_metric, text="Informacion del médico:", font=("Arial", 17, "bold"), anchor="w", text_color="black").grid(row=0, column=4, sticky="sw", pady=(10,15), padx=(15))
    
    lblNomMedico = CTkLabel(master=shipped_metric, text="Nombre: ", font=("Arial", 15), anchor="w", text_color="black")
    lblNomMedico.grid(row=1, column=4, sticky="sw", padx=(15))
    lblMailMedico = CTkLabel(master=shipped_metric, text="Mail: ", font=("Arial", 15), anchor="w", text_color="black")
    lblMailMedico.grid(row=2, column=4, sticky="sw", padx=(15))
    lblUsuarioMedico = CTkLabel(master=shipped_metric, text="Usuario de AMR: ", font=("Arial", 15), anchor="w", text_color="black")
    lblUsuarioMedico.grid(row=3, column=4, sticky="sw", padx=(15))
    
    lblContrasenaMedico = CTkLabel(master=shipped_metric, text="Contraseña de AMR: ", font=("Arial", 15), anchor="w", text_color="black")
    lblContrasenaMedico.grid(row=1, column=5, sticky="sw", padx=(15))
    lblTelMedico = CTkLabel(master=shipped_metric, text="Teléfono: ", font=("Arial", 15), anchor="w", text_color="black")
    lblTelMedico.grid(row=2, column=5, sticky="sw", padx=(15))

    ############################################## BOTON BUSCAR TURNOS ################################################

    table_frame = CTkFrame(master=main_view, fg_color="transparent")
    table_frame.pack(expand=True, fill="both", padx=27, pady=10)
    table = CTkTable(master=table_frame, values=table_data, colors=["#E6E6E6", "#EEEEEE"],  hover_color="#B4B4B4", width=600, command=infoTurno)
    table.pack(expand=True)


    btn = CTkButton(master=search_container, text="Buscar turnos",  font=("Arial", 14, "bold"), text_color="#F9F9FA", fg_color="#6BAAA2", hover_color="#55958D", width=130, command=lambda: buscar_turnos_por_medico(medico_seleccionado, fecha_formateada))
    btn.grid(row=0, column=5, padx=(100,0), pady=10)


    CTkButton(master=title_frame, text="Eliminar turno",  font=("Arial", 15, "bold"), text_color="#6BAAA2", fg_color="transparent", hover_color="#E6E6E6", width=130, border_color="#6BAAA2", border_width=2, command=eliminarTurno).pack(anchor="center", side="right", padx=(0,18))
   