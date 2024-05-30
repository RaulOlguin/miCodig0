"""
se requiere desarrollar un ia que permita hacer multiple operaciones las operaciones que puede hacer
estan almacenadas en un diccionario (pseudo inteligencia)
este diccionario va a contar con una llave y un valor, la llave va hacer referencia a la operacion
y la operacion va a estar en el cuerpo

tiene que haber un mantenedor, opcion 1 insertar operacion, opecion 2 eliminar
opecion 3 listar operacion

una cuarta opcion listar operaciones, y esa va a mostrar los valores para acceder.
cual operacion desea operar

hay que subirlo a github

"""

operaciones = {}

def existe(clave):
    if clave in operaciones:
        return True
    else:
        return False

def insertar(clave, texto):
    if existe(clave):
        print("\n\tOperacion ya existe")
    else:
        operaciones.update({clave : texto})
        

def eliminar(clave):
    if existe(clave):
        del(operaciones[clave])
    else:
        print("\n\tOperacion no existe")


def mostrar(clave, operacion=None):
    if existe(clave):
        if operacion == None:
            print(f"\t{clave} =  { operaciones[clave] }")
        else:
            print(f"\n{clave}")
    else:
        print("\n\tOperacion no existe")


def listar_operaciones():
    print("\n\n")
    for clave, operacion in operaciones.items():
        mostrar(clave, operacion)

while True:

    print("\n\n\tOpcion 1: insertar operacion")
    print("\tOpcion 2: eliminar operacion")
    print("\tOpcion 3: listar operacion")
    print("\tOpcion 4: ejecutar operacion")
    print("\tOpcion 5: Salir")

    print(operaciones)

    opcion = int(input("\n\tIngrese su opcion : "))


    if opcion == 5:
        break
    
    elif opcion == 1:
        print("\n\n\tINSERTAR OPERACION\n\n")
        clave = input("\tIngrese Nombre de la Operacion : ")
        operacion = input("\tIngrese Operacion : ")
        insertar(clave, operacion)
    
    elif opcion == 2:
        print("\n\n\tELIMINAR OPERACION")
        clave = input("\n\n\tIngrese Nombre de la Operacion : ")
        eliminar(clave)

    elif opcion == 3:
        print("\n\n\tLISTAR OPERACION\n\n")
        listar_operaciones()
    
    elif opcion == 4:
        print("\n\n\tEJECUTAR OPERACION")
        clave = input("\n\n\tIngrese Nombre de la Operacion : ")
        mostrar(clave)

    