def avalia(coeficientes, x):
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** i)
    return resultado