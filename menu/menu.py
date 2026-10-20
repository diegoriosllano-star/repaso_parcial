from ejercicios import ejercicio1_taxi as ej1


def ejecutarEjercicio1():
    kilometros = ej1.leerKilometros()
    importe = ej1.calcularImporte(kilometros)
    ej1.mostrarImporte(kilometros, importe)


def ejecutarEjercicio2():
    print("Ejercicio 2 pendiente.")


def ejecutarEjercicio3():
    print("Ejercicio 3 pendiente.")


def mostrarMenu():
    print()
    print("REPASO PARA EL EXAMEN PARCIAL")
    print("1. Viaje en taxi")
    print("2. Comisión de ventas")
    print("3. Multa de biblioteca")
    print("0. Salir")


def menus():
    opcion = ""

    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ejecutarEjercicio1()
        elif opcion == "2":
            ejecutarEjercicio2()
        elif opcion == "3":
            ejecutarEjercicio3()
        elif opcion != "0":
            print("Opción no válida.")