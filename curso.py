class Curso:
    total_cursos = 0  # Contador de instancias

    def __init__(self, nombre, codigo, descripcion):
        self.nombre = nombre
        self.codigo = codigo
        self.descripcion = descripcion
        Curso.total_cursos += 1  # Aumenta el contador cada vez que se crea un curso

    def mostrar_detalles(self):
        print('Detalles:')
        print(f"Nombre: {self.nombre}")
        print(f"Codigo: {self.codigo}")
        print(f"Descripcion: {self.descripcion}")

    def actualizar_descripcion(self, nueva_descripcion: str):
        self.descripcion = nueva_descripcion
        print(f"Se ha actualizado la descripción del curso {self.nombre}")

    def __str__(self):
        return f"{self.nombre}, {self.codigo}, {self.descripcion}"

    def __repr__(self):
        return f"Curso:('{self.nombre}','{self.codigo}', '{self.descripcion}')"

    @classmethod
    def desde_tupla(cls, tupla):
        return cls(*tupla)