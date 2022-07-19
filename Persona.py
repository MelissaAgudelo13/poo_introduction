#clase va a tener los atributos relacionados a la persona#a traves de init inicializamos nuestra instancia
class Persona:
    #variables o atributos globales que pertenecen a a la clase persona 
    pais = "Colombia"
    total_lineas_codigo=0

    #A traves de init INICIALIZAMOS nuestra instancia./cuando hacemos la division entre clases lo mas conveniente es que creemos otro archivo para ejecutar el codigo 
    
    '''def __init__(self, nombre, apellido, edad): SELF nos incluye toda la información correspondiente al objeto individual o instancia
        nombre = "Elena", apellido = "De Troya", edad = 30 ↓ ponemos atributos que queremos para miperson
        dentro de la funcion quiero recibir datos en este ejemplo (nombre, apellido ,edad) entonces cuando este inicializando la persona le tengo que mandar el nombre, apellido y la edad en el main
        self.nombre = "Elena" con estos atributos le estamos asignando directamente a nuestra persona acualquier persona q vayamos a dar de alta estamos asignando estos valores
        self.apellido = "De troya"
        self.edad = 30
        self.lineas_codigo = 0'''

    def __init__(self, nombre, apellido, edad): 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.lineas_codigo = 0 #cuando inicializamos una persona la empezamos en 0 
# crear acciones como cumplir años
    def cumpleaños(self): #va recibir el self va a ser de una instancia en especifico
        self.edad +=1 # a la edad de la persona le quiero aumentar un 1
        if Persona.mayoria_edad(self.edad):
            print("Wuju, eres mayor de edad")

    def tomar_cerveza(self):
        if Persona.mayoria_edad(self.edad):
            print("Aqui esta tu cerveza")
        else:
            print("Los siento, no puedes tomar")

    def codificar(self,cantidad_lineas):
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo+=cantidad_lineas
    # con classmethod podemos modificar por medio de una funcion que pueda pertener a toda la clase 
    @classmethod # va a ser una funcion correspondiente al modificar algo pertenenciente a toda la clase
    def cambiar_pais(cls,nuevo_pais):#como nuevo pais recibo a mexico
        cls.pais = nuevo_pais

    @staticmethod
    def mayoria_edad(edad):
        if edad > 18:
            return True
        else:
            return False


