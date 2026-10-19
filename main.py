
# Sistema de Gestion de Estudiantes
# Aplicacion desarrollada con programacion orientada a objetos.

class Estudiante:
    # Constructor: inicializa los datos del estudiante.
    def __init__(self, nombre, matricula, calificacion1,
                 calificacion2, calificacion3):
        self.nombre = nombre
        self.matricula = matricula
        self.calificacion1 = calificacion1
        self.calificacion2 = calificacion2
        self.calificacion3 = calificacion3

    # Metodo para calcular el promedio.
    def calcular_promedio(self):
        return (
            self.calificacion1
            + self.calificacion2
            + self.calificacion3
        ) / 3

    # Metodo para mostrar la informacion del estudiante.
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Matricula: {self.matricula}")
        print(f"Promedio: {self.calcular_promedio():.2f}")
        print("-------------------------")


# Programa principal: creacion de objetos.
def main():
    estudiante1 = Estudiante(
        "Ana Lopez", "EST001", 90, 85, 95
    )

    estudiante2 = Estudiante(
        "Carlos Perez", "EST002", 80, 88, 92
    )

    estudiante3 = Estudiante(
        "Maria Garcia", "EST003", 100, 95, 98
    )

    # Mostrar la informacion de los tres objetos.
    print("SISTEMA DE GESTION DE ESTUDIANTES")
    print("=========================")

    estudiante1.mostrar_informacion()
    estudiante2.mostrar_informacion()
    estudiante3.mostrar_informacion()


# Ejecutar el programa principal.
if __name__ == "__main__":
    main()
