class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso: str, dia: str, hora_inicio: str, hora_fin: str) -> None:
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        type(self).total_horarios += 1

    def mostrar_horario(self) -> None:
        print(self)

    def modificar_horario(self, nuevo_horario: dict) -> None:
        if nuevo_horario.get('curso'):
            self.curso = nuevo_horario['curso']
        if nuevo_horario.get('dia'):
            self.dia = nuevo_horario['dia']
        if nuevo_horario.get('hora_inicio'):
            self.hora_inicio = nuevo_horario['hora_inicio']
        if nuevo_horario.get('hora_fin'):
            self.hora_fin = nuevo_horario['hora_fin']
    
    def __str__(self) -> str:
        return f'{self.curso} ~ {self.dia} >> {self.hora_inicio} - {self.hora_fin}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}(curso={self.curso}, dia={self.dia}, hora_inicio={self.hora_inicio}, hora_fin={self.hora_fin})'

    @classmethod
    def desde_tupla(cls, tupla: tuple):
        return cls(*tupla)

    @staticmethod
    def es_horario_valido(horario) -> bool:
        return horario.hora_inicio < horario.hora_fin

