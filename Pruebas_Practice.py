#Ejercicio Calculadora Basica
print('Calculadora')
print('-' * 10)
# Declarar las variables
numero1 = 0
numero2 = 0
resultado = 0
# Definir los metodos
def menu():
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicacion')
    print('4.Division')
    print('5.Salir')
    print('Elija un opcion: ')

def IngresarDatos():
    numero1 = int(input('Ingrese el primer numero: '))
    numero2 = int(input('Ingrese el segundo numero: '))

def Suma():
    print(IngresarDatos())
    print("La suma es: ",numero1 + numero2)

def Resta():
    print(IngresarDatos())
    print("La resta es: ", numero1 - numero2)

def Multiplicacion():
    print(IngresarDatos())
    print("La multiplicacion es: ", numero1 * numero2)
    
def Division():
    print(IngresarDatos())
    if numero2 == 0:
        print("¡El dividendo no puede ser cero!")
    else:
        resultado = numero1 / numero2
        print("La division es: ", resultado)
        
while True:
    menu()
    seleccion = int(input())
    if seleccion == 1:
        print(Suma())  
    elif seleccion == 2:
        print(Resta())
    elif seleccion == 3:
        print(Multiplicacion())
    elif seleccion == 4:
        print(Division())
    elif seleccion == 5:
        print('-------¡Gracias por usa mi calculadora!-------')
        break
        
    else:
        print('¡Elija una opcion valida!')  
