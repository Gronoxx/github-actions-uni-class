def contar_palavras(texto):
    splitted_text = texto.split()
    return len(splitted_text)

def calcular_ipm(item, segundos):
    if segundos <= 0:
        raise ValueError("time is invalid")
    ipm = (item / segundos) * 60
    return ipm

def calcular_ppm(num_palavras,segundos):
    return calcular_ipm(num_palavras,segundos)

def calcular_cpm(num_caracteres, segundos):
    return calcular_ipm(num_caracteres,segundos)

def ppm_padrao(texto, segundos):
    quantidade_palavras_padrao = len(texto)/5
    return calcular_ipm(quantidade_palavras_padrao,segundos)

def calcular_precisao(digitado, esperado):
    quantidade_caracteres = max(len(digitado), len(esperado))
    if quantidade_caracteres == 0:
        raise ValueError ("No text to evaluate precision")
    quantia_erros = 0
    for caracteres in zip(digitado,esperado):
        if caracteres[0] != caracteres[1]:
            quantia_erros += 1
    quantia_erros += abs(len(digitado) - len(esperado))
    return (1 - quantia_erros/quantidade_caracteres) * 100