from tkinter import Tk, Label, Button, Entry

import random
import os

class Futbolista:
    def __init__(self, nombre, edad, equipoActual, nacionalidad, ligaActual, posicion):
        self.nombre = nombre
        self.edad = edad
        self.equipoActual = equipoActual
        self.nacionalidad = nacionalidad
        self.ligaActual = ligaActual
        self.posicion = posicion

futbolista1a = Futbolista("Lionel Messi", 36, "Inter Miami", "Argentina", "MLS", "Delantero")
futbolista2a = Futbolista("Sergio Busquets", 35, "Inter Miami", "España", "MLS", "Mediocampista")
futbolista3a = Futbolista("Thiago Almada", 22, "Atlanta United", "Argentina", "MLS", "Mediocampista")
futbolista4a = Futbolista("Riqui Puig", 24, "Los Angeles Galaxy", "España", "MLS", "Mediocampista")


futbolista1b = Futbolista("Samuel Lino", 24, "Atletico Madrid", "Brasil", "LaLiga Santander", "Delantero")
futbolista2b = Futbolista("Nico Williams", 21, "Athletic Bilbao", "España", "LaLiga Santander", "Delantero")
futbolista3b = Futbolista("Nahuel Molina", 25, "Atletico Madrid", "Argentina", "LaLiga Santander", "Defensa")
futbolista4b = Futbolista("Pedri", 21, "Barcelona", "España", "LaLiga Santander", "Mediocampista")

futbolista1c = Futbolista("Mason Mount", 25, "Manchester United", "Inglaterra", "Premier League", "Mediocampista")
futbolista2c = Futbolista("Emre Can", 30, "Borussia Dortmund", "Alemania", "Bundesliga", "Mediocampista")
futbolista3c = Futbolista("Enzo Fernández", 23, "Chelsea", "Argentina", "Premier League", "Mediocampista")
futbolista4c = Futbolista("Rui Patricio", 35, "Wolverhampton", "Portugal", "Premier League", "Arquero")
futbolista5c = Futbolista("Gabriel Jesus", 26, "Arsenal", "Brasil", "Premier League", "Delantero")
futbolista6c = Futbolista("Reece James", 24, "Chelsea", "Inglaterra", "Premier League", "Defensa")
futbolista7c = Futbolista("Nelson Semedo", 30, "Wolverhampton", "Portugal", "Premier League", "Defensa")

futbolista1d = Futbolista("Goncalo Ramos", 22, "PSG", "Portugal", "Ligue One", "Delantero")
futbolista2d = Futbolista("Lucas Hernández", 27, "PSG", "Francia", "Ligue One", "Defensa")
futbolista3d = Futbolista("Vitinha", 23, "PSG", "Portugal", "Ligue One", "Mediocampista")
futbolista4d = Futbolista("Randal Kolo Muani", 25, "PSG", "Francia", "Ligue One", "Delantero")
futbolista5d = Futbolista("Alexandre Lacazette", 32, "Olympique Lyon", "Francia", "Ligue One", "Delantero")

futbolista1e = Futbolista("Mike Maignan", 28, "Milan", "Francia", "Serie A", "Arquero")
futbolista2e = Futbolista("Benjamin Pavard", 27, "Inter", "Francia", "Serie A", "Defensa")
futbolista3e = Futbolista("Tammy Abraham", 26, "Roma", "Inglaterra", "Serie A", "Delantero")
futbolista4e = Futbolista("Luis Alberto", 31, "Lazio", "España", "Serie A", "Mediocampista")
futbolista5e = Futbolista("Bremer", 26, "Juventus", "Brasil", "Serie A", "Defensa")

futbolista1f = Futbolista("Dani Olmo", 25, "Leipzig", "España", "Bundesliga", "Mediocampista")
futbolista2f = Futbolista("Exequiel Palacios", 25, "Bayer Leverkusen", "Argentina", "Bundesliga", "Mediocampista")
futbolista3f = Futbolista("Julian Brandt", 30, "Borussia Dortmund", "Alemania", "Bundesliga", "Mediocampista")
futbolista4f = Futbolista("Alejandro Grimaldo", 28, "Bayer Leverkusen", "España", "Bundesliga", "Defensa")
futbolista5f = Futbolista("Harry Kane", 30, "Bayern", "Inglaterra", "Bundesliga", "Delantero")

