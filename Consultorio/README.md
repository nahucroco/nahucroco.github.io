# Proyecto administración de consultorio

Este proyecto fue realizado con el fin de seguir afianzando mis conocimientos en Python, POO y UX/UI además de incluir nuevas librerías, métodos y archivos. Si bien muchas de sus funcionalidades
ya se pueden utilizar, el proyecto aún esta en desarrollo. 

# Instructivo

- Se debe ejecutar el archivo "main.py". Éste se encuentra conectado por los demás módulos python importados al principio.
- Registro de turnos: Para registrar un turno se debe seleccionar un paciente, un médico, una obra social, un horario y un día. Mientras el turno no esté ocupado, este se registrará.
- Búsqueda de turnos: Para buscar un turno se debe selecionar un médico y un día. Luego los turnos con dichos atributos se mostrarám en la tabla ubicada en la interfaz. Se deberá clickear sobre uno de los turnos
registrados para obtener su información.
- Registro de pacientes, médicos y obras sociales: Para registrar una instancia de cualquiera de las clases anteriormente nombradas, se debe ingresar los datos pedidos. En los médicos y los pacientes, seleccionar
una obra social, luego presionar el botón de agregar, se debe realizar este procedimiento para cada obra social asignada a un medico o paciente. Lo mismo aplica para los planes en el caso de registrar una nueva
obra social.

# Funcionamiento

El sistema está realizado en Python, con librerías como Customtkinter, tkinter y json. Para reservar un turno primero deben existir al menos un paciente, una obra social y un médico. Además, el horario 
seleccionado debe estar disponible. El programa principal se encuentra en "main.py", y dicho archivo tiene importados los modulos correspondientes a la carga de instancias de cada clase, además de un módulo
en donde se encuentran todas las clases creadas. En la carpeta media se encuentran las imágenes e iconos utilizados en formato png e ico. En la carpeta data se encuentran los archivos con extensión JSON en 
donde se carga cada instancia creada. En la carpeta files se hayan dos archivos de word, correspondientes al caso de uso y al modelo de dominio del sistema, además de un prototipo realizado en figma.

# Fallas y correciones en proceso

- Dar de baja a una instancia de cualquier clase.
- Seleccionar un plan a la hora de registrar nuevo turno.
- Mostrar mensajes de alerta al usuario que actualmente se muestran en consola.
- La tabla de turnos no se actualiza cuando eliminamos un turno y luego volvemos a pulsar "Buscar".
- Cuando vamos a seleccionar una obra social para registrar un nuevo turno algunas de estas se muestran repetidas veces.
