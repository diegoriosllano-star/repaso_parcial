# ENUNCIADO
# Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido.
# Los viajes de más de 20 km tienen 10% de descuento.
# Se necesita mostrar el importe del viaje.


# PROBLEMA
# Calcular el importe de un viaje en taxi según
# los kilómetros recorridos.


# ENTRADAS
# kilometros : float, kilómetros, rango válido de 0 en adelante.


# SALIDAS
# importe : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - Los kilómetros pueden contener decimales.
# - El mínimo válido es 0 km.
# - El banderazo cuesta $35.
# - Cada kilómetro recorrido cuesta $9.
# - Si el viaje es de 20 km o menos, no se aplica descuento.
# - Si el viaje es mayor a 20 km, se aplica 10% de descuento
#   sobre el importe total del viaje.
# - El importe final se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce una distancia válida.


# ALGORITMO
# 1. Leer los kilómetros recorridos.
# 2. Calcular el importe inicial:
#       importe = 35 + (kilometros * 9)
# 3. Si kilometros > 20:
#       descuento = importe * 0.10
#       importe = importe - descuento
# 4. Mostrar los kilómetros recorridos y el importe final.


# CASOS DE PRUEBA
# 5 km  -> $80.00
# 20 km -> $215.00
# 21 km -> $201.60
# 30 km -> $274.50


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - La única biblioteca permitida es tabulate.
# - No agregues clases ni funciones auxiliares.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerKilometros() -> float :
#   Solicita los kilómetros recorridos y los devuelve como número decimal.
#
# calcularImporte(kilometros) -> float :
#   Calcula y devuelve el importe final del viaje.
#
# mostrarImporte(kilometros, importe) -> None :
#   Muestra los kilómetros recorridos y el importe final usando tabulate.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate


def leerKilometros():
    kilometros = float(input("Ingrese los kilómetros recorridos: "))
    return kilometros


def calcularImporte(kilometros):
    importe = 35 + (kilometros * 9)

    if kilometros > 20:
        descuento = importe * 0.10
        importe = importe - descuento

    return importe


def mostrarImporte(kilometros, importe):
    filas = [
        ["Kilómetros", kilometros],
        ["Importe", f"${importe:.2f}"]
    ]

    print(tabulate(filas, headers=["Concepto", "Valor"]))