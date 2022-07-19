# este archivo se utiliza para ejecutar/necesitamos decirle al archivo que queremos utilizar el archivo de persona
from Persona import Persona# de mi archicvo que se llama persona quiero que importes mi clase persona 
#una instancia es cuando ya haces una declaracion de esa clase persona , elena=persona, aqui elena ya es una instancia de persona, una instancia es algo a los que ya le pusimos datos a lo que ya esta incializado con una clase persona y ya tiene informacion y eso lo hace una instancia, por mas variables que hagamos del tipo persona, todas van a tener el mismo nombre apellido y edad , si pongo a juana a a tnener el mismo nombre de elena 
elena = Persona("Elena", "De Troya", 30) #Instancia de Persona

juana = Persona("Juana", "De Arco", 33)

print(elena.nombre)
print(juana.nombre)

juana.cumpleaños() # 33
print(juana.edad) #34

elena.codificar(101)
print(elena.lineas_codigo)

elena.codificar(40)
juana.codificar(20)
print(elena.lineas_codigo)
print(juana.lineas_codigo)
print(Persona.total_lineas_codigo)

Persona.cambiar_pais("Mexico")

if Persona.mayoria_edad(19):
    print("wow, si eres mayor de edad")