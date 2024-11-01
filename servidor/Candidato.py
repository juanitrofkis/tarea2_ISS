class Candidato:

    def __init__(self, dni: str, nombre: str, apellidos: str, perfil: str, experiencia: int, correo: str, cv: str):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.perfil = perfil
        self.experiencia = experiencia
        self.correo = correo
        self.cv = cv


    # Método para convertir el objeto a diccionario y poder serializarlo en JSON en la respuesta
    def a_diccionario(self):
        return { "dni": self.dni,
                 "nombre": self.nombre,
                 "apellidos": self.apellidos,
                 "perfil": self.perfil,
                 "experiencia": self.experiencia,
                 "correo": self.correo,
                 "cv": self.cv
                }