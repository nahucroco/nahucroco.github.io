class Turno:
    def __init__(self, idTurno, dia, horario, paciente, medico, obraSocial):
        self.idTurno = idTurno
        self.dia = dia
        self.horario = horario
        self.paciente = paciente
        self.medico = medico
        self.obraSocial = obraSocial

class Paciente:
    def __init__(self, idPaciente, dni, telefono, apellidoPaciente, nombrePaciente, nroAfiliado, arrayOS):
        self.idPaciente = idPaciente
        self.dni = dni
        self.telefono = telefono
        self.apellidoPaciente = apellidoPaciente
        self.nombrePaciente = nombrePaciente
        self.nroAfiliado = nroAfiliado
        self.arrayOS = arrayOS

class Medico:
    def __init__(self, idMedico, usuarioAMR, contrasenaAMR, apellidoMedico, nombreMedico, telefono, mail, arrayOS):
        self.idMedico = idMedico
        self.usuarioAMR = usuarioAMR
        self.contrasenaAMR = contrasenaAMR
        self.apellidoMedico = apellidoMedico
        self.nombreMedico = nombreMedico
        self.telefono = telefono
        self.mail = mail
        self.arrayOS = arrayOS

class ObraSocial:
    def __init__(self, idObraSocial, nombreObraSocial, arrayPlanes):
        self.idObraSocial = idObraSocial
        self.nombreObraSocial = nombreObraSocial
        self.arrayPlanes = arrayPlanes
