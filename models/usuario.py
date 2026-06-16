class Usuario:

    #Constructor 
    def __int__(self, id_usuario, nombre, matricula, email, carrera):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.matricula = matricula
        self.email = email
        self.carrera = carrera
        self.activo = True

    def activar (self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    return f "Nombre: {self.nombre}, Matricula: {self.matricula}, Email:{self.email}, Carrera: {self.carrera}"
