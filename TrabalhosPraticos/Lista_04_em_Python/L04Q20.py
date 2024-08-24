#Implemente uma função que calcule a transposta de uma matriz mat. 
# A função tem como valor de retorno o ponteiro do vetor que representa a matriz transposta criada. 
# A implementação dessa função deve ser dada por: 
# float * transposta (int m,int n, float** mat)  OBS:utilizar vetor de ponteiros 

def transposta(m, n, mat):
    return [[mat[i][j] for i in range(m)] for j in range(n)]