def media(v):
    return sum(v) / len(v)

def variancia(v, m):
    return sum((x - m) ** 2 for x in v) / len(v)

v = [1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 10.0]

m = media(v)
var = variancia(v, m)

resultados = {'media': m, 'variancia': var}
print(resultados)