futbolistas = [
    futbolista1a,
    futbolista2a,
    futbolista3a,
    futbolista4a,
    futbolista1b,
    futbolista2b,
    futbolista3b,
    futbolista4b,
    futbolista1c,
    futbolista2c,
    futbolista3c,
    futbolista4c,
    futbolista5c,
    futbolista6c,
    futbolista7c,
    futbolista1d,
    futbolista2d,
    futbolista3d,
    futbolista4d,
    futbolista5d,
    futbolista1e,
    futbolista2e,
    futbolista3e,
    futbolista4e,
    futbolista5e,
    futbolista1f,
    futbolista2f,
    futbolista3f,
    futbolista4f,
    futbolista5f,
]

futbolista_random = random.choice(futbolistas)
print(futbolista_random.nombre)


intentos = 3
preguntas = 8
futbolista = str
op1 = 0
op = 0

################################ CONFIGURACION DE VENTANA #########################################
    
ventana = Tk()
ventana.geometry("606x810+680+100")
ventana.title("VentanaHolaMundo")
ventana.configure(bg="#64908a")

######################################## RESPONDER NO #############################################

def responderNo():
    for widget in ventana.winfo_children():
        widget.pack_forget()            
    lbl = Label(ventana, text='No', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)

######################################## RESPONDER SI #############################################

def responderSi():
    for widget in ventana.winfo_children():
        widget.pack_forget()            
    lbl = Label(ventana, text='Si', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)

###################################### RESPONDER POR EDAD ###########################################

def responderEdad(op1):
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
        
    if op1 == 1 and 20 > futbolista_random.edad >= 15:
        responderSi()
    elif op1 == 1 and 20 <= futbolista_random.edad or futbolista_random.edad < 15:
        responderNo()
    elif op1 == 2 and 25 > futbolista_random.edad >= 20:
        responderSi()
    elif op1 == 2 and 25 <= futbolista_random.edad or futbolista_random.edad < 20:
        responderNo()
    elif op1 == 3 and 30 > futbolista_random.edad >= 25:
        responderSi()
    elif op1 == 3 and 30 <= futbolista_random.edad or futbolista_random.edad < 25:
        responderNo()
    elif op1 == 4 and 35 > futbolista_random.edad >= 30:
        responderSi()
    elif op1 == 4 and 35 <= futbolista_random.edad or futbolista_random.edad < 30:
        responderNo()
    elif op1 == 5 and 40 > futbolista_random.edad >= 35:
        responderSi()
    elif op1 == 5 and 40 <= futbolista_random.edad or futbolista_random.edad < 35:
        responderNo()

    preguntas = preguntas - 1

    lbl = Label(ventana, text='Le quedan ' + str(preguntas) + ' preguntas', font=("Arial", 26), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)

    btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
    btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    btn1.pack(pady=15)

    ventana.mainloop()     

######################################## PREGUNTAR POR EDAD #########################################

