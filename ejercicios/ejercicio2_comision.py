# ENUNCIADO
# Un vendedor gana 5% de comisión sobre sus ventas del mes.
# Si vende $10,000 o más, la comisión es de 8%.
# Si vende más de $50,000, recibe además un bono de $1,000.
# Se necesita mostrar la comisión, el bono y el total a pagar.


# PROBLEMA
# Calcular la comisión, el bono y el total a pagar
# a un vendedor según sus ventas mensuales.


# ENTRADAS
# ventas : float, pesos mexicanos, rango válido de 0 en adelante.


# SALIDAS
# comision : float, pesos mexicanos, mostrada con dos decimales.
# bono : float, pesos mexicanos, mostrado con dos decimales.
# total : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - Las ventas pueden contener decimales.
# - El valor mínimo válido de ventas es $0.
# - Si las ventas son menores a $10,000, la comisión es de 5%.
# - Si las ventas son de $10,000 o más, la comisión es de 8%.
# - El 8% reemplaza al 5%; los porcentajes no se acumulan.
# - Si las ventas son mayores a $50,000, se agrega un bono de $1,000.
# - Si las ventas son de $50,000 o menos, el bono es de $0.
# - El total a pagar es la comisión más el bono.
# - Los importes se muestran con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce un valor válido de ventas.


# ALGORITMO
# 1. Leer las ventas mensuales.
# 2. Si ventas >= 10000:
#       comision = ventas * 0.08
# 3. En caso contrario:
#       comision = ventas * 0.05
# 4. Si ventas > 50000:
#       bono = 1000
# 5. En caso contrario:
#       bono = 0
# 6. Calcular:
#       total = comision + bono
# 7. Mostrar comisión, bono y total.


# CASOS DE PRUEBA
# $5000  -> comisión $250.00, bono $0.00, total $250.00
# $10000 -> comisión $800.00, bono $0.00, total $800.00
# $50000 -> comisión $4000.00, bono $0.00, total $4000.00
# $50001 -> comisión $4000.08, bono $1000.00, total $5000.08


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - La única biblioteca permitida es tabulate.
# - No agregues clases ni funciones auxiliares.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerVentas() -> float :
#   Solicita las ventas mensuales y las devuelve como número decimal.
#
# calcularComision(ventas) -> float :
#   Calcula y devuelve la comisión correspondiente a las ventas.
#
# calcularBono(ventas) -> float :
#   Calcula y devuelve el bono correspondiente a las ventas.
#
# mostrarPago(comision, bono, total) -> None :
#   Muestra la comisión, el bono y el total usando tabulate.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate


def leerVentas():
    ventas = float(input("Ingrese las ventas del mes: "))
    return ventas


def calcularComision(ventas):
    if ventas >= 10000:
        comision = ventas * 0.08
    else:
        comision = ventas * 0.05

    return comision


def calcularBono(ventas):
    if ventas > 50000:
        bono = 1000
    else:
        bono = 0

    return bono


def mostrarPago(comision, bono, total):
    filas = [
        ["Comisión", f"${comision:.2f}"],
        ["Bono", f"${bono:.2f}"],
        ["Total", f"${total:.2f}"]
    ]

    print(tabulate(filas, headers=["Concepto", "Valor"]))