#Implementar o  exercício 6 utilizando alocação dinâmica de memória, sugestões: 
# para fazer a alocação dinâmica use: v=(float  *)malloc(n*sizeof(float))  ,  
# testar  para  ver  se  existe  memória  suficiente  para  fazer  a  alocação  if(v==NULL) 
# {printf(“Memória Insuficiente\n”); exit(1);} e para liberar o espaço de memória use free(v);

import ctypes

def media(v):
    return sum(v) / len(v)

def variancia(v, m):
    return sum((x - m) ** 2 for x in v) / len(v)

n = 10
v = (ctypes.c_float * n)(*([1.5, 2.0, 3.5, 4.0, 5.5, 6.0, 7.5, 8.0, 9.5, 10.0]))

m = media(v)
print({'media': m, 'variancia': variancia(v, m)})