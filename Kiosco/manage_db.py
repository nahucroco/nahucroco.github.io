import sqlite3
from tkinter import messagebox

DB_NAME = "Kiosco.db"



#cursor.execute('CREATE TABLE USUARIOS(USUARIO VARCHAR(20) PRIMARY KEY, CONTRASENA VARCHAR(20))')
#cursor.execute('CREATE TABLE PRODUCTOS(NOMBRE VARCHAR(40), CATEGORÍA VARCHAR(20), PESO REAL, MARCA VARCHAR(40), PRECIO REAL, CODIGO INTEGER PRIMARY KEY)')


def usuario_existe(nombre_usuario, contrasena):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute('SELECT usuario, contrasena FROM usuarios WHERE usuario = ? AND contrasena = ?', (nombre_usuario, contrasena))
    usuario = cursor.fetchone()
    return usuario is not None

def registrarUsuario(usuario, pass1):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    try:
        cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, pass1))
        conexion.commit()  # Confirmar la transacción para guardar los cambios en la base de datos
    except sqlite3.IntegrityError:
        return 'error1'
    except Exception as e:
        return 'error2'
        conexion.rollback()  # Revertir la transacción en caso de errorcursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)")

def editarArticuloDB(nombre, categoria, codigo, marca, peso, precio, ventana, var):  
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    if var == "agregar":
        cursor.execute('INSERT INTO PRODUCTOS (NOMBRE, CATEGORÍA, PESO, MARCA, PRECIO, CODIGO) VALUES (?, ?, ?, ?, ?, ?)', (nombre, categoria, peso, marca, precio, codigo))
        conexion.commit()
        ventana.destroy()
        messagebox.showinfo("Completado", 'Articulo cargado exitosamente')
    else:
        print(nombre)
        print(codigo)
        conexion.execute('UPDATE PRODUCTOS SET NOMBRE = ?, CATEGORÍA = ?, PESO = ?, MARCA = ?, PRECIO = ?, CODIGO = ? WHERE CODIGO = 85923',(nombre, categoria, peso, marca, precio, codigo,))
        conexion.commit()
        conexion.close()
        ventana.destroy()
        messagebox.showinfo("Completado", 'Articulo modificado exitosamente') 

def buscarArticuloDB(codigo):
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM PRODUCTOS WHERE CODIGO=?", (codigo,))
    articulo = cursor.fetchone()
    return(articulo)
