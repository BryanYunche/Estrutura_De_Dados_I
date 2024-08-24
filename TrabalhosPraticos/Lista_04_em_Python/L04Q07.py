import ctypes

def media(v):
    return sum(v) / len(v)

def variancia(v, m):
    return sum((x - m) ** 2 for x in v) / len(v)

n = 10
v = (ctypes.c_float * n)(*([1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 10.0]))

m = media(v)
print({'media': m, 'variancia': variancia(v, m)})