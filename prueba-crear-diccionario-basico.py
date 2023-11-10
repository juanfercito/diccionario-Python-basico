print('|**** Crear colecciones de letras y numeros ****|\n')

print('  Escriba numeros superiores a 1 para iniciar programa, \n  caso contrario ingrese 1 para salir: \n')
# Este es un ejercicio facil para demostrar una forma de crear colecciones
# de datos con diccionarios, sin que se repitan los valores de los mismos
# a medida que crece la coleccion:
coll = {}
while True:

    # En este punto se escriben los valores que requiere la pantalla y se
    # efectua un recorrido de los datos para validar su existencia:
    num = int(input("escriba un numero: "))
    num2 = int(input("escriba un numero: "))
    num3 = int(input("escriba un numero: "))

    if num > 1:

        letr = input("escriba cualquier letra: ")

        for i in range(num):
            i += 1
            coll[letr] = i

        if num2 > 1:

            letr2 = input("escriba cualquier letra: ")

            for i in range(num2):
                i += 1
                coll[letr2] = i

        if num3 > 1:

            letr3 = input("escriba cualquier letra: ")

            for i in range(num3):
                i += 1
                coll[letr3] = i

        print(coll)

    # para efectos practicos, solo para demostracion, usaremos una condicion
    # else para detener el programa y evitar la ejecucion continua:
    else:
        print(input("presione ENTER para salir: "))

        exit()
