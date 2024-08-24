#Implemente uma função que indique se uma matriz quadrada de números inteiros é uma matriz identidade ou não. 
# A função deve retornar 1 se a matriz  for  uma matriz identidade e caso contrário. 
# A função recebe como parâmetros a matriz de inteiros, usando a representação de matrizes através de 
# vetores sinples e um número n , indicando a dimensão da matriz. 
# Essa função deve obedecer ao protótipo: int matriz_identidade(int *mat,int n)

def matriz_identidade(mat, n):
    return all(mat[i * n + i] == 1 and all(mat[i * n + j] == 0 for j in range(n) if j != i) for i in range(n))