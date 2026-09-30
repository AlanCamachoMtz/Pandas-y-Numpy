class Persona:
    def __init__(self, nombre, apellido):
        if not nombre or not apellido:
            raise ValueError("Nombre y apellido no pueden estar vacios")
        if any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
            raise ValueError("Nombre y Apellido no pueden contener numeros")
        self.nombre = nombre.title()
        self.apellido = apellido.title()

    def describir(self):
        return(f"Esta es una Persona que se llama {self.nombre} y se apellida {self.apellido}")
    
class Empleado(Persona):
    def __init__(self, nombre, apellido, clave):
        super().__init__(nombre, apellido)
        if not isinstance(clave, int) or clave <= 0:
            raise ValueError("La clave tiene que ser un numero entero positivo y mayor a 0")
        self.clave = clave

    def describir(self):
        return(f"Este es un Empleado que se llama {self.nombre}, que se apellida {self.apellido} y tiene la clave {self.clave}")

class Paciente(Persona):
    def __init__(self, nombre, apellido, clave, genero):
        super().__init__(nombre, apellido)
        if not isinstance(clave, int) or clave <= 0:
            raise ValueError("La clave tiene que ser un numero entero positivo y mayor a 0")
        if genero.lower() not in ["hombre" or "mujer"]:
            raise ValueError("El genero debe ser Hombre o Mujer")
        self.clave = clave
        self.genero = genero

    def describir(self):
        return(f"Este es un Paciente que se llama {self.nombre}, que se apellida {self.apellido}, que tiene la clave {self.clave} y su genero es {self.genero}")

#Ejemplos:
     
persona1 = Persona("Sergio", "Canales")
print(persona1.describir())

empleado1 = Empleado("Sergio", "Canales", 10)
print(empleado1.describir())

paciente1 = Paciente("Sergio", "Canales", 10, "Hombre")
print(paciente1.describir())
