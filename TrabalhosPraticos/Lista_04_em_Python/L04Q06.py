#Implemente  um  programa  em  C  que  calcule  a  média  e  a  variância  de  um  
# conjunto  de  10  números  reais  modularizar  as funcionalidades para o cálculo 
# da média e da variância os protótipos das funções media e variancia devem ser : 
# float media(int n, float* v) e float variancia (int n, float *v, float m)

def media(v):
    return sum(v) / len(v)

def variancia(v, m):
    return sum((x - m) ** 2 for x in v) / len(v)

v = [1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 10.0]

m = media(v)
var = variancia(v, m)

resultados = {'media': m, 'variancia': var}
print(resultados)