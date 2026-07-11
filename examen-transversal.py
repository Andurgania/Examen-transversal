def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")
def leer_opcion():
    """No recibe parámetros. Solicita una opción, valida que sea un entero
    dentro del rango [1,6] y la retorna. Maneja errores de tipo con try/except."""
    while True:
        entrada = input("Ingrese opción: ")
        try:
            opcion = int(entrada)
        except ValueError:
            print("Debe seleccionar una opción válida")
            continue 
        if 1 <= opcion <= 6:
            return opcion
        else:
            print("Debe seleccionar una opción válida")
def cupos_tipo(tipo, planes, inscripciones):
    """Recibe el tipo de plan, no retorna nada, muestra el total de cupos
    disponibles para ese tipo directamente por pantalla."""
    tipo = tipo.lower()
    total = 0
    for codigo in planes:
        if planes[codigo][1].lower() == tipo:
            total += inscripciones[codigo][1]
    print(f"El total de cupos disponibles es: {total}")
def busqueda_precio(p_min, p_max, planes, inscripciones):
    """Recibe precio mínimo y máximo, no retorna nada, muestra directamente
    por pantalla los planes encontrados, ordenados alfabéticamente por nombre."""
    resultados = []
    for codigo in inscripciones:
        precio = inscripciones[codigo][0]
        cupos = inscripciones[codigo][1]
        if p_min <= precio <= p_max and cupos != 0:
            nombre = planes[codigo][0]
            resultados.append(f"{nombre}-{codigo}")
    resultados.sort()
    if resultados:
        print(f"Los planes encontrados son: {resultados}")
    else:
        print("No hay planes en ese rango de precios.")
def buscar_codigo(codigo, planes):
    """Recorre el diccionario y retorna True si el código existe, False si no."""
    return codigo in planes
def actualizar_precio(codigo, nuevo_precio, planes, inscripciones):
    """Verifica existencia (reutilizando buscar_codigo), actualiza el precio
    y retorna True, o retorna False si el código no existe."""
    if buscar_codigo(codigo, planes):
        inscripciones[codigo][0] = nuevo_precio
        return True
    return False
def validar_codigo(codigo, planes):
    if codigo.strip() == "":
        return False
    return not buscar_codigo(codigo, planes)
def validar_nombre(nombre):
    return nombre.strip() != ""
def validar_tipo(tipo):
    return tipo.lower() in ("mensual", "trimestral", "anual")
def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
    except ValueError:
        return False
    return duracion > 0
def validar_respuesta_sn(valor):
    return valor.lower() in ("s", "n")
def validar_horario(horario):
    return horario.strip() != ""
def validar_precio(precio_str):
    try:
        precio = int(precio_str)
    except ValueError:
        return False
    return precio > 0
def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
    except ValueError:
        return False
    return cupos >= 0 
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina,
                  incluye_clases, horario, precio, cupos, planes, inscripciones):
    """Agrega el registro en ambos diccionarios y retorna True.
    Si el código ya existía, retorna False."""
    if buscar_codigo(codigo, planes):
        return False
    planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]
    return True
def eliminar_plan(codigo, planes, inscripciones):
    """Verifica existencia (reutilizando buscar_codigo), elimina el registro
    en ambos diccionarios y retorna True, o retorna False si no existe."""
    if buscar_codigo(codigo, planes):
        del planes[codigo]
        del inscripciones[codigo]
        return True
    return False
def main():
    planes = {
        "F001": ["Plan Básico", "mensual", 1, False, False, "libre"],
        "F002": ["Plan Full", "mensual", 1, True, True, "libre"],
        "F003": ["Plan Estudiante", "trimestral", 3, False, True, "tarde"],
        "F004": ["Plan Senior", "trimestral", 3, True, False, "mañana"],
        "F005": ["Plan Anual Pro", "anual", 12, True, True, "libre"],
        "F006": ["Plan Nocturno", "mensual", 1, False, True, "noche"],
    }
    inscripciones = {
        "F001": [14990, 30],
        "F002": [22990, 10],
        "F003": [39990, 0],
        "F004": [35990, 6],
        "F005": [159990, 2],
        "F006": [18990, 15],
    }
    while True:
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == 1:
            tipo = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo, planes, inscripciones)
        elif opcion == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                except ValueError:
                    print("Debe ingresar valores enteros")
                    continue
                if p_min < 0 or p_max < 0 or p_min > p_max:
                    print("Debe ingresar valores enteros")
                    continue
                break
            busqueda_precio(p_min, p_max, planes, inscripciones)
        elif opcion == 3:
            repetir = "s"
            while repetir == "s":
                codigo = input("Ingrese código del plan: ").strip().upper()
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio <= 0:
                        raise ValueError
                except ValueError:
                    print("Debe ingresar un precio entero positivo")
                else:
                    if actualizar_precio(codigo, nuevo_precio, planes, inscripciones):
                        print("Precio actualizado")
                    else:
                        print("El código no existe") 
                repetir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
        elif opcion == 4:
            codigo = input("Ingrese código del plan: ").strip().upper()
            nombre = input("Ingrese nombre del plan: ")
            tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
            duracion_str = input("Ingrese duración (meses): ")
            acceso_str = input("¿Incluye acceso a piscina? (s/n): ")
            clases_str = input("¿Incluye clases grupales? (s/n): ")
            horario = input("Ingrese horario: ")
            precio_str = input("Ingrese precio: ")
            cupos_str = input("Ingrese cupos: ") 
            if not validar_codigo(codigo, planes):
                print("Código inválido o ya existente")
            elif not validar_nombre(nombre):
                print("Nombre inválido")
            elif not validar_tipo(tipo):
                print("Tipo inválido")
            elif not validar_duracion(duracion_str):
                print("Duración inválida")
            elif not validar_respuesta_sn(acceso_str):
                print("Respuesta de acceso a piscina inválida")
            elif not validar_respuesta_sn(clases_str):
                print("Respuesta de clases grupales inválida")
            elif not validar_horario(horario):
                print("Horario inválido")
            elif not validar_precio(precio_str):
                print("Precio inválido")
            elif not validar_cupos(cupos_str):
                print("Cupos inválido")
            else:
                duracion = int(duracion_str)
                acceso_piscina = acceso_str.strip().lower() == "s"
                incluye_clases = clases_str.strip().lower() == "s"
                precio = int(precio_str)
                cupos = int(cupos_str) 
                if agregar_plan(codigo, nombre, tipo.lower(), duracion, acceso_piscina,
                                 incluye_clases, horario, precio, cupos, planes, inscripciones):
                    print("Plan agregado")
                else:
                    print("El código ya existe")
        elif opcion == 5:
            codigo = input("Ingrese código del plan a eliminar: ").strip().upper()
            if eliminar_plan(codigo, planes, inscripciones):
                print("Plan eliminado")
            else:
                print("El código no existe")
        elif opcion == 6:
            print("Programa finalizado.")
            break
    main()