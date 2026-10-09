from main import calculadora


def ejecutar_calculadora(monkeypatch, respuestas):
    entradas = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda _="": next(entradas))
    calculadora()


def test_suma(monkeypatch, capsys):
    ejecutar_calculadora(monkeypatch, ["1", "2", "3", "8"])

    assert "Resultado: 5.0" in capsys.readouterr().out


def test_division_entre_cero(monkeypatch, capsys):
    ejecutar_calculadora(monkeypatch, ["4", "10", "0", "8"])

    salida = capsys.readouterr().out
    assert "No se puede dividir entre cero" in salida
    assert "Resultado:" not in salida


def test_raiz_de_numero_negativo(monkeypatch, capsys):
    ejecutar_calculadora(monkeypatch, ["6", "-4", "8"])

    assert "No se puede calcular la raíz cuadrada de un número negativo" in capsys.readouterr().out
