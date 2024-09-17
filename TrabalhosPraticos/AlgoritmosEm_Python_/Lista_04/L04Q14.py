#Implemente  uma  função  avalia,  que  permite  avaliação  de  polinômios.  
# Cada  polinômio  é  definido  é  definido  por  um  vetor 
# contendo coeficientes. Por exemplo, o polinômio 3x2+2x+12, 
# terá um vetor de coeficientes igual a v[ ]={12,2,3}. A função avalia deve obedecer ao protótipo: 


def avalia(coeficientes, x):
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** i)
    return resultado