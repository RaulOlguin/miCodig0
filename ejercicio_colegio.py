""" 
un colegio que por tercera vez nos va a llamar
este colegio en la tercera actualizacion requiere un menu donde la opcion es buscar alumnos utilizando diccionario
se crea un diccionario manual de 5 alumnos

opcion 1 busca por nombre en diccionario manual
opcion 2 ingreso de notas dinamico en una lista notas por alumno (los alumnos tienen distintas notas)

"""
import os
os.system('color 71')#cambiando color de la terminal

# Diccionario con alumnos
alumnos = {
        'NEO':[],
        'MORPHEO':[],
        'SWITCH':[],
        'TRINITY':[],
        'SYPHER':[]
        }

#----------------------------------------------------------------------------------------------
# funcion que revisa si existe un alumno en el diccionario
def existe_alumno(nombre=""):
    if nombre.upper() in alumnos.keys():
        return True
    else:
        return False


#----------------------------------------------------------------------------------------------
# funcion que busca un alumno y muestra sus notas

def buscar_nombre(nombre=""):
    os.system('cls')# limpiando la pantalla
    
    if existe_alumno(nombre):
        tieneNotas = len(alumnos[nombre.upper()]) 
       
        if  tieneNotas == 0 :
            print(f"\n\tEl Alumno {nombre.upper()} No registra notas\n\n")
        else:
            print(f"\n\tEl Alumno {nombre.upper()} registra {tieneNotas} notas:\n\t{alumnos[nombre.upper()]}")
    else:
        print("\n\tEl Alumno Solicitado no Esta en Nuestros Registros\n\n")

    input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")    


#----------------------------------------------------------------------------------------------
# funcion que ingresa notas para un alumno

def ingresa_notas(nombre = "", cantNotas=1):
   
    os.system('cls')# limpiando pantalla

    contadorNota = 0
    print("\n\n")

    if not existe_alumno(nombre):
        print("\t*** Alumno no existe ***\n\n")
    else:

        while contadorNota < cantNotas:
       
            try:
                nota = float(input(f"\tIngrese {(len(alumnos[nombre.upper()]) + 1)}° nota del alumno {nombre.upper()} >> "))
            except:
                print("\n\t*** Nota no valida ***\n")
                nota = -1
           
            if 0 <= nota <=7:
                alumnos[nombre.upper()].append(nota)
                contadorNota += 1
            else:
                print("\tLa nota tiene que estar entre 0 y 7\n\n")

    input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")

#----------------------------------------------------------------------------------------------
# menu inicio

while True:
    os.system('cls')

    print("\n")
    print("\t\t█████████████████████████████████████████████████████████░░")
    print("\t\t██                                                     ██░░")
    print("\t\t██              Bien Venido a Colegio                  ██░░")
    print("\t\t██                                                     ██░░")
    print("\t\t██      opcion 1: Buscar Alumno                        ██░░")
    print("\t\t██      opcion 2: Ingresar Notas                       ██░░")
    print("\t\t██      opcion 3: Salir                                ██░░")
    print("\t\t██                                                     ██░░")
    print("\t\t█████████████████████████████████████████████████████████░░")
    print("\t\t░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    opcion = int(input("\t\t\t\t\t[_]\b\b"))

    if opcion == 3:
        break
    elif opcion == 1:
        
        try:
            nombre = input("\n\t¿Cual es el nombre del alumno? >> ")
        except:
            print("\tIngrese un nombre valido\n\n")
            input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")
        else:    
            buscar_nombre(nombre)


    elif opcion == 2:

        try:
            cantNotas = 0
            nombre = input("\n\t¿Cual es el nombre del alumno? >> ")

            while cantNotas < 1:
                cantNotas= int(input("\t¿Cuantas notas va a ingresar? >> "))
                if cantNotas < 1:
                    print("\tLa Cantidad minima de notas tiene que ser 1\n")
        
        except(ValueError, TypeError):
            print("\tHay un error con el tipo de datos que ha intentado ingresar")
            input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")
        except:
            print("\t se ha producido un error")
            input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")
        else:
            ingresa_notas(nombre, cantNotas)

    else:
        print("\n\n\tLas opciones disponibles son 1, 2 y 3\n\n")
        input("\n\t>> PRESIONE ENTER PARA CONTINUAR <<")

os.system('color 07')
os.system('cls')