from app.reservas import (
    validar_reserva,
    calcular_costo_reserva
)

def test_reserva_valida():

    resultado = validar_reserva(
        "Carlos Torres",
        4
    )

    assert resultado[0] is True


def test_nombre_vacio():

    resultado = validar_reserva(
        "",
        4
    )

    assert resultado[0] is False


def test_personas_invalidas():

    resultado = validar_reserva(
        "Carlos",
        0
    )

    assert resultado[0] is False


def test_limite_personas():

    resultado = validar_reserva(
        "Carlos",
        15
    )

    assert resultado[0] is False


def test_calculo_costo():

    total = calcular_costo_reserva(4)

    assert total == 100000