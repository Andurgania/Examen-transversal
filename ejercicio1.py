def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_copias(valor):
    try:
        return int(valor) >= 0
    except ValueError:
        return False

def validar_prestamo(valor):
    try:
        return int(valor) > 0
    except ValueError:
        return False

def mostrar_menu():
    """Muestra las opciones del menú principal."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion in ("1", "2", "3", "4", "5", "6"):
            return int(opcion)
        print("Opción no válida. Ingrese un número del 1 al 6.")

def agregar_libro(biblioteca):
    print("\n--- Agregar libro ---")
    titulo = input("Título: ")
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío o ser solo espacios.")
        return
    copias = input("Cantidad de copias: ")
    if not validar_copias(copias):
        print("Error: las copias deben ser un número entero mayor o igual a cero.")
        return
    prestamo = input("Período de préstamo (días): ")
    if not validar_prestamo(prestamo):
        print("Error: el período de préstamo debe ser un número entero mayor que cero.")
        return
    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias),
        "prestamo": int(prestamo),
        "disponible": False,
    }
    biblioteca.append(libro)
    print(f"Libro '{libro['titulo']}' agregado correctamente.")

def buscar_libro(biblioteca, titulo):
    for i, libro in enumerate(biblioteca):
        if libro["titulo"] == titulo:
            return i
    return -1

def eliminar_libro(biblioteca):
    print("\n--- Eliminar libro ---")
    titulo = input("Título del libro a eliminar: ").strip()
    posicion = buscar_libro(biblioteca, titulo)
    if posicion == -1:
        print(f"El libro '{titulo}' no se encuentra registrado.")
    else:
        biblioteca.pop(posicion)
        print(f"El libro '{titulo}' fue eliminado correctamente.")

def actualizar_disponibilidad(biblioteca):
    for libro in biblioteca:
        libro["disponible"] = libro["copias"] >= 1

def mostrar_libros(biblioteca):
    actualizar_disponibilidad(biblioteca)
    print("\n=== LISTA DE LIBROS ===")
    if not biblioteca:
        print("No hay libros registrados.")
        return
    for libro in biblioteca:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("*" * 45)

def final():
    biblioteca = []
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            agregar_libro(biblioteca)
        elif opcion == 2:
            print("\n--- Buscar libro ---")
            titulo = input("Título a buscar: ").strip()
            posicion = buscar_libro(biblioteca, titulo)
            if posicion == -1:
                print(f"El libro '{titulo}' no se encuentra registrado.")
            else:
                libro = biblioteca[posicion]
                estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print(f"\nLibro encontrado en la posición {posicion}:")
                print(f"  Título   : {libro['titulo']}")
                print(f"  Copias   : {libro['copias']}")
                print(f"  Préstamo : {libro['prestamo']} días")
                print(f"  Estado   : {estado}")
        elif opcion == 3:
            eliminar_libro(biblioteca)
        elif opcion == 4:
            actualizar_disponibilidad(biblioteca)
            print("Disponibilidad actualizada correctamente.")
        elif opcion == 5:
            mostrar_libros(biblioteca)
        elif opcion == 6:
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break
    
final()