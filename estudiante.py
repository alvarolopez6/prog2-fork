class Estudiante:
    total_estudiantes = 0  # Contador de instancias

    def __init__(self, nombre:str, edad:int, cursos_inscritos:list[str]):
        self.nombre = nombre
        self.edad = edad
        self.cursos_inscritos = cursos_inscritos
        Estudiante.total_estudiantes += 1  # Aumenta el contador cada vez que se crea un estudiante
    def mostrar_informacion(self):
        print(repr(self))
    def __str__(self):
        return f"{self.nombre},{self.edad},{self.cursos_inscritos}"
    def __repr__(self):
        return f"nombre:{self.nombre}, edad:{self.edad}, cursos:{self.cursos_inscritos}"
    @staticmethod
    def es_mayor_de_edad(edad):
        if edad>=18:
            return True
        else:
            return False
    @classmethod
    def desde_tupla(cls,tupla):
        return cls(*tupla)
