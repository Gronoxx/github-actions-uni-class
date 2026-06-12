import pytest

from src.typing_rate import contar_palavras, calcular_ppm, calcular_cpm, ppm_padrao, calcular_precisao, calcular_ipm

def test_contar_palavras():
    assert contar_palavras("hello world") == 2
    assert contar_palavras("") == 0
    assert contar_palavras("one two three four five six") == 6

def test_calcular_ppm():
    assert calcular_ppm(50, 60) == 50.0
    assert calcular_ppm(120, 120) == 60.0

def test_calcular_cpm():
    assert calcular_cpm(300, 60) == 300.0

def test_ppm_padrao():
    assert ppm_padrao("abcde" * 5, 60) == 5.0

def test_calcular_precisao():
    assert calcular_precisao("abcd", "abcd") == 100.0
    assert calcular_precisao("axcd", "abcd") == 75.0
    assert calcular_precisao("ab", "abcd") == 50.0

def test_tempo_invalido():
    with pytest.raises(ValueError):
        calcular_ipm(100, 0)
    with pytest.raises(ValueError):
        calcular_ppm(50, -10)

def test_precisao_texto_vazio():
    with pytest.raises(ValueError):
        calcular_precisao("", "")

def test_contar_palavras_espacos_irregulares():
    assert contar_palavras("   hello    world  ") == 2
    assert contar_palavras("\t\n foo \n bar \t baz \n") == 3
    assert contar_palavras("        ") == 0 
    assert contar_palavras("solo") == 1

def test_calcular_ppm_valores_quebrados():
    assert calcular_ppm(10, 7) == pytest.approx(85.71428571)
    assert calcular_ppm(5, 2.5) == 120.0

def test_calcular_cpm_quebrado_e_grande():
    assert calcular_cpm(250, 45) == pytest.approx(333.33333333)
    assert calcular_cpm(1_000_000, 1) == 60_000_000.0

def test_ppm_padrao_texto_irregular():
    assert ppm_padrao("hello world", 30) == pytest.approx(4.4)

def test_precisao_bordas_agressivas():
    assert calcular_precisao("xxxx", "abcd") == 0.0
    assert calcular_precisao("abcdef", "abcd") == pytest.approx(66.66666667)
    assert calcular_precisao("", "abcd") == 0.0
    assert calcular_precisao("ax", "abc") == pytest.approx(33.33333333)

def test_ipm_tempo_zero_float():
    with pytest.raises(ValueError):
        calcular_ipm(100, 0.0)
