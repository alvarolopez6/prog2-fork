class Vigilante:
    total_vigilantes = 0
    lista_vigilantes = []

    def __init__(self,nombre:str,especialidad:str,turnos_asignados:list[str]):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos_asignados = turnos_asignados
        Vigilante.total_vigilantes += 1
        Vigilante.lista_vigilantes.append(self.nombre)

    def asignar_turno(self, turno:str):
        if turno in self.turnos_asignados:
            pass
        else:
            self.turnos_asignados.append(turno)

    def mostrar_informacion(self):
        return (self.nombre, self.especialidad, self.turnos_asignados)

    def __str__(self):
        return (f'Nombre: {self.nombre} \nEspecialidad: {self.especialidad} \n Turnos asignados: {self.turnos_asignados}')

    def __repr__(self):
        return (f'Vigilante(nombre = {self.nombre}, especialidad = {self.especialidad}, turnos_asignados = {self.turnos_asignados})')

    @classmethod
    def desde_tupla(cls, tupla:tuple):
        return cls(*tupla)

    @staticmethod
    def esta_disponible(nombre:str):
        if nombre in Vigilante.lista_vigilantes:
            return 'Disponible'
        else:
            return 'No disponible'



