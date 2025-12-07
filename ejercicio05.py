estudiantes = []

def agregar_estudiante():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    promedio = float(input("Promedio: "))

    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    for i, est in enumerate(estudiantes, start=1):
        print(f"{i}. Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']}")
    print()

def mejor_promedio():
    if not estudiantes:
        print("No hay estudiantes.\n")
        return

    mejor = max(estudiantes, key=lambda e: e["promedio"])
    print("Estudiante con mejor promedio:")
    print(f"Nombre: {mejor['nombre']}, Edad: {mejor['edad']}, Promedio: {mejor['promedio']}\n")

def buscar_por_nombre():
    nombre_buscar = input("Nombre a buscar: ")
    encontrados = []

    for est in estudiantes:
        if est["nombre"].lower() == nombre_buscar.lower():
            encontrados.append(est)

    if not encontrados:
        print("No se encontraron estudiantes con ese nombre.\n")
    else:
        print("Estudiantes encontrados:")
        for est in encontrados:
            print(f"Nombre: {est['nombre']}, Edad: {est['edad']}, Promedio: {est['promedio']}")
        print()

def eliminar_por_nombre():
    nombre_eliminar = input("Nombre a eliminar: ")
    eliminados = 0

    for est in estudiantes[:]:
        if est["nombre"].lower() == nombre_eliminar.lower():
            estudiantes.remove(est)
            eliminados += 1

    if eliminados == 0:
        print("No se encontró ningún estudiante con ese nombre.\n")
    else:
        print(f"Se eliminaron {eliminados} estudiante(s) con ese nombre.\n")

def mostrar_menu():
    print("=== MENÚ ESTUDIANTES ===")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        mejor_promedio()
    elif opcion == "4":
        buscar_por_nombre()
    elif opcion == "5":
        eliminar_por_nombre()
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.\n")
