import pytest
from src.main import determinar_mail, generar_lista_dominios_ordenada_alfa_sin_repetir

@pytest.mark.parametrize("mail, esperado", [
    ("mg@hotmail.com.ar", True),
    ("fghj@gmail.com", False),
    ("f@ghj@hotmail.com.ar@", False),
    ("fg@hj@gmail.com", False),
    ("fghj@outlookmail.ar", False),
    ("fgh#j@gmail.com.ar", False),
    ("ioap@gmail.com.ar", True),
    ("malsg@hotmail.com.ar", True),
    ("pas@outlook.com.ar", True)

])

def test_determinar_mail_pass(mail, esperado):
    assert determinar_mail(mail) == esperado

def test_dominios(monkeypatch):
    inputs = iter(["mg@hotmail.com.ar", "fghj@gmail.com", "f@ghj@hotmail.com.ar@", "fg@hj@gmail.com", "fghj@outlookmail.ar"
    "fgh#j@gmail.com.ar","ioap@gmail.com.ar","malsg@hotmail.com.ar","pas@outlook.com.ar",""])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    resultado = generar_lista_dominios_ordenada_alfa_sin_repetir()
    assert resultado == ["gmail","hotmail","outlook"]