# ENUNCIADO
# Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro.
# A partir del día 11 de retraso, cada día cuesta $10.
# La multa máxima es de $200.
# Se necesita mostrar la multa a partir de los días de retraso.


# PROBLEMA
# Calcular la multa por retraso en la devolución de un libro
# según el número de días de retraso.


# ENTRADAS
# dias : int, días de retraso, rango válido de 0 en adelante.


# SALIDAS
# multa : float, pesos mexicanos, mostrada con dos decimales.


# REGLAS Y SUPUESTOS
# - Los días de retraso se manejan únicamente con números enteros.
# - El mínimo válido es 0 días.
# - Si no hay días de retraso, la multa es de $0.
# - Los primeros 10 días de retraso cuestan $5 por día.
# - A partir del día 11, cada día adicional cuesta $10.
# - La multa máxima es de $200.
# - La multa se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce un número válido de días.


# ALGORITMO
# 1. Leer los días de retraso.
# 2. Si dias <= 10:
#       multa = dias * 5
# 3. En caso contrario:
#       multa = (10 * 5) + ((dias - 10) * 10)
# 4. Si multa > 200:
#       multa = 200
# 5. Mostrar los días de retraso y la multa.


# CASOS DE PRUEBA
# 0 días  -> $0.00
# 10 días -> $50.00
# 11 días -> $60.00
# 25 días -> $200.00
# 40 días -> $200.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - La única biblioteca permitida es tabulate.
# - No agregues clases ni funciones auxiliares.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerDias() -> int :
#   Solicita los días de retraso y los devuelve como entero.
#
# calcularMulta(dias) -> float :
#   Calcula y devuelve la multa según los días de retraso
#   y el límite máximo permitido.
#
# mostrarMulta(dias, multa) -> None :
#   Muestra los días de retraso y la multa usando tabulate.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate


def leerDias():
    dias = int(input("Ingrese los días de retraso: "))
    return dias


def calcularMulta(dias):
    if dias <= 10:
        multa = dias * 5
    else:
        multa = (10 * 5) + ((dias - 10) * 10)

    if multa > 200:
        multa = 200

    return multa


def mostrarMulta(dias, multa):
    filas = [
        ["Días de retraso", dias],
        ["Multa", f"${multa:.2f}"]
    ]

    print(tabulate(filas, headers=["Concepto", "Valor"]))