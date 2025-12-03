salario_base = float(input("Salario base: "))
horas_extras = float(input("Horas extras: "))
pago_hora_extra = float(input("Pago por hora extra: "))
bono = float(input("Bono: "))
afp = float(input("AFP (%): "))
salud = float(input("Salud (%): "))

salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono
descuento_afp = salario_base * (afp / 100)
descuento_salud = salario_base * (salud / 100)
descuentos_totales = descuento_afp + descuento_salud
salario_neto = salario_bruto - descuentos_totales

print("\n--- RESULTADOS ---")
print("Salario bruto:", salario_bruto)
print("Descuentos totales:", descuentos_totales)
print("Salario neto:", salario_neto)
