def validar_reserva(nombre, cantidad_personas):

    if nombre.strip() == "":
        return False, "El nombre es obligatorio"

    if cantidad_personas <= 0:
        return False, "La cantidad de personas debe ser mayor a cero"

    if cantidad_personas > 12:
        return False, "La cantidad máxima permitida es 12 personas"

    return True, "Reserva válida"


def calcular_costo_reserva(cantidad_personas):

    costo_por_persona = 25000

    return cantidad_personas * costo_por_persona