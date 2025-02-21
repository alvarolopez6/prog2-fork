class Profesor:
    total_profesores = 0
    def __init__(self, nombre: str, especialidad: str, cursos_asignados: list[str]):
        self.nombre = nombre
        self.especialidad = especialidad
        self.cursos_asignados = cursos_asignados
        type(self).total_profesores += 1

    def asignar_curso(self, curso: str):
        if curso not in self.cursos_asignados:
            self.cursos_asignados.append(curso)
            return f'El curso {curso} se ha asignado correctamente'
        else:
            return f'El curso {curso} ya esta asignado'

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
        print(f'Especialidad: {self.especialidad}')
        print(f'Cursos asignados:')
        for curso in self.cursos_asignados:
            print(f'- {curso}')

    def __str__(self):
        return (f'{self.nombre}, especialidad: {self.especialidad},'
                f'cursos asignados: {self.cursos_asignados}')

    def __repr__(self):
        return f'Profesor({self.nombre}, {self.especialidad}, {self.cursos_asignados})'

    @classmethod
    def desde_tupla(cls, tupla: tuple):
        return cls(*tupla)

    @staticmethod
    def esta_disponible_para_nuevo_curso():
        print("Sí, lo está")
