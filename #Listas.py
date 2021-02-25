#Listas
Nombres = ['']
Nombres.remove('')
#Definir las funciones
def Menu():
    print("1.Insertar un nuevo dato a lista.")
    print("2.Eliminar un Dato de la lista.")
    print("Elija una opcion: ")
    
def PedirDatos():
    for n in range(1,6):
       palabra = str(input(f'Ingrese la palabra #[{n}]: ')) 
       Nombres.append(palabra)
       
def MostrarDatos():
    print(Nombres)
      
def EliminarDatos():
    palabra = str(input('¿Qué nombre desea eliminar? '))
    Nombres.remove(palabra)
    print('El nombre ha sido elimado')
    MostrarDatos()
    
def Insertar():
    palabra = str(input('¿Qué palabra desea agregar? '))
    Nombres.append(palabra)
    
print("\t\tProblema: Listado de Palabras")
print('--'*30)

print("Inserte 5 Nombres: ")
PedirDatos()
print('')
MostrarDatos()

print("\nElija una opcion: ")
Menu()      
opcion = int(input())
if (opcion == 1):
    print(Insertar())
    MostrarDatos()
        
elif(opcion == 2):
    print(EliminarDatos())
   
else:print('¡Opcion Invalida! Feliz Día')  

print('¡¡Gracias por usar el sistema de Lista!!')