def preguntarEdad():
    global preguntas
    global futbolista_random
    for widget in ventana.winfo_children():
        widget.pack_forget()
    
    lbl = Label(ventana, text='Eligió preguntar por edad', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(pady=15)

    btn1 = Button(ventana, text='¿Tiene entre 15 y 20 años?', command=lambda: responderEdad(1))
    btn1.pack(pady=15)
 
    btn2 = Button(ventana, text='¿Tiene entre 20 y 25 años?', command=lambda: responderEdad(2))
    btn2.pack(pady=15)

    btn3 = Button(ventana, text='¿Tiene entre 25 y 30 años?', command=lambda: responderEdad(3))
    btn3.pack(pady=15)

    btn4 = Button(ventana, text='¿Tiene entre 30 y 35 años?', command=lambda: responderEdad(4))
    btn4.pack(pady=15)

    btn5 = Button(ventana, text='¿Tiene entre 35 y 40 años?', command=lambda: responderEdad(5))
    btn5.pack(pady=15) 

    botones = [btn1, btn2, btn3, btn4, btn5]
    for boton in botones:
        boton.config(height=2, width=45, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    ventana.mainloop()  

##################################### RESPONDER POR EQUIPO ##########################################

def responderEquipo(op):
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()

    if op == 1 and futbolista_random.equipoActual == "Bayern":
        responderSi()
    elif op == 1 and futbolista_random.equipoActual != "Bayern":
        responderNo()
    elif op == 2 and futbolista_random.equipoActual == "Barcelona":
        responderSi()
    elif op == 2 and futbolista_random.equipoActual != "Barcelona":
        responderNo()
    elif op == 3 and futbolista_random.equipoActual == "Borussia Dortmund":
        responderSi()
    elif op == 3 and futbolista_random.equipoActual != "Borussia Dortmund":
        responderNo()
    elif op == 4 and futbolista_random.equipoActual == "Atletico Madrid":
        responderSi()
    elif op == 4 and futbolista_random.equipoActual != "Atletico Madrid":
        responderNo()
    elif op == 5 and futbolista_random.equipoActual == "PSG":
        responderSi()
    elif op == 5 and futbolista_random.equipoActual != "PSG":
        responderNo()
    elif op == 6 and futbolista_random.equipoActual == "Inter Miami":
        responderSi()
    elif op == 6 and futbolista_random.equipoActual != "Inter Miami":
        responderNo()
    elif op == 7 and futbolista_random.equipoActual == "Manchester United":
        responderSi()
    elif op == 7 and futbolista_random.equipoActual != "Manchester United":
        responderNo()
    elif op == 8 and futbolista_random.equipoActual == "Inter":
        responderSi()
    elif op == 8 and futbolista_random.equipoActual != "Inter":
        responderNo()
    elif op == 9 and futbolista_random.equipoActual == "Juventus":
        responderSi()
    elif op == 9 and futbolista_random.equipoActual != "Juventus":
        responderNo()
    elif op == 10 and futbolista_random.equipoActual == "Milan":
        responderSi()
    elif op == 10 and futbolista_random.equipoActual != "Milan":
        responderNo()
    elif op == 11 and futbolista_random.equipoActual == "Arsenal":
        responderSi()
    elif op == 11 and futbolista_random.equipoActual != "Arsenal":
        responderNo()
    elif op == 12 and futbolista_random.equipoActual == "Chelsea":
        responderSi()
    elif op == 12 and futbolista_random.equipoActual != "Chelsea":
        responderNo()
    elif op == 13 and futbolista_random.equipoActual == "Atheltic Bilbao":
        responderSi()
    elif op == 13 and futbolista_random.equipoActual != "Atheltic Bilbao":
        responderNo()
    elif op == 14 and futbolista_random.equipoActual == "Wolverhampton":
        responderSi()
    elif op == 14 and futbolista_random.equipoActual != "Wolverhampton":
        responderNo()
    elif op == 15 and futbolista_random.equipoActual == "Bayer Leverkusen":
        responderSi()
    elif op == 15 and futbolista_random.equipoActual != "Bayer Leverkusen":
        responderNo()
    elif op == 16 and futbolista_random.equipoActual == "Lazio":
        responderSi()
    elif op == 16 and futbolista_random.equipoActual != "Lazio":
        responderNo()
    elif op == 17 and futbolista_random.equipoActual == "Roma":
        responderSi()
    elif op == 17 and futbolista_random.equipoActual != "Roma":
        responderNo()
    elif op == 18 and futbolista_random.equipoActual == "Lens":
        responderSi()
    elif op == 18 and futbolista_random.equipoActual != "Lens":
        responderNo()
    elif op == 19 and futbolista_random.equipoActual == "Leipzig":
        responderSi()
    elif op == 19 and futbolista_random.equipoActual != "Leipzig":
        responderNo()
    elif op == 20 and futbolista_random.equipoActual == "Olympique Lyon":
        responderSi()
    elif op == 20 and futbolista_random.equipoActual != "Olympique Lyon":
        responderNo()

    preguntas = preguntas - 1

    lbl = Label(ventana, text='Le quedan ' + str(preguntas) + ' preguntas', font=("Arial", 26), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)


    btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
    btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    btn1.pack(pady=15)

    ventana.mainloop()  

###################################### PREGUNTAR POR EQUIPO #########################################

def preguntarEquipo():
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
    
    lbl = Label(ventana, text='Eligió preguntar por equipo', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(padx=10, pady=2) 

    btn1 = Button(ventana, text='¿Juega en el Bayern?', command=lambda: responderEquipo(1))
    btn1.pack(pady=2)
 
    btn2 = Button(ventana, text='¿Juega en el Barcelona?', command=lambda: responderEquipo(2))
    btn2.pack(pady=2)

    btn3 = Button(ventana, text='¿Juega en el Borussia Dortmund?', command=lambda: responderEquipo(3))
    btn3.pack(pady=2)

    btn4 = Button(ventana, text='¿Juega en el Atletico Madrid?', command=lambda: responderEquipo(4))
    btn4.pack(pady=2)

    btn5 = Button(ventana, text='¿Juega en el PSG?', command=lambda: responderEquipo(5))
    btn5.pack(pady=2) 

    btn6 = Button(ventana, text='¿Juega en el Inter Miami?', command=lambda: responderEquipo(6))
    btn6.pack(pady=2) 

    btn7 = Button(ventana, text='¿Juega en el Manchester United?', command=lambda: responderEquipo(7))
    btn7.pack(pady=2) 

    btn8 = Button(ventana, text='¿Juega en el Inter?', command=lambda: responderEquipo(8))
    btn8.pack(pady=2) 

    btn9 = Button(ventana, text='¿Juega en la Juventus?', command=lambda: responderEquipo(9))
    btn9.pack(pady=2) 

    btn10 = Button(ventana, text='¿Juega en el Milan?', command=lambda: responderEquipo(10))
    btn10.pack(pady=2) 

    btn11 = Button(ventana, text='¿Juega en el Arsenal?', command=lambda: responderEquipo(11))
    btn11.pack(pady=2) 

    btn12 = Button(ventana, text='¿Juega en el Chelsea?', command=lambda: responderEquipo(12))
    btn12.pack(pady=2) 

    btn13 = Button(ventana, text='¿Juega en el Atheltic Bilbao?', command=lambda: responderEquipo(13))
    btn13.pack(pady=2) 

    btn14 = Button(ventana, text='¿Juega en el Wolverhampton?', command=lambda: responderEquipo(14))
    btn14.pack(pady=2) 

    btn15 = Button(ventana, text='¿Juega en el Bayer Leverkusen?', command=lambda: responderEquipo(15))
    btn15.pack(pady=2) 

    btn16 = Button(ventana, text='¿Juega en la Lazio?', command=lambda: responderEquipo(16))
    btn16.pack(pady=2) 

    btn17 = Button(ventana, text='¿Juega en la Roma?', command=lambda: responderEquipo(17))
    btn17.pack(pady=2) 

    btn18 = Button(ventana, text='¿Juega en el Lens?', command=lambda: responderEquipo(18))
    btn18.pack(pady=2) 

    btn19 = Button(ventana, text='¿Juega en el Leipzig?', command=lambda: responderEquipo(19))
    btn19.pack(pady=2) 
        
    btn20 = Button(ventana, text='¿Juega en el Olympique Lyon?', command=lambda: responderEquipo(20))
    btn20.pack(pady=2) 


    botones = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20]
    for boton in botones:
        boton.config(height=1, width=29, font=("Arial", 13), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    ventana.mainloop()  
 
################################## RESPONDER POR NACIONALIDAD #######################################

def responderNacionalidad(op):
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()

    if op == 1 and futbolista_random.nacionalidad == "Argentina":
        responderSi()
    elif op == 1 and futbolista_random.nacionalidad != "Argentina":
        responderNo()
    elif op == 2 and futbolista_random.nacionalidad == "Inglaterra":
        responderSi()
    elif op == 2 and futbolista_random.nacionalidad != "Inglaterra":
        responderNo()
    elif op == 3 and futbolista_random.nacionalidad == "España":
        responderSi()
    elif op == 3 and futbolista_random.nacionalidad != "España":
        responderNo()
    elif op == 4 and futbolista_random.nacionalidad == "Alemania":
        responderSi()
    elif op == 4 and futbolista_random.nacionalidad != "Alemania":
        responderNo()
    elif op == 5 and futbolista_random.nacionalidad == "Portugal":
        responderSi()
    elif op == 5 and futbolista_random.nacionalidad != "Portugal":
        responderNo()
    elif op == 6 and futbolista_random.nacionalidad == "Brasil":
        responderSi()
    elif op == 6 and futbolista_random.nacionalidad != "Brasil":
        responderNo()
    elif op == 7 and futbolista_random.nacionalidad == "Francia":
        responderSi()
    elif op == 7 and futbolista_random.nacionalidad != "Francia":
        responderNo()

    preguntas = preguntas - 1

    lbl = Label(ventana, text='Le quedan ' + str(preguntas) + ' preguntas', font=("Arial", 26), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)


    btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
    btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    btn1.pack(pady=15)

    ventana.mainloop()  

##################################### PREGUNTAR POR NACIONALIDAD ####################################

def preguntarNacionalidad():
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
    
    lbl = Label(ventana, text='Eligió preguntar por nacionalidad', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(padx=10, pady=15) 

    btn1 = Button(ventana, text='¿Es de nacionalidad Argentina?', command=lambda: responderNacionalidad(1))
    btn1.pack(pady=15)
 
    btn2 = Button(ventana, text='¿Es de nacionalidad Inglesa?', command=lambda: responderNacionalidad(2))
    btn2.pack(pady=15)

    btn3 = Button(ventana, text='¿Es de nacionalidad Española?', command=lambda: responderNacionalidad(3))
    btn3.pack(pady=15)

    btn4 = Button(ventana, text='¿Es de nacionalidad Alemana?', command=lambda: responderNacionalidad(4))
    btn4.pack(pady=15)

    btn5 = Button(ventana, text='¿Es de nacionalidad Portuguesa?', command=lambda: responderNacionalidad(5))
    btn5.pack(pady=15) 

    btn6 = Button(ventana, text='¿Es de nacionalidad Brasileña?', command=lambda: responderNacionalidad(6))
    btn6.pack(pady=15) 

    btn7 = Button(ventana, text='¿Es de nacionalidad Francesa', command=lambda: responderNacionalidad(7))
    btn7.pack(pady=15) 

    botones = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]
    for boton in botones:
        boton.config(height=2, width=45, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    ventana.mainloop()  

##################################### RESPONDER POR LIGA ############################################

def responderLiga(op):
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
        

    if op == 1 and futbolista_random.ligaActual == "LaLiga Santander":
        responderSi()
    elif op == 1 and futbolista_random.ligaActual != "LaLiga Santander":
        responderNo()
    elif op == 2 and futbolista_random.ligaActual == "MLS":
        responderSi()
    elif op == 2 and futbolista_random.ligaActual != "MLS":
        responderNo()
    elif op == 3 and futbolista_random.ligaActual == "Bundesliga":
        responderSi()
    elif op == 3 and futbolista_random.ligaActual != "Bundesliga":
        responderNo()
    elif op == 4 and futbolista_random.ligaActual == "Premier League":
        responderSi()
    elif op == 4 and futbolista_random.ligaActual != "Premier League":
        responderNo()
    elif op == 5 and futbolista_random.ligaActual == "Ligue One":
        responderSi()
    elif op == 5 and futbolista_random.ligaActual != "Ligue One":
        responderNo()
    elif op == 6 and futbolista_random.ligaActual == "Serie A":
        responderSi()
    elif op == 6 and futbolista_random.ligaActual != "Serie A":
        responderNo()

    preguntas = preguntas - 1

    lbl = Label(ventana, text='Le quedan ' + str(preguntas) + ' preguntas', font=("Arial", 26), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)


    btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
    btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    btn1.pack(pady=15)

    ventana.mainloop()  

######################################## PREGUNTAR POR LIGA #########################################

def preguntarLiga():
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
    
    lbl = Label(ventana, text='Eligió preguntar por liga', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(padx=10, pady=15) 

    btn1 = Button(ventana, text='¿Juega en LaLiga Santander?', command=lambda: responderLiga(1))
    btn1.pack(pady=15)
 
    btn2 = Button(ventana, text='¿Juega en la MLS?', command=lambda: responderLiga(2))
    btn2.pack(pady=15)

    btn3 = Button(ventana, text='¿Juega en la Bundesliga?', command=lambda: responderLiga(3))
    btn3.pack(pady=15)

    btn4 = Button(ventana, text='¿Juega en la Premier League?', command=lambda: responderLiga(4))
    btn4.pack(pady=15)

    btn5 = Button(ventana, text='¿Juega en la Ligue One?', command=lambda: responderLiga(5))
    btn5.pack(pady=15) 

    btn6 = Button(ventana, text='¿Juega en la Serie A?', command=lambda: responderLiga(6))
    btn6.pack(pady=15) 

    botones = [btn1, btn2, btn3, btn4, btn5, btn6]
    for boton in botones:
        boton.config(height=2, width=45, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    ventana.mainloop()  

#################################### RESPONDER POR POSICION #########################################

def responderPosicion(op):
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
        

    if op == 1 and futbolista_random.posicion == "Arquero":
        responderSi()
    elif op == 1 and futbolista_random.posicion != "Arquero":
        responderNo()
    elif op == 2 and futbolista_random.posicion == "Defensa":
        responderSi()
    elif op == 2 and futbolista_random.posicion != "Defensa":
        responderNo()
    elif op == 3 and futbolista_random.posicion == "Mediocampista":
        responderSi()
    elif op == 3 and futbolista_random.posicion != "Mediocampista":
        responderNo()
    elif op == 4 and futbolista_random.posicion == "Delantero":
        responderSi()
    elif op == 4 and futbolista_random.posicion != "Delantero":
        responderNo()

    preguntas = preguntas - 1

    lbl = Label(ventana, text='Le quedan ' + str(preguntas) + ' preguntas', font=("Arial", 26), bg="#64908a", fg="#42342F")
    lbl.pack(pady=40)


    btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
    btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    btn1.pack(pady=15)

    ventana.mainloop()  

###################################### PREGUNTAR POR POSICION #######################################

def preguntarPosicion():
    global preguntas
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
    
    lbl = Label(ventana, text='Eligió preguntar por posicion', font=("Arial", 30), bg="#64908a", fg="#42342F")
    lbl.pack(padx=10, pady=15) 

    btn1 = Button(ventana, text='¿Juega como arquero?', command=lambda: responderPosicion(1))
    btn1.pack(pady=15)
 
    btn2 = Button(ventana, text='¿Juega como defensa?', command=lambda: responderPosicion(2))
    btn2.pack(pady=15)

    btn3 = Button(ventana, text='¿Juega como mediocampista?', command=lambda: responderPosicion(3))
    btn3.pack(pady=15)

    btn4 = Button(ventana, text='¿Juega como delantero?', command=lambda: responderPosicion(4))
    btn4.pack(pady=15)

    botones = [btn1, btn2, btn3, btn4]
    for boton in botones:
        boton.config(height=2, width=45, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    ventana.mainloop()  

    #################### ARRIESGAR ####################

############################################ ARRIESGAR ##############################################
    
def obtener_texto(entrada):
    global preguntas
    global op1
    global futbolista_random
    global futbolista
    global intentos

    for widget in ventana.winfo_children():
        widget.pack_forget()

    texto_ingresado = entrada.get()
    etiqueta_resultado = Label(ventana, font=("Arial", 30), bg="#64908a", fg="#42342F")
    etiqueta_resultado.config(text="Texto ingresado: " + texto_ingresado)
    
    if texto_ingresado != futbolista_random.nombre:
        for widget in ventana.winfo_children():
            widget.pack_forget()
        lbl1 = Label(ventana, text='Futbolista equivocado!', font=("Arial", 30), bg="#64908a", fg="#42342F")
        lbl1.pack(padx=10, pady=20) 
        intentos = intentos - 1 
        lbl2 = Label(ventana, text='Le quedan ' + str(intentos) + ' intentos', font=("Arial", 20), bg="#64908a", fg="#42342F")
        lbl2.pack(padx=10, pady=10) 
        
        btn1 = Button(ventana, text='Continuar', command=menuPrincipal)
        btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
        btn1.pack(pady=70)
        

    elif texto_ingresado == futbolista_random.nombre:
        for widget in ventana.winfo_children():
            widget.pack_forget()

        lbl1 = Label(ventana, text='USTED HA GANADO!', font=("Arial", 30), bg="#64908a", fg="#42342F")
        lbl1.pack(padx=10, pady=60) 
        
        btn1 = Button(ventana, text='Salir', command=funcSalir)
        btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
        btn1.pack(pady=65)


def arriesgar():
    global preguntas
    global op1
    global futbolista_random

    for widget in ventana.winfo_children():
        widget.pack_forget()
        

    # Crear la entrada de texto
    lbl = Label(ventana, text='Ingrese nombre y apellido del futbolista ', font=("Arial", 25), bg="#64908a", fg="#42342F")
    lbl.pack(padx=10, pady=25) 
    entrada = Entry(ventana)
    entrada.config(width=25, font=("Arial", 15))
    entrada.pack(pady=30)

    # Crear un botón para obtener el texto ingresado
    boton_obtener_texto = Button(ventana, text="Ingresar", command=lambda :obtener_texto(entrada))
    boton_obtener_texto.config(height=1, width=25, font=("Arial", 15), relief="ridge", cursor="hand2", bg="#e8caa4", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")
    boton_obtener_texto.pack(pady=35)


#################################### SALIR ###############################################
    
def funcSalir():
    ventana.destroy()

#################################### MENU PRINCIPAL ###############################################

def menuPrincipal():
    global salir
    global preguntas
    global futbolista_random
    global futbolista
    global op1
    global intentos



    for widget in ventana.winfo_children():
        widget.pack_forget()

    lbl = Label(ventana, text='Adivina el futbolista!', font=("Arial", 42), bg="#64908a", fg="#42342F")
    lbl.pack(pady=17)

    btn1 = Button(ventana, text='Preguntar por edad', command=preguntarEdad)
    btn1.pack(pady=17)

    btn2 = Button(ventana, text='Preguntar por equipo', command=preguntarEquipo)
    btn2.pack(pady=17)

    btn3 = Button(ventana, text='Preguntar por nacionalidad', command=preguntarNacionalidad)
    btn3.pack(pady=17)

    btn4 = Button(ventana, text='Preguntar por liga', command=preguntarLiga)
    btn4.pack(pady=17)

    btn5 = Button(ventana, text='Preguntar por posicion', command=preguntarPosicion)
    btn5.pack(pady=17)

    btn6 = Button(ventana, text='Arriesgar', command=arriesgar)
    btn6.pack(pady=17)

    btn7 = Button(ventana, text='Salir', command=funcSalir)
    btn7.pack(pady=17)

    botones = [btn1, btn2, btn3, btn4, btn5, btn6, btn7]

    for boton in botones:
        boton.config(height=2, width=45, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D", fg="#42342F")

    if preguntas <= 0:
        for widget in ventana.winfo_children():
            widget.pack_forget()
        lbl = Label(ventana, text='Superó el limite de preguntas!', font=("Arial", 30), bg="#64908a", fg="#42342F")
        lbl.pack(pady=15)
        lbl2 = Label(ventana, text='El futbolista era: ' + futbolista_random.nombre, font=("Arial", 25), bg="#64908a", fg="#42342F")
        lbl2.pack(pady=15)
        btn1 = Button(ventana, text='Salir', command=funcSalir)
        btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D")
        btn1.pack(pady=15)

    elif intentos <= 0:

        for widget in ventana.winfo_children():
            widget.pack_forget()

        lbl1 = Label(ventana, text='Superó el limite de intentos!', font=("Arial", 30), bg="#64908a", fg="#42342F")
        lbl1.pack(padx=10, pady=20) 
        intentos = intentos - 1 
        lbl2 = Label(ventana, text='El futbolista era ' + futbolista_random.nombre, font=("Arial", 20), bg="#64908a", fg="#42342F")
        lbl2.pack(padx=10, pady=10) 
        
        btn1 = Button(ventana, text='Salir', command=funcSalir)
        btn1.config(height=1, width=25, font=("Arial", 15), relief="ridge", bg="#e8caa4", cursor="hand2", borderwidth=0, activebackground="#E2BC8D")
        btn1.pack(pady=70)
        


    ventana.mainloop() 

##################################################################################################


menuPrincipal()






