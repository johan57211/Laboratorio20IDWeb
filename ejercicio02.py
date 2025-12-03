ingreso_mensual = float(input("Ingreso mensual: "))
ingreso_anual = ingreso_mensual * 14   

print("\nIngreso anual:", ingreso_anual)

tramos = [
    (0, 20000, 0.00),
    (20000, 50000, 0.10),
    (50000, 100000, 0.20),
    (100000, float("inf"), 0.30)
]

impuesto_total = 0
print("\n--- IMPUESTO POR TRAMOS ---")

for inicio, fin, tasa in tramos:
    if ingreso_anual > inicio:
        monto_tramo = min(ingreso_anual, fin) - inicio
        impuesto = monto_tramo * tasa
        impuesto_total += impuesto
        print(f"Tramo {inicio}-{fin}: {impuesto}")

print("\nTotal impuestos:", impuesto_total)
tasa_efectiva = (impuesto_total / ingreso_anual) * 100
print("Tasa efectiva real: ", tasa_efectiva, "%")
