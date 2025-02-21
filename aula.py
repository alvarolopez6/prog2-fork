class Aula:
    total_aulas = 0  # Contador de instancias
    def __init__(self, numero:int, capacidad:int, recursos:list[str]):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        self.reservada=False
        self.es_adecuada_para_clase=True
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula
    def mostrar_detalles(self):
        return repr(self)
    def __str__(self):
        return f"{self.numero},{self.capacidad},{self.recursos}"
    def __repr__(self):
        return (f"Numero: {self.numero}, Capacidad: {self.capacidad}, Recursos: {self.recursos}")
    @classmethod
    def desde_tupla(cls,tupla):
        return cls(*tupla)
    @staticmethod
    def es_adecuada_para_clase():
            print(f'La clase es adecuada para clase.')
    def reservar_aula(self):
        if self.reservada == False:
            print(f'Has reservado la aula numero {self.numero}')
            self.reservada=True
        else:
            print('Lo siento, la aula esta reservada